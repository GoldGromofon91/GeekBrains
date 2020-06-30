from abc import abstractmethod


class Clother:
    def __init__(self, size, height):
        self.coat_size = size
        self.costume_height = height

    @property
    def sum_cloth(self):
        cloth = (self.coat_size / 6.6 + 0.5) + (2 * (self.costume_height/100) + 0.3)
        return f'Необходимое количество ткани: {round(cloth, 2)} м'

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clother):
    def cloth(self):
        coat = self.coat_size / 6.6 + 0.5
        print(f'Для создания пальто {self.coat_size} - размера, необходимо {round(coat,2)} м')


class Costume(Clother):
    def cloth(self):
        costume = 2 * (self.costume_height/100) + 0.3
        print(f'Для создания костюма для роста {self.costume_height} см, необходимо {round(costume,2)}')


usr_size = int(input('Для подсчета количества ткани для ПАЛЬТО, введите размер: '))
usr_height = int(input('Для подсчета количества ткани для КОСТЮМА введите рост: '))
cloth = Clother(usr_size, usr_height)
print(cloth.sum_cloth)
coat = Coat(usr_size,usr_height)
coat.cloth()
costume = Costume(usr_size,usr_height)
costume.cloth()