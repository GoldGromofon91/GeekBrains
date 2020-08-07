"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from collections import Counter
from random import randint


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Функция работает на основе модуля collections, тип данных counter(словарь).  
def mod(lst):
    ar = Counter(lst).most_common(3)[0]
    return f'Чаще всего встречается число {ar[0]}, оно появилось в массиве {ar[1]} раз(а)'

array = [randint(0,100) for i in range(1000)]

print(mod(array))
print(func_2())
print(func_1())
print(timeit("func_1()",setup="from __main__ import func_1",number=1000))
print(timeit("func_2()",setup="from __main__ import func_2",number=1000))
print(timeit("mod(array)",setup="from __main__ import mod , array",number=1000))

"""
!!!. При установочных значениях(т.е len(array) < 100)) по скорости работы выигрывает func_1 в связи с тем
что алгоритм имеет сложность О(n), func_2 содержит метод count сложность которого O(n + m)!
    
    Пытаясь улучшить код, решил воспользоваться внутренним модулем collections, на установочных значениях 
    функция mod() показывала худшее время. Однако решив усложнить задачу: путем увеличения числа повторов
    увеличив сам список, а также увеличив вероятность попадания числел (текущие значения в скрипте)-->  функция mod() 
    показала следующие результаты:
    23.520419713
    23.068806817000002
    0.10159662899999944
    Которые подводят к выводу: использование встроенных инструментов в Python правильный подход
"""







