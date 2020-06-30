# Вариант 1
import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, color):
        if color == 'Red':
            self.__color = color
            print(self.__color)
            time.sleep(2)
        elif color == 'Yellow' and self.__color == 'Red':
            self.__color = color
            print(self.__color)
            time.sleep(2)
        elif color == 'Green' and self.__color == 'Yellow':
            self.__color = color
            print(self.__color)
            time.sleep(2)
        else:
            print('Ошибка ввода')


l = TrafficLight()
l.running('Red')
l.running('Yellow')
l.running('Green')
l.running('Yellow')


# Вариант2
class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        usr_count = int(input('Сколько раз вы хотите запустить светофор?: '))
        check = 0
        while check < usr_count:
            for el in self.__color:
                check += 1
                if el == 'Красный':
                    print(f'{el}...')

                    time.sleep(7)
                elif el == 'Желтый':
                    print(f'{el}...')

                    time.sleep(5)
                elif el == 'Зеленый':
                    print(f'{el}...')

                    time.sleep(2)
        else:
            print('До свидания!')


usr_opinion = input('Программа светофор! Для запуска нажмите "start": ')
if usr_opinion == 'start' or 'Start':
    light = TrafficLight()
    light.running()
