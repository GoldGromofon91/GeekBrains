# задание1
def register(word):
    return word.capitalize()


usr_word = input('Введите любое слово: ')
print(f'Ваше слово: {register(usr_word)}')


# задание 2
def register_1(word):
    my_string = ' '.join(word)
    return my_string.title()


usr_word = input('Введите несколько слов: ').split()
print(f'Ваше слово: {register_1(usr_word)}')
