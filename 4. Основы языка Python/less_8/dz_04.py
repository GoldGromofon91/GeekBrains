class WareHouse:
    def __init__(self, size):
        self.size = size
        self.wh_dict = {}

    def __add__(self, other):
        if self.size > 0:
            self.size -= other.subject_size
        else:
            print('Склад переполнен')

    def __sub__(self, other):
        if self.size > 0:
            self.size += other.subject_size
        else:
            print('На складе нет оборудования')

    def acceptance(self, other, count):
        if isinstance(count, int):
            value = {other.subject: count}
            self.wh_dict.update(value)
        else:
            print('Количество укажите числом')


class OfficeEquip:
    def __init__(self, subject, size):
        self.subject = subject
        self.subject_size = size


class Printer(OfficeEquip):
    def __init__(self, subject, size):
        super().__init__(subject, size)
        # self.printer_color = color


class Scanner(OfficeEquip):
    def __init__(self, subject, size):
        super().__init__(subject, size)
        # self.scanner_color = color


class Xerox(OfficeEquip):
    def __init__(self, subject, size):
        super().__init__(subject, size)
        # self.xerox_color = color


wh = WareHouse(100)
p_1 = Printer('Принтер', 20)
X_1 = Xerox('Xerox', 5)
print(wh + p_1)
print(wh - X_1)
print(wh.size)
wh.acceptance(p_1, 10)
wh.acceptance(X_1, 'ten')
