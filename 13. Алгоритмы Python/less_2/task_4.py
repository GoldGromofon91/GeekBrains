"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
# Решение 1
# start = 1 
# usr_num = int(input('Введите количество элементов: '))

# def rec_sum(num_start, count):
# 	# print(num_start, count)
# 	if count % 2 == 0 :
# 		num_start = num_start *(-1)
# 		# print(f'New number- {num_start}')
# 	elif num_start < 0 and count % 2 !=0:
# 		# new = num_start * (-1)
# 		num_start = num_start *(-1)
# 	if count == 1:
# 		return num_start
# 	else:
# 		return rec_sum(-num_start/2, count - 1) + num_start

# print (f'Количество элементов: {usr_num}, Сумма: {rec_sum(start,usr_num)}')

# Решение 2 (без условий смены знака)
start = 1 
usr_num = int(input('Введите количество элементов: '))

def rec_sum(num_start, count):
	if count == 1:
		return num_start
	else:
		return rec_sum(-num_start/2, count - 1) + num_start
print (f'Количество элементов: {usr_num}, Сумма: {rec_sum(start,usr_num)}')
