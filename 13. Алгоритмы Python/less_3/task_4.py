"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


import hashlib

def transformat(user_pass):
	hash_user_obj = hashlib.sha256(user_pass.encode('ascii'))
	salt_hash = hashlib.sha224('dz04'.encode('ascii'))
	res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
	return res_pass

class Cash_list:
    def __init__(self):
        self.urls_hash = []
    
    def is_empty(self):
        return self.urls_hash == []

    def all(self):
        print(f'Список всех url: {self.urls_hash}')
    
    def add_(self,el):
        hash_el = transformat(el)
        if hash_el not in self.urls_hash:
        	self.urls_hash.append(hash_el)
        else:
        	print('Такой url есть в базе')

    def add_to_front(self, elem):
    	hash_el = transformat(elem)
    	if hash_el not in self.urls_hash:
    		self.urls_hash.append(hash_el)
    	else:
    		print('Такой url есть в базе')

    def add_to_rear(self, elem):
    	hash_el = transformat(elem)
    	if hash_el not in self.urls_hash:
    		self.urls_hash.insert(0, elem)
    	else:
    		print('Такой url есть в базе')


    def remove_from_front(self):
        return self.urls_hash.pop()

    def remove_from_rear(self):
        return self.urls_hash.pop(0)

    def size_basic_stack(self):
        return len(self.urls_hash)



if __name__ == '__main__':
    HS_obj = Cash_list()
    print(HS_obj.is_empty())
    print(HS_obj.size_basic_stack())
    HS_obj.add_('https://geekbrains.ru')
    HS_obj.all()
    HS_obj.add_('https://geekbrains.ru')
    HS_obj.add_to_front('https://habr.com/ru/top/')
    HS_obj.all()
