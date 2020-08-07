"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from datetime import datetime
import time, random

res = []
def time_decorator(function_to_decorate):
     def wrapper_my_func():
         start_time = datetime.now()
         function_to_decorate() 
         print(f'Время выполнения: {datetime.now() - start_time}')
     return wrapper_my_func

@time_decorator
def create_list():
	list = [random.randint(1,100) for i in range(20)]
	print(list)
	return list

create_list()

"""
Чтобы не создавать отдельно список ключей, создал список словарей, т.к словари это хеш-таблицы время заполения такого списка
меньше, чем заполнение списка любыми другими элементами
"""
@time_decorator
def create_dict():
	new_dict=[{'id'+str(el):random.randint(1,100)} for el in range(1,21)]
	print(new_dict)
	return new_dict

create_dict()

