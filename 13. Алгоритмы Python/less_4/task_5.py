"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

a = []
n=23
for i in range(n**2):
    a.append(i)
us=23
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
a.remove(0)
# print(set(a))
print(len(a))
for i in range(len(a)):
	if i == us:
		print(a[i])
	# if i == us:
		# print(a[i])
		# break
# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(9))
# print(timeit("simple(9)",setup="from __main__ import simple",number=10))
# print(timeit("simple(9)",setup="from __main__ import simple",number=100))
# print(timeit("simple(9)",setup="from __main__ import simple",number=1000))





