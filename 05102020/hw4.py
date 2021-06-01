"""
Программа принимает действительное положительное число x и целое отрицательное число y.
 Необходимо выполнить возведение числа x в степень y.
  Задание необходимо реализовать в виде функции my_func(x, y).
  При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
 Первый — возведение в степень с помощью оператора **.+
  Второй — более сложная реализация без оператора **, предусматривающая использование цикла.+
"""

def my_func():
    """returns the result of raising to a negative power"""
    global x , y
    x = float(input('enter float: '))
    y = int(input('enter negative integer: '))
    return x**y

def my_func_2():
    global x, y
    result = 1
    x = float(input('enter float: '))
    y = int(input('enter negative integer: '))
    for i in range(abs(y)):
        result *= x
    return  1 / result

print(my_func())
print(my_func_2())
