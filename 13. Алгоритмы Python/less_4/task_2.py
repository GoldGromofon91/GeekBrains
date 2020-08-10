"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


def recursive_reverse(n):
    if n == 0:
        return str(n % 10)
    return f'{str(n % 10)}{recursive_reverse(n // 10)}'


@memorize
def recursive_reverse_mod(n):
    if n == 0:
        return str(n % 10)
    return f'{str(n % 10)}{recursive_reverse(n // 10)}'

n = 123456
print(timeit.timeit("recursive_reverse(n)", setup="from __main__ import recursive_reverse, n",number=100000))

print(timeit.timeit("recursive_reverse_mod(n)", setup="from __main__ import recursive_reverse_mod, n",number=100000))

"""
!!!. Использование декоратора-мемоизации позволять избежать вызова дублей при использовании рекурсии, что хорошо прослеживается
при N>> 
"""













