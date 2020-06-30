def user_info(name, s_name, age, city, mail, phone):
    print(f'Имя:{name}. Фамилия:{s_name}. Возраст:{age}. Город:{city}. E-mail:{mail}. Телефон:{phone}')


us_name = input('Введите ваше имя: ')
us_s_name = input('Введите вашу фамилию: ')
us_age = input('Введите ваш возраст: ')
us_city = input('Введите город проживания: ')
us_mail = input('Введите ваш e-mail: ')
us_phone = input('Введите ваш телефон: ')
user_info(us_name, us_s_name, us_age, us_city, us_mail, us_phone)
