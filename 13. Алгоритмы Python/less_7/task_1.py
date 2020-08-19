"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import time
from random import randint

from memory_profiler import memory_usage


def memory_check(function_to_decorate):
    def wrapper_my_func():
        ms1 = memory_usage()
        function_to_decorate()
        mf1 = memory_usage()
        mdiff1 = mf1[0] - ms1[0]
        print(f'Количество выделенной памяти: {mdiff1} Mib')

    return wrapper_my_func


# @memory_check
def buble(ulist):
    n = 1
    while n < len(ulist):
        for i in range(len(ulist) - n):
            if ulist[i] < ulist[i + 1]:
                ulist[i], ulist[i + 1] = ulist[i + 1], ulist[i]
        n += 1


# @memory_check
def buble2(ulist):
    buble_flag = True
    while buble_flag:
        buble_flag = False
        for i in range(len(ulist) - 1):
            if ulist[i] < ulist[i + 1]:
                ulist[i], ulist[i + 1] = ulist[i + 1], ulist[i]
                buble_flag = True



lst_obj = [randint(-100, 100) for i in range(1000)]
print(timeit.timeit("buble(lst_obj)", setup="from __main__ import buble,lst_obj", number=1))

lst_obj = [randint(-100, 100) for i in range(1000)]
print(timeit.timeit("buble2(lst_obj)", setup="from __main__ import buble2,lst_obj", number=1))

""" 
    !!!. Попытка доработать алгоритм сортировки "Пузырьком" путем добавления флага в цикл while с целью исключения 
    лишнего прохода(если все элементы отсортированы)  выйгрыша по времени не дала! 
"""
