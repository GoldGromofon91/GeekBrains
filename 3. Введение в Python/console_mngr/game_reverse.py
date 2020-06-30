import random

def game_reverse():
    min_number = 1
    max_number = 100
    right_answer = None
    while right_answer != '=':
        number = random.randint(min_number, max_number)
        print(f'Вы загодали число {number}?')
        usr_answer = input(
            'Введите "=" - если я угадал, ">" - если загаданное вами число больше, "<" - если загаданное вами число '
            'меньше ')
        if usr_answer == '>':
            min_number = number + 1
        elif usr_answer == '<':
            max_number = number - 1
        else:
            break
    print('Я молодец, я угадал!')


if __name__ == '__main__':
    game_reverse()
