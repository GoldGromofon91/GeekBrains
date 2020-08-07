"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from uuid import uuid4
import hashlib

def transformat(user_salt, user_pass):
	hash_user_obj = hashlib.sha256(user_pass.encode('ascii'))
	salt_hash = hashlib.sha224(user_salt.encode('ascii'))
	res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
	return res_pass


start = True
salt = 'user1'
while start: 
	us_pass = input('Введите пароль.Для выхода введите "q": ')
	if us_pass == 'q':
		print('bye')
		break
	else:
		res_pass = transformat(salt,us_pass) 
		print(f'В базе данных хранится строка: {res_pass}')
		us_pass2 = input('Введите (повторно)пароль: ')

		if transformat(salt,us_pass2) == res_pass:
			print(f'Добро пожаловать {salt}')
			break
		else:
			print('Пароль не верен. Попробуйте еще раз')
			continue

