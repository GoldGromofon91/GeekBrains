print('Здравствуйте! Эта программа вычислит факториал любого числа n!')
usr_num = int(input('Введите число n: '))


def my_fact(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
        yield i, res


for check, el in my_fact(usr_num):
    print(f'Факториал числа {check}: {el}')
