import random
# Стандартно через функции
usr_list = [random.randint(1, 200) for i in range(15)]
print(f'Сгенерированный список: {usr_list}')

def my_filter(numbers):
    res = []
    for i in range(1, len(numbers), 1):
        if numbers[i] > numbers[i - 1]:
            res.append(numbers[i])
    return res

print('Итоговый список: {}'.format(my_filter(usr_list)))

# Оптимизация
print('*' * 20 + ' Результат с оптимизацией ' + '*' * 20)
print(f'Сгенерированный список: {usr_list}')
res_list = [usr_list[i] for i in range(1, len(usr_list), 1) if usr_list[i] > usr_list[i - 1]]
print('Итоговый список:', res_list)
