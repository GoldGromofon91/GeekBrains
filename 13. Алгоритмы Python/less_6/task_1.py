from memory_profiler import profile, memory_usage
import timeit
import time


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


# 1.
@profile
def func():
    usr_number = 123123123877789
    num = 0
    while usr_number > 0:
        perc = usr_number % 10
        if perc > num:
            num = perc
        usr_number //= 10
    return num


@profile
def modify():
    usr_number = '123123123877789'  # input('Введите любое число: ')
    usr_str = list(usr_number)
    return max(usr_str)


# print(timeit.timeit("func()", setup="from __main__ import func", number=10000))
# print(timeit.timeit("modify()", setup="from __main__ import modify", number=10000))
# 2.
firm_list = [
    {'name': 'Apple', 'cost': 20783},
    {'name': 'Google', 'cost': 20532},
    {'name': 'Mail', 'cost': 15089},
    {'name': 'Facebook', 'cost': 18953},
    {'name': 'Yandex', 'cost': 15321},
    {'name': 'Amazon', 'cost': 19845}
]


@profile
def func2(firm_list):
    gen_list = [(elem.get('cost')) for elem in firm_list]
    gen = sorted(gen_list, reverse=True)[0:3]
    for element in firm_list:
        for key, val in element.items():
            if val in gen:
                print('{} - {}'.format(key, val))


@profile
def modify_2(firm_list):
    res = []
    for el in firm_list:
        s = list(el.items())
        res.append(s)
    res.sort(key=lambda i: i[1], reverse=True)
    print(res[:3])
    del firm_list
    del res


# print(timeit.timeit("func2(firm_list)", setup="from __main__ import func2,firm_list", number=10))
# print(timeit.timeit("modify_2(firm_list)", setup="from __main__ import modify_2,firm_list", number=10))


# 3.

@profile
def reverse_string(s):
    if not s:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])


@memorize
@profile
def reverse_string_m(s):
    if not s:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])


if __name__ == '__main__':
    func()
    modify()
    """ Домашнее задание урока №1 (Основы введения Python)
        !!! Алгоритм поиска самой большой цифры в числе.
        Функция func() - Сложность О(N) - линейная.
        Профилирование памяти показывает,что алгоритм поиска дополнительную память (Increment) не выделяет,
        а значит оптимизировать данный код по памяти не требуется.
        ОДНАКО, данную функцию можно оптимизировать
        Функция modify() - Сложность O(len) - зависит от длины.
        Профилирование памяти показывает,что  алгоритм требует столько же памяти как и первый. Однако он использует
        встроенные функции, и синтаксически лаконичен.
        При проведении замеров быстродействия функция modify() показала явное преимущество в скорости выполнения за счет встроенных функкий
        func() - 0.040931775000000004
        modify()-0.01834691999999999
        func() Mem usage- 10,3MiB
        modify() Mem usage- 10,3MiB
        Оптимизация проведена успешно!
    """
    ts = time.process_time()
    ms = memory_usage()
    func2(firm_list)
    tf = time.process_time()
    mf = memory_usage()
    tdiff = tf - ts
    mdiff = mf[0] - ms[0]
    print('Время поиска ', tdiff, mdiff)

    ts = time.process_time()
    ms = memory_usage()
    modify_2(firm_list)
    tf = time.process_time()
    mf = memory_usage()
    tdiff = tf - ts
    mdiff = mf[0] - ms[0]
    print('Время поиска (модификация) ', tdiff, mdiff)
    """ Домашнее задание c курса (Алгоритмы Python)
        !!! Алгоритм поиска самой большой цифры в числе.
        Функция func2() - Сложность О(N^2) - квадратичная(вложенные циклы).
        Профилирование памяти показывает,что алгоритм поиска дополнительную память (Increment) не выделяет,
        а значит оптимизировать данный код по памяти не требуется.
        ОДНАКО, данную функцию можно оптимизировать
        Функция modify() - Сложность O(nlogn) - логарифмическая.
        Профилирование памяти показывает,что  алгоритм требует столько же памяти как и первый. Однако он использует
        встроенные функции, и синтаксически лаконичен.
        При проведении замеров быстродействия функция modify_2() показала явное преимущество в скорости выполнения за 
        счет встроенных функкий
        func2() - 0.0070260000000000045
        modify_2()-0.006520999999999999
        func2() Usage Memory:0.0
        modify_2() Usage Memory:0.0
        Оптимизация проведена успешно!
    """
    ts = time.process_time()
    ms = memory_usage()
    reverse_string(str(range(0, 1000)))
    tf = time.process_time()
    mf = memory_usage()
    tdiff = tf - ts
    mdiff = mf[0] - ms[0]
    print('Время реверса строки', tdiff, mdiff)

    ts1 = time.process_time()
    ms1 = memory_usage()
    reverse_string_m(str(range(0, 1000)))
    tf1 = time.process_time()
    mf1 = memory_usage()
    tdiff1 = tf1 - ts1
    mdiff1 = mf1[0] - ms1[0]
    print('Время реверса+мемоизация строки', tdiff1, mdiff1)
    """ Домашнее задание c курса (Алгоритмы Python)
        !!! Алгоритм реверса строки.
         Функция reverse_string()- Сложность О(n!) - факториальная(рекурсия).
        Профилирование памяти показывает,что алгоритм реверса строки(на основе рекурсии) использует 0.0390625 MiB 
        (хотя профилирование через @profile округляет такие несерьезные значения и выводит 0)
        
        ОДНАКО, данную функцию можно оптимизировать:
        Функция reverse_string_m() + @memorize - Сложность O(n!) - факториальная(рекурсия), но благодаря мемоизации
        отсутсвуют дубли рекурсии, что позволяет оптимизировать память в 3 раза до 0.0078125 MiB
        
        reverse_string() - 0.522173
        reverse_string_m()-0.499957
        reverse_string() - Usage Memory:0.0390625
        reverse_string_m()- Usage Memory:0.0078125
        Оптимизация проведена успешно!
    """
