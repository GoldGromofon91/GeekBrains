"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import  timeit
import cProfile

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def revers_mem(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def run_cprof():
    revers(1234563)
    revers_mem(1234563)
    revers_2(1234563)
    revers_3(1234563)


print(f'Func reverse_1:\n{timeit("revers(1234563)", setup="from __main__ import revers", number=100000)}')
print(f'Func reverse_mem:\n{timeit("revers_mem(1234563)", setup="from __main__ import revers_mem", number=100000)}')
print(f'Func reverse_2:\n{timeit("revers_2(1234563)", setup="from __main__ import revers_2", number=100000)}')
print(f'Func reverse_3:\n{timeit("revers_3(1234563)", setup="from __main__ import revers_3", number=100000)}')

cProfile.run('revers(123456)')
cProfile.run('revers_mem(123456)')
cProfile.run('revers_2(123456)')
cProfile.run('revers_3(123456)')
cProfile.run('run_cprof')

"""
!!!. По результатам замеров видно, что самая медленная функция - reverse (Рекурсивная), ее сложность Факториальная.
    Использование мемоизации ускоряет работу функции, 
    Средняя по скорости выполнения - reverse_2(Цикл) сложность линейная
    Самая быстрая функция -reverse_3 (Использование стандартных функций и взятие среза) слоность константная
"""
