import time, random


class Car:
    def __init__(self, color, name, speed, is_police=None):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def car_go(self):
        print('Двигатель запущен! Пристегнитесь!')

    def car_stop(self):
        self.speed = 0
        print('Двигатель заглушен! ')
        print(f'Текущая скорость {self.speed}')

    def car_direction(self):
        direct = ['Прямо', 'На лево', 'На право']
        count = 0
        while count < 3:
            for i in range(random.randint(0, 2), len(direct)):
                side = direct[i]
                time.sleep(3)
                count += 1
                print(f'{self.color} {self.name} едет {side}')

    def car_speed(self):
        while self.speed < 80:
            time.sleep(2)
            self.speed += 10
            print(f'{self.color} {self.name} едет со скоростью: {self.speed}')
        return print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def car_speed(self):
        while self.speed < 80:
            if self.speed >= 60:
                print('Не превышайте скорость')
                break
            else:
                time.sleep(2)
                self.speed += 10
            print(f'{self.color} {self.name} едет со скоростью: {self.speed}')
        return print(f'Текущая скорость {self.speed}')


class WorkCar(Car):
    def car_speed(self):
        while self.speed < 80:
            if self.speed >= 40:
                print('Не превышайте скорость на рабочей машине')
                break
            else:
                time.sleep(2)
                self.speed += 10
            print(f'{self.color} {self.name} едет со скоростью: {self.speed}')
        return print(f'Текущая скорость {self.speed}')


class SpeedCar(Car):
    def car_speed(self):
        while self.speed <= 200:
            if self.speed == 100:
                print('Держитесь крепче! текущая скорость %d' % self.speed)
            time.sleep(0.5)
            self.speed += 20
            print(f'{self.color} {self.name} едет со скоростью: {self.speed}')
        return print(f'Текущая скорость {self.speed}')


class PoliceCar(Car):
    pass


car = Car('Green', 'Lexus', 30)
car.car_go()
car.car_direction()
car.car_speed()
# print(car.speed)
car.car_stop()
# print(car.speed)
t_car = TownCar('White', 'Hyndai', 10)
t_car.car_go()
t_car.car_speed()
t_car.car_direction()
t_car.car_stop()
# print(t_car.speed)
w_car = WorkCar('ЧЕРНАЯ','ГАЗЕЛЬ',5)
w_car.car_go()
w_car.car_direction()
w_car.car_speed()
w_car.car_stop()
p_car = PoliceCar('Black', 'Ford', 30, True)
p_car.car_go()
p_car.car_speed()
p_car.car_stop()
s_car = SpeedCar('Red','Lamborgini',60)
s_car.car_speed()