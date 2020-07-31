"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
import random

# 2.1 Сложность: О(3n^2)

rand_list1 = [random.randint(1,100) for x in range(10)] # O(n)
print(rand_list1)
def search_min1(us_list):
	min_numb = us_list[0]
	for i in range(len(us_list)):
		for el in us_list:
			if el < min_numb:
				min_numb = el
				min_index = i
	return 'Минимальное число №1: {}'.format(min_numb)
print(search_min1(rand_list1)) 

# 2.2 Сложность О(2n)

rand_list2 = [random.randint(1,100) for x in range(10)] # O(n)
print(rand_list2)

def search_min2(us_list):
	min_numb = us_list[0]
	for i in range(len(us_list)):
		if us_list[i] < min_numb:
			min_numb = us_list[i]
	return 'Минимальное число №2: {}'.format(min_numb)
print(search_min2(rand_list2)) 













