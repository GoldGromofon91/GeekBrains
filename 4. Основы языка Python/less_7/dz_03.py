class Organic_cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        summa = self.cell + other.cell
        return summa

    def __sub__(self, other):
        if self.cell > other.cell:
            sub_cell = self.cell - other.cell
            return sub_cell
        else:
            return 'Число меньше 0'

    def __mul__(self, other):
        mul_cell = self.cell * other.cell
        return mul_cell

    def __truediv__(self, other):
        try:
            div = self.cell / other.cell
        except ZeroDivisionError:
            return 'Деление на 0'
        else:
            return round(div, 2)

    def make_order(self, nsr):
        return (nsr * "*" + '\n') * round(self.cell / nsr)


c_1 = Organic_cell(30)
print(c_1.cell)
c_2 = Organic_cell(15)
print(c_2.cell)
sum_cell = c_1 + c_2
print(sum_cell)
sub = c_1 - c_2
print(sub)
mul = c_1 * c_2
print(mul)
div = c_1 / c_2
print(div)
c_3 = Organic_cell(15)
print(c_3.make_order(4))
