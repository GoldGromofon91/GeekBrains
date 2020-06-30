# Через функции
def sort_int(numbers):
    result = []
    for i in numbers:
        if i == 'q':
            break
        else:
            i = int(i)
            result.append(i)
    return result

running = True
res_sum = 0
while running:
    usr_number = input(
        'Введите числа через "пробел". ' + 'Для вывода суммы нажмите Enter!. Для выхода нажмите "q": ').split()
    print(usr_number)
    if usr_number != ['q']:
        summa = sum(sort_int(usr_number))
        res_sum = res_sum + summa
        print(f'Сумма чисел равна: {res_sum}')
    else:
        print(f'Сумма ваших чисел равна: {res_sum}. До свидания!')
        break

# Без функций
running = True
res_sum = 0
while running:
    usr_number = input(
        'Введите числа через "пробел". ' + 'Для вывода суммы нажмите Enter!. Для выхода нажмите "q": ').split()
    # result = [] - оптимизация
    for i in usr_number:
        if i == 'q':
            # print('До свидания!') - оптимизация
            running = False
        else:
            # i = int(i)
            # result.append(i) - оптимизация
            # summa = sum(result) - оптимизация
            res_sum = res_sum + int(i)
    print(f'Сумма ваших чисел равна: {res_sum}')
    if usr_number == ['q']:
        print('До свидания!')
        break
