"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib

def transformat(string):
	hash_user_obj = hashlib.sha256(string.encode('ascii'))
	salt_hash = hashlib.sha224('dz03'.encode('ascii'))
	res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
	return res_pass


hs_set = set() 
usr_str = input('Введите строку:')
for i in range(len(usr_str)):
	for j in range(len(usr_str),i,-1):
		hs_set.add(transformat(usr_str[i:j]))
print(f'Количество уникальных хешей-подстрок: {len(hs_set)}\nУникальные кеши:\n' + '*' * 100 + f'\n{hs_set}\n' + '*' * 100)






