"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
"""

"""

import random

class KworkBoard:
    def __init__(self):
        self.basic_kwork = []
        self.unsolved_kwork = []
    
    def is_empty(self):
        return self.basic_kwork == []

    def all(self):
        print('Список выполненных задач:\n{}\nСписок задач на доработке:\n{}'.format(self.basic_kwork,self.unsolved_kwork))
    
    def add_kwork(self,el):
        if len(el) <=1:
            for i in el:
                if i['status'] == 0:
                    self.unsolved_kwork.append(i)
                else:
                    self.basic_kwork.append(i)
        elif len(el) > 1:
            for i in el:
                if i['status'] == 0:
                    self.unsolved_kwork.append(i)
                else:
                    self.basic_kwork.append(i)

    def execute_all(self):
        for idx in range(len(self.unsolved_kwork)): 
            for elem in self.unsolved_kwork:
                if elem['status'] == 0:
                    elem['content'] = 'EDIT SOMETHING'
                    elem['status'] = 1
                    self.basic_kwork.append(elem)
                    self.unsolved_kwork.remove(elem)

    def add_to_front(self, elem):
        self.basic_kwork.append(elem)

    def add_to_rear(self, elem):
        self.basic_kwork.insert(0, elem)

    def remove_from_front(self):
        return self.basic_kwork.pop()

    def remove_from_rear(self):
        return self.basic_kwork.pop(0)

    def size_basic_stack(self):
        return len(self.basic_kwork)


def generate_data(length):
	return [{'id':i + 1,'content':'text','status':random.randint(0, 1)} for i in range(length)]



if __name__ == '__main__':
    kb_obj = KworkBoard()
    input_data = generate_data(10) # N - число сколько данных необъходимо сгенерировать
    kb_obj.add_kwork(input_data)
    kb_obj.add_kwork([{'id':13,'content':'text','status':0}])
    print('Вывод всех задач из двух очередей:\n')
    kb_obj.all()
    print ('='*80)
    kb_obj.execute_all()
    print('После выполнения всех заданий, вывод результата')
    kb_obj.all()






