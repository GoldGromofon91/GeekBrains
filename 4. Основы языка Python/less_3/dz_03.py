# Простой способ
n_1 = int(input('Введите первое число: '))
n_2 = int(input('Введите второе число: '))
n_3 = int(input('Введите третье число: '))

def my_func(a, b, c):
    if a < b:
        m = a
    else:
        m = b
    if c < m:
        m = c
    sum_numb = a + b + c - m
    return sum_numb

print(my_func(n_1, n_2, n_3))

# через список
number = input('Введите три числа через пробел: ').split()
res_list = []

def my_func2(list_u):
    summa = []
    for i in list_u:
        i = int(i)
        summa.append(i)
    while len(summa)!=1:
        max_n = max(summa)
        summa.remove(max_n)
        res_list.append(max_n)
    return sum(res_list)

print(my_func2(number))
