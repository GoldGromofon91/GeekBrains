"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge(usr_list):
    i, j, k = 0, 0, 0
    if len(usr_list) > 1:
        center = len(usr_list) // 2
        left = usr_list[:center]
        right = usr_list[center:]
        merge(left)
        merge(right)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                usr_list[k] = left[i]
                i += 1
            else:
                usr_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            usr_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            usr_list[k] = right[j]
            j += 1
            k += 1
        return usr_list


usr_num = int(input('Введите число элементов: '))
rnd = [random.uniform(0, 50) for _ in range(usr_num)]
print(f'Исходный список:{rnd}')
print(f'Отсортированный список:{rnd}')
print(f'Время выполнения: {timeit.timeit("merge(rnd)", setup="from __main__ import merge,usr_num,rnd", number=1)}')