"""
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
  Об окончании ввода данных свидетельствует пустая строка.
"""
with open('hw1.txt', 'w') as my_file_hw1:
    while 1:
        content = input()
        my_file_hw1.write(content)
        if not content:
            break
