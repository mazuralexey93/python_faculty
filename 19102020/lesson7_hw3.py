"""
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
 Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
 Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:

    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return f'Combining of two cells: {self.number_of_cells + other.number_of_cells}'

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells > 0:
            return f'Subtraction of two cells: {self.number_of_cells - other.number_of_cells}'
        else:
            return 'Subtraction of two cells should more than zero'

    def __mul__(self, other):
        return f'Multiplication of two cells: {self.number_of_cells * other.number_of_cells}'

    def __truediv__(self, other):
        return f'Division of two cells: {self.number_of_cells // other.number_of_cells}'

    def make_order(self, cells_in_row):

        order = ''
        numbers_of_row = self.number_of_cells // cells_in_row
        order += f"{'*' * cells_in_row}\n" * numbers_of_row
        order += f"{'*' * (self.number_of_cells - cells_in_row * numbers_of_row)}"
        print(order)

a = Cell(22)
b = Cell(15)
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b)
print(f" {'_' * 25} order of Cell 'a' {'_' * 25}")
a.make_order(6)
print(f" {'_' * 25} order of Cell 'b' {'_' * 25}")
b.make_order(4)
