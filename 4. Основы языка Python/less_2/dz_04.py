print('Здравсвтуйте! Данная программа будет разбивать одно предложение на строки!')
usr_str = input('Введите любое предложение, слова разделяйте " "!: ')
edit_string = usr_str.split()
for ind, el in enumerate(edit_string, 1):
    if len(el) > 10:
        el = el[:10]
    print(ind, el)
