"""
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
x = int(input('enter divisor: '))
y = int(input('enter denominator: '))
def division(x,y):
    """
    :param x: divider
    :param y: denominator
    :return: division result
    """
    try:
        return x / y
    except ZeroDivisionError:
        return 'Divizion by zero, change the denominator'
    except ValueError:
        return 'Enter only the numbers'

print(division(x,y))
print(division(175,15))
