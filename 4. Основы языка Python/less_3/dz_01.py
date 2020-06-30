def my_del(x, y):
    return x / y


usr_num1 = int(input('Введите первое число: '))
usr_num2 = int(input('Введите второе число: '))
try:
    res = my_del(usr_num1, usr_num2)
except ZeroDivisionError:
    print("Error! Деление на ноль.")
else:
    print(f'Результат деления {round(res,2)}')
