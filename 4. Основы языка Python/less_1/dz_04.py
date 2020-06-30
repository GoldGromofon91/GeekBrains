# при использовании функции max
usr_number = int(input('Введите число n: '))
usr_str = list(str(usr_number))
print(max(usr_str))

# при использовании цикла wile and if
usr_number = int(input('Введите любое число n: '))
num = 0
while usr_number > 0:
    perc = usr_number % 10
    if perc > num:
        num = perc
    usr_number //= 10
print(f'Самая большая цифра в вашем числе n: {num}')
