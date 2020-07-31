"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
"""Пример создания стека через ООП"""


class PlatesClass:
	def __init__(self):
		self.some_list = []

	def clear(self):
		return self.some_list.clear()

	def is_empty(self):
		return self.some_list == []

	def add_el(self,elem):
		self.some_list.append(elem)

	def pop_el(self):
		return self.some_list.pop()

	def del_el(self,elem):
		return self.some_list.remove(elem)

	def get_last_val(self):
		return self.some_list[len(self.some_list) - 1]

	def get_val(self,el):
		for i in range(len(self.some_list)):
			if (el - 1) == i:
				print('Объект №{} - {}'.format(el,self.some_list[i]))

	def all(self):
		for el in enumerate(self.some_list,1):
			print (el)

	def size(self):
		return len(self.some_list)

"""
Решение 1.Данная функция разбивает элементы только по двум стопкам в равном количестве
def create_obj(size_stack):
	PlC_OBJ.clear()
	PlC_OBJ_2.clear()
	lenght = 1 
	while lenght <= size_stack //2 :
		PlC_OBJ.add_el('Стопка 1. Тарелка {}'.format(lenght))
		lenght = lenght + 1 
	else:
		for i in range(size_stack - (size_stack //2)):
			PlC_OBJ_2.add_el('Стопка 2. Тарелка {}'.format(i+1))
	return 'Заполнены'	
"""
# Решение 2.

def create_N_stack(count_obj):
	lenght_stack_max = 5
	plates_list = []
	integer = count_obj // lenght_stack_max
	remainder = count_obj % lenght_stack_max
	if (integer == 0) and (remainder != 0):
		plates_list.append(PlatesClass())
	elif (integer % 2 != 0) and (remainder == 0):
		for i in range(integer):
			plates_list.append(PlatesClass())
	elif (integer % 2 == 0) and (remainder == 0):
		for i in range(integer):
			plates_list.append(PlatesClass())
	else:
		for i in range(integer + 1):
			plates_list.append(PlatesClass())
	return plates_list

def create_N_obj(count_obj):
	lenght_stack_max = 5
	plates_list = create_N_stack(count_obj)
	
	while count_obj > 0:
		for ind in range(len(plates_list)):
			if plates_list[ind].is_empty():
				for el in range(5):
					plates_list[ind].add_el('Стопка№{}. Тарелка№{}'.format(ind + 1,el + 1))
					count_obj = count_obj - 1
			else:
				continue

	return plates_list

if __name__ == '__main__':
	test = create_N_obj(20)
	print('Переменная test: {},\n Длина: {}\n Содержит в себе:\n {}'.format(type(test), len(test),test))
	
	obj_1 = test[0]
	obj_2 = test[1]
	obj_3 = test[2]
	obj_4 = test[3]

	obj_1.all()
	obj_2.all()
	obj_3.all()
	obj_4.all()











