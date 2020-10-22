"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
 класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
 первый элемент первой строки первой матрицы складываем с
  первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, elements_of_matrix):
        self.elements_of_matrix = elements_of_matrix  # list of lists

    def __str__(self):  # displayed matrices
        for row in self.elements_of_matrix:
            for el in row:
                print(el, end='  ')
            print()
        return ''

    def __add__(self, other):  # compare and sum of matrices
        if len(self.elements_of_matrix) == len(other.elements_of_matrix):
            for i, row in enumerate(self.elements_of_matrix):
                if len(row) == len(other.elements_of_matrix[i]):
                    for j, el in enumerate(row):
                        self.elements_of_matrix[i][j] += other.elements_of_matrix[i][j]
                else:
                    return f'Rows should be the same numbers of elements'
        else:
            return f'Matrices should be the same number of rows'
        # return str(Matrix(self.elements_of_matrix))
        return Matrix(self.elements_of_matrix)


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# A = Matrix([[1, 2], [4, 5, 6], [7, 8, 9]])
# A = Matrix([[1, 2, 3], [4, 5, 6]])
B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(A)
print(B)
print(A + B)
