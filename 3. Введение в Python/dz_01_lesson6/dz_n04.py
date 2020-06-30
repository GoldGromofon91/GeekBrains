def situation (number):
    if number == 13:
        raise ValueError ('Число 13')
    else:
        return number ** 2
usr_number = int(input('Введите число от 0 до 100 '))
try:
    res_numb = situation(usr_number)
except ValueError:
    print('Вы ввели число 13')
else:
    print('Число в квадрате = ', res_numb)