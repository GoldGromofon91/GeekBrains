f = open('dz_01.txt', 'w')
run = True
while run:
    usr_word = input("Введите символы: ")
    if usr_word == '':
        run = False
    else:
        f.write(usr_word + '\n')
print('Файл записан!')
f.close()
