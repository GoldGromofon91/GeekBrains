import random,math

numbers = [random.randint(-10,10) for i in range(10)]
print(numbers)
result=[]
def change_numb(array):
    for numb in array:
        res_numb = numb if numb < 0 else math.pow(math.sqrt(numb),2)
        result.append(res_numb)
    return result
print(change_numb(numbers))