class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('%s \nЗАПУСК ОТРИСОВКИ...' % self.title)


class Pencil(Stationery):
    def draw(self):
        print('*' * 20 + f' Начата ОТРИСОВКА: {self.title}ом ' + '*' * 20)

class Pen(Stationery):
    def draw(self):
        print('-' * 20 + f' ПОВТОРНАЯ ОТРИСОВКА: {self.title} ' + '-' * 20)


class Handle(Stationery):
    def draw(self):
        print('=' * 20 + f' ОТРИСОВКА: {self.title}ом ' + '=' * 20)


st = Stationery('Канцелярские принадлежности')
st.draw()
pencil = Pencil('Карандаш')
pencil.draw()
pen = Pen('Синяя Ручка')
pen.draw()
handle = Handle('Маркер')
handle.draw()