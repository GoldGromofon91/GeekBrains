usr_list = list(input('Введите любой набор элементов: '))
print(f'Ваш список: {usr_list}')
print(f'Вы создали список: {usr_list}, длинной {len(usr_list)} символов')
i = 0
for count in range(int(len(usr_list) / 2)):
    usr_list[i], usr_list[i + 1] = usr_list[i + 1], usr_list[i]
    i += 2
print(f'Ваш новый список {usr_list}')
