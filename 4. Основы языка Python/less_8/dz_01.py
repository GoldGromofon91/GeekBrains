class Data:
    def __init__(self, str):
        self.string = str

    @classmethod
    def data_numb(cls, usr_str):
        usr_numb = list(map(int, usr_str.split('-')))
        for i in usr_numb:
            print(f'Теперь у {i} - тип {type(i)}')

    @staticmethod
    def data_val(usr_str):
        usr_numb = list(map(int, usr_str.split('-')))
        if 1 <= usr_numb[0] <= 31 and 1 <= usr_numb[1] <= 12 and len(str(usr_numb[2])) == 4:
            for el in usr_numb:
                print(f'У {el} - {type(el)}')
        else:
            print('Вы ввели неккоректно дату')


usr_date = input('Введите число в формате "ДД-ММ-ГГГГ": ')
Data.data_numb(usr_date)
Data.data_val(usr_date)
