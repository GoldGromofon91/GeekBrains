"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


"""
Решение: Создал в Mysql таблицу auth, сгенерировал значение в json. Перенес значения
из json в python, если ключ active = 0 -->предлагаем пройти аутентификацию.

Cложность: О(n)
"""
import json

with open('/Users/nikita_sv/Desktop/Work_GB/13. Алгоритмы Python/less_1/auth.json','r') as f: #O(1)
	auth_json = json.loads(f.read())	#O(1)

def check_auth(auth_json):
	for elem in auth_json: # O(n)
		if elem['active'] == '0':	#O(1)
			user_auth = input('Пользователь {} - Войдите на ресурс(введите 1): '.format(elem['login']))
			if user_auth == 1: #O(1)
				elem['active'] == '1' #O(1)
		else:
			print('Пользователь {} - online'.format(elem['login']))
	return auth_json
print('Список Список исходных пользователей:\n', auth_json)
check_auth(auth_json)

















