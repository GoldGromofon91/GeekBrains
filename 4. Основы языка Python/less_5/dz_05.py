def change(num):
    num_list = num.split()
    int_list = []
    for i in num_list:
        i = int(i)
        int_list.append(i)
    return int_list


with open('dz_05.txt', 'w') as f:
    usr_num = input('Введите числа через пробел: ')
    sum = sum(change(usr_num))
    print(f'Файл записан!\nВведенные числа: {usr_num}\nСумма чисел: {sum}')
    f.write('Ваши числа: ' + f'{usr_num}\n' + f'Сумма чисел равна: {str(sum)}')
