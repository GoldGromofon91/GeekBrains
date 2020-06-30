from itertools import count, cycle

usr_srt = int(input('Введите начальное значение последовательности: '))
usr_fnh = int(input('Введите конечное значение последовательности: '))
count_list = []
cycle_list = []
check = 1
for num in count(usr_srt):
    if num > usr_fnh:
        break
    else:
        count_list.append(num)
# usr_list = [num for num in count(usr_srt) if num < usr_fnh]
print(f'Ваша последовательность:\n{count_list}')

for el in cycle(count_list):
    if check > len(count_list):
        break
    cycle_list.append(el)
    check += 1
print(f'Ваша 2-я последовательность:\n{cycle_list}')
