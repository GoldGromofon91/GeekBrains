import random
numbers = [random.randint(-10,100) for i in range(20)]
print(numbers)
res_numb = [number for number in numbers if number %3 == 0 and number > 0 and number %4 != 0]
print(res_numb)