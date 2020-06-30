evens_list = [num for num in range(20, 241, 1) if num % 20 == 0]
odds_list = [num for num in range(20, 240, 1) if num % 21 == 0]
print(f'Список чисел кратный 20:\n{evens_list}')
print(f'Список чисел кратный 21:\n{odds_list}')
