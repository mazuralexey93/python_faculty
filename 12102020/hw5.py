"""
5. Создать (программно) текстовый файл,
 записать в него программно набор чисел, разделенных пробелами.
  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('hw5.txt', 'w') as my_file_hw5:
    try:
        numbers = input('Enter the numbers separated by space: ')
        list_numbers = numbers.split()
        my_file_hw5.write(numbers)
        print(f'Sum of numbers:', sum(map(int, list_numbers)))
    except:
        print('ValueError: ', 'Enter  numbers, not string')
