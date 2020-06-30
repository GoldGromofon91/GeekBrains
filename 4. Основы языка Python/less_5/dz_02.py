with open('dz_02.txt', 'r') as f:
    lines = 0
    words = 0
    el = 0
    for line in f:
        lines += 1
        words += len(line.split())
print('Файл прочитан!' + '\n' + f'В файле {lines} строк(и), {words} слов!')
