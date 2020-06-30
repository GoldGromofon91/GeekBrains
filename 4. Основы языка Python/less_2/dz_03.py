usr_answer = int(input('Введите месяц в формате числа "1-12": '))
seasons = {
    'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]
}
for key, val in seasons.items():
    if usr_answer in val:
        print(f'Время года: {key}')
