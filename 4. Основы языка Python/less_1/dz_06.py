usr_start = int(input('Введите количество километров в день, со скольки вы начали бегать: '))
usr_finish = int(input('Введите количество километров в день, которое хотите достичь: '))
usr_increase = int(input('Введите значение на которое вы будите увеличивать количество километров в (%): '))
percent = usr_increase / 100
day = 1
print(f'{day}-й день: {usr_start}')
while usr_start <= usr_finish:
    day +=1
    usr_start = usr_start + (usr_start * percent)
    print(f'{day} - й день: {round(usr_start,2)}')
print(f'На {day}-й день вы достигнете результат не менее {usr_finish}')