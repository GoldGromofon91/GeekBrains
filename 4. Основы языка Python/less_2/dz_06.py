print('Пример создания программы склада')
usr_list = []
i = 1
while True:
    usr_name = input('Введите название товара: ')
    usr_coast = int(input('Введите стоимость товара: '))
    usr_quantity = int(input('Введите количество товара: '))
    usr_unit = input('Введите единицу измерения: ')
    usr_opinion = input('Для продолжения ввода нажмите "Enter". Для выхода введите "q": ')
    res_tuple = (i, {'название': usr_name, 'цена': usr_coast, 'количество': usr_quantity,
                     'ед.': usr_unit})
    usr_list.append(res_tuple)
    i +=1
    if usr_opinion == 'q':
        break
print(f'Ваш текущий список товаров: {usr_list}')
res_usr_dict = {}
for count in usr_list:
    for key, val in count[1].items():
        if res_usr_dict.get(key):
            res_usr_dict[key].append(val)
        else:
            res_usr_dict[key] = [val]
print(f'Итоговый список товаров {res_usr_dict}')