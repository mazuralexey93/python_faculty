"""
 Реализовать функцию my_func(),
  которая принимает три позиционных аргумента,
   и возвращает сумму наибольших двух аргументов.
"""

def my_func(a,b,c):
   result = sorted([a, b, c])
   return result[1] + result[2]

print('The sum of two large arguments =', my_func(32,-23,-3))
