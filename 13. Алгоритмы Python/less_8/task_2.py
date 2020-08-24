"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BinaryTree:
    def __init__(self, root_obj):
        try:
            self.root = int(root_obj)
        except ValueError:
            print('Некорректное значение для root-а')
        self.left_child = None
        self.right_child = None

    
    def insert_left(self, new_node):
        try:
            new_node = int(new_node)
        except (ValueError,TypeError,SyntaxError):
            print('Error! Некорректное значение для потомка!')
            return f' Текущее значение {self.left_child}'
        if new_node >= self.root:
            print('Ваше значение не подходит для левого потомка.')
        else:
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            new_node = int(new_node)
        except (ValueError,TypeError,SyntaxError):
            print('Error! Некорректное значение для потомка!')
            return f' Текущее значение {self.left_child}'
        if new_node <= self.root:
            print('Ваше значение не подходит для правого потомка.')
        else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(10)

print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(20)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
