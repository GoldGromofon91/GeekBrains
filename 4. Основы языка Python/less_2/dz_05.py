usr_list = input('Введите какую-нибудь последовательность целых чисел через "/": ')
edit_usr_list = usr_list.split('/')
usr_sort = []
for i in edit_usr_list:
    i = int(i)
    usr_sort.append(i)
print(f'Ваша последовательность: {usr_sort}')
# print(usr_sort, type(usr_sort))
while True:
    usr_numb = input('Введите число n: . Для выхода нажмите "q" ')
    if usr_numb == 'q':
        break
    usr_sort.append(int(usr_numb))
    usr_sort = sorted(usr_sort, reverse=True)
    print(f'Теперь ваша последовательность: {usr_sort}')
print(f'Ваша последовательность {usr_sort}')

