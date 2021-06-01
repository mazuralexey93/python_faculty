#Поработайте с переменными, создайте несколько, выведите на экран,
#запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.


number = 12
message = 'SOS'
result = 2 + 2

print(number)
print(message)
print(result)

user_input_number1 = int(input('Введите 1e число: '))
user_input_number2 = int(input('Введите 2e число: '))
user_input_text = input('Введите текст: ')

print('1e число: ', user_input_number1)
print('2e число: ', user_input_number2)
print('Вы ввели: ', (user_input_text))
