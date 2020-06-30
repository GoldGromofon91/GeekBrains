# Через функцию.
def degree_func(x, y):
    res = x ** y
    return res


while True:
    num_1 = int(input('Введите первое целое не отрицательное число: '))
    num_2 = int(input('Введите второе целое отрицательное число: '))
    if num_1 < 0 or num_2 > 0:
        continue
    else:
        print(f'Результат возведения в степень: {degree_func(num_1, num_2)}')
        break

# Через цикл, ,без проверки правильного ввода
def degree_2(x, y):
    i = 0
    res = 1
    x = 1 / x
    while i > y:
        res = res * x
        i -= 1
    return res


print('*' * 20, ' Вариант №2 ', '*' * 20)
num_3 = int(input('Введите первое целое не отрицательное число: '))
num_4 = int(input('Введите второе целое отрицательное число: '))
print(f'Результат возведения в степень: {degree_2(num_3, num_4)}')
