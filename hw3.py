#. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


# number = int(input('Введите число n,чтобы найти сумму чисел n + nn + nnn: ' ))
# result = number + (number * 10 + number) + (number * 100 + number * 10 + number)
# print(result)


## реализация через цикл for

# n = int(input('Введите число n,чтобы найти сумму чисел n + nn + nnn: ' ))
# number = n
# result = 0
# # меняя range есть возможность масштабировать n + nn + nnn + nnnn и т.д
# for i in range(3):
#    result += number
#    number = number * 10 + n
# print(result)

## корректно для целых чисел от -10 до 10

n = input('Введите число n,чтобы найти сумму чисел n + nn + nnn: ')
print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')

# метод конкатинации n, с переводом из типа str в int
# корректно для целых положительных чисел



