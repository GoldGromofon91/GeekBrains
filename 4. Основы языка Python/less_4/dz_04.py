# Согласно задания
numbers = [1, 1, 2, 3, 3, 5, 4, 4, 6, 7, 10, 9, 8, 8]
print(f'Исходный список чисел:\n{numbers}')
res_numb = [num for num in numbers if numbers.count(num) == 1]
print(f'Список из уникальных чисел:\n{res_numb}')

# С использованием случайных чисел
import random

print('*' * 20 + ' Результат со случайными числами ' + '*' * 20)
numbers = [random.randint(1, 10) for i in range(20)]
print(f'Исходный список чисел:\n{numbers}')
res_numb = [num for num in numbers if numbers.count(num) == 1]
print(f'Список из уникальных чисел:\n{res_numb}')
