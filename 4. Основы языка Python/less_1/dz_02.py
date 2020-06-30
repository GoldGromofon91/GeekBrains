print('Здравсвтуйте! Программа перевед любое количество секунд в формат ЧЧ:ММ:СС')
usr_time = int(input('Сколько секунд вы хотите перевести в формат: "ЧЧ:ММ:СС": '))
hour = usr_time // 3600
minutes = (usr_time // 60) % 60
second = usr_time % 60

print(f'Время составляет {hour}ч:{minutes}м:{second}с')
