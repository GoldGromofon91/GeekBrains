class MyError(Exception):
    def __str__(self):
        return 'Вы ввели не число'


result = []
numb = []
running = True
while running:
    usr_data = input('Введите любое число. Для выхода введите "stop": ')
    if usr_data == 'stop':
        running = False
        break
    try:
        if not usr_data.isdigit():
            raise MyError()
    except MyError as err:
        print(err)
    else:
        numb.append(usr_data)
        print(numb)
        result = list(map(int, numb))
print(result)
