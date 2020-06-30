usr_numb = int(input('Введите число n от "0" до "100": '))
usr_str = str(usr_numb)
sum_str_1 = usr_str + usr_str
sum_str_2 = usr_str + usr_str + usr_str
sum_numb = usr_numb + int(sum_str_1) + int(sum_str_2)
print(f'Сумма числа {usr_numb} в формате "n + nn + nnn" равна: {sum_numb}')
