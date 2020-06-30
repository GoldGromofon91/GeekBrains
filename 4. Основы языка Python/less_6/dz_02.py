class Road:
    def __init__(self, usr_len, usr_widt):
        self._len = usr_len
        self._wid = usr_widt
        self.__mass = 25
        self.__thickness = 5

    def create_road(self):
        mass = self._len * self._wid * self.__mass * self.__thickness
        return print(f'Для покрытия дорожного полотна, вам необходимо {int(mass / 1000)} тонн асфальта')


usr_len = int(input('Введите необходимое значение длины дороги: '))
usr_widt = int(input('Введите необходимое значение ширины дороги: '))

r = Road(usr_len, usr_widt)
r.create_road()
