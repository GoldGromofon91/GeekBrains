"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def summ(n):
    if n == 1:
        return 1
    else:
        return n + summ(n - 1)

n = int(input('Введите число:: '))
if summ(n) == (n*(n+1))/2:
	print(f'Равенство верно!\nСумма чисел равняется: {summ(n)}')