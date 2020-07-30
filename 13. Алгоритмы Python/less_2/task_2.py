"""Рекурсия против цикла
Вывод чисел по убыванию, начиная с текущего и до нуля
"""


def count_cycle(i):
    """Цикл"""
    while i >= 0:
        print(i)
        i -= 1


count_cycle(3)


def count_recur(i):
    """Рекурсия"""
    print(i)
    # базовый случай
    if i <= 0:
        return
    # рекурсивный случай
    count_recur(i-1)


count_recur(3)
