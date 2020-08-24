from collections import Counter, deque


def create_Btree(usr_string):
	#Вычисляем чистоту, затем Создаем список(очередь) , значениями которого является элементы словаря отсортированные не по ключу а по значению
	frequency = Counter(usr_string)
	deq_elem_obj = deque(sorted(frequency.items(), key=lambda el:el[1]))
	# print(deq_elem_obj)
	# Если в  deq_elem_obj 1 элемент(кортеж) считаем вес, создаем словарь, и перезаписываем deq_elem_obj
	if len(deq_elem_obj) == 1:
		weight_new_node = deq_elem_obj[0][1]
		new_node={0:deq_elem_obj.popleft()[0],1:None}
		# print(new_node)
		deq_elem_obj.append((new_node,weight_new_node))
		# print(deq_elem_obj)
	else:
		#если элементов больше 1-го суммируем их частоты и создаем новый узел, и размещаем его в deq_elem_obj в соответсвии с новой частотой узла 
		while len(deq_elem_obj) > 1:
			weight_new_node = deq_elem_obj[0][1] + deq_elem_obj[1][1]
			new_node ={0: deq_elem_obj.popleft()[0],1:deq_elem_obj.popleft()[0]}
			#размещаем новый узел в соответсвии с частотой
			for n, elem in enumerate(deq_elem_obj):
				# print(elem, elem[1])
				if weight_new_node > elem[1]:
					continue
				else:
					deq_elem_obj.insert(n,(new_node,weight_new_node))
					# print('after insert', deq_elem_obj)
					break
			else:
				#если вес нового узла из deq_elem_obj больше веса всех элементов в deq_elem_obj то после перебора добавляем этот новый узел в конец очереди
				deq_elem_obj.append((new_node,weight_new_node))

	return deq_elem_obj[0][0]


def create_bvalue(us_tree, path=''):
 	# Базовый случай: Если не словарь, создаем словарь где ключ принимает значение соответсвующее ветви 0 или 1
    if not isinstance(us_tree, dict):
        code_table[us_tree] = path
    else:
        create_bvalue(us_tree[0], path=f'{path}0')
        create_bvalue(us_tree[1], path=f'{path}1')


def view_coding_str(dict_value):
	for el in dict_value.values():
		print(el, end=' ')


def haffman_coding_start():
	print('*'*50+' Кодирование в стиле Хаффмана '+'*'*50)
	usr_str = "abc abc qwe qcd dd 676 kjhkjh h h hgfghf"#input('Введите строку:')
	print(f'Ваша строка: {usr_str}')
	tree = create_Btree(usr_str)
	create_bvalue(tree)
	print('Ваша строка кодированная методом Хаффмана:')
	view_coding_str(code_table)




if __name__ == "__main__":
	code_table = dict()

	haffman_coding_start()


