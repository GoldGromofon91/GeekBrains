"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from random import randint
from statistics import median


def gnom_style(lst_obj):
    i, j, size = 1, 2, len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i, j = j, j + 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst_obj


def srch_median(num):
    length = (2 * num) + 1
    lst_obj = [randint(0, 50) for _ in range(length)]
    print(lst_obj)
    print(f'Гномья сортировка:\n{gnom_style(lst_obj)}')
    if length < 1:
        return None
    if length % 2 == 1:
        return gnom_style(lst_obj)[length // 2]
    else:
        return sum(gnom_style(lst_obj)[length // 2 - 1:length // 2 + 1]) / 2.0


usr_num = int(input('enter num: '))
mediana = srch_median(usr_num)
print(f'Медиана: {mediana}')
