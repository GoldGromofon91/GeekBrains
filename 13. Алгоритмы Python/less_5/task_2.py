"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
#C использованием модуля collections


# Решение c ООП
class Clc_16x:
    def __init__(self, num):
        self.num = num
        self.sum_res = []
        self.mul_res = []


    def __add__(self, other):
        summ = hex(int(self.num, 16) + int(other.num,16))
        for el in range(2,len(summ)):
        	self.sum_res.append(summ[el].upper())
        return self.sum_res


    def __mul__(self, other):
        multx = hex(int(self.num, 16) * int(other.num, 16))
        print()
        for el in range(2,len(multx)):
        	self.mul_res.append(multx[el].upper())
        return self.mul_res


if __name__ == '__main__':
    calc_obj = Clc_16x(input('Введите 1-е число в 16-м формате: '))
    calc_obj_2 = Clc_16x(input('Введите 2-е число в 16-м формате: '))
    print(f'Сумма чисел равна:{calc_obj + calc_obj_2}\nПроизведение чисел равно: {calc_obj * calc_obj_2}')

