class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        full_name = self.surname + " " + self.name
        # print(f'Здравствуйте {self.surname} {self.name}')
        return full_name

    def get_total_income(self):
        total = 0
        for val in self._income.values():
            total = total + val
        return total


person1 = Position('Iva', 'Ivanov', 'Зам.Начальника', {'оклад': 2000, 'премия': 2000})
print(person1.get_full_name())
print(person1.get_total_income())
person2 = Position('Eva', 'Avramova', 'Попс', {'оклад': 50000, 'премия': 10000})
print(person2.get_full_name())
print(person2.get_total_income())

