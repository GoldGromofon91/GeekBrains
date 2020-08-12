"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict
import random

def start():
	firm_dict = defaultdict(list)
	cost_firm = defaultdict(list)
	start = 0
	summ_all = 0
	cost_elem = 0
	max_cst_frm = ''
	min_cst_frm = ''
	try:
		num_manufacture= int(input('Введите количество предприятий для расчета прибыли: '))
	except (TypeError, ValueError):
		print(f'Ошибка {E}! Введите количество предприятий цифрами!')
	
	while start < num_manufacture:
		name_manufacture = input(f'Введите название {start + 1}-го предприятия: ')
		cost_manufacture = input('Через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ')
		firm_dict[name_manufacture].append(cost_manufacture)
		start +=1
	else:
		usr_choice = input('Для продолжения введите "n", для выхода "q": ')
		if usr_choice == 'q':
			return print('Bye')
		else:
			pass
	
	for elem in firm_dict:
		for j in firm_dict[elem]:
			cost_elem = sum(list(map(int,j.split())))
			summ_all = summ_all + cost_elem
			cost_firm[elem].append(cost_elem)
	
	print(f'Средняя годовая прибыль всех предприятий: {(summ_all / 4) / num_manufacture}')
	
	for el_cst in cost_firm:
		for j in cost_firm[el_cst]:
			if j > (summ_all / 4) / num_manufacture:
				max_cst_frm = el_cst
			else:
				min_cst_frm = el_cst

	print(f'Предприятия, с прибылью выше среднего значения: {max_cst_frm}\nПредприятия, с прибылью ниже среднего значения: {min_cst_frm}')


start()










