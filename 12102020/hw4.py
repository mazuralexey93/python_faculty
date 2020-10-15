"""
4. Создать (не программно) текстовый файл со следующим содержимым:
...
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
  Новый блок строк должен записываться в новый текстовый файл.
"""
with open('hw4.txt', 'r', encoding='utf-8') as my_file_hw4:
    read_text = my_file_hw4.read()

with open('hw4_ru.txt', 'w', encoding='utf-8') as my_file_hw4:
    my_file_hw4.write(read_text.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре'))
