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


def create_N_obj(size_stack):
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

if __name__ == '__main__':
	PlC_OBJ = PlatesClass()
	PlC_OBJ_2 = PlatesClass()

	print(create_N_obj(12))
	PlC_OBJ.all()
	PlC_OBJ_2.all()
	print('=' * 40)
	print(create_N_obj(20))
	PlC_OBJ.all()
	PlC_OBJ_2.all()















