class MyError(Exception):

    def __str__(self):
        return 'Error! Вы ввели 0, на ноль делить нельзя!'


usr_data1 = input('Введите 1-е число: ')
usr_data2 = input('Введите 2-е число: ')

try:
    usr_numb1 = int(usr_data1)
    usr_numb2 = int(usr_data2)
    if usr_numb2 == 0:
        raise MyError()
    # usr_del = usr_numb1 / usr_numb2
except ValueError:
    print('Вы ввели не числа')
except MyError as err:
    print(err)
else:
    print('Error not found!')
    usr_del = usr_numb1 / usr_numb2
    print(f'Результат деления: {usr_del}')


