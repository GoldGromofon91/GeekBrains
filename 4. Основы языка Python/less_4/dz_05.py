from functools import reduce

some_list = [num for num in range(100, 1001, 1) if num % 2 == 0]
print(f'Cумма чисел равна: {reduce(lambda x, y: x + y, some_list)}')
