"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
 Сформировать итоговый массив чисел, соответствующих требованию.
  Элементы вывести в порядке их следования в исходном списке.
   Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
import random
some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [num for num, i in zip(some_list, some_list[:]) if some_list.count(i) == 1]

random_list = [random.randint(1, 100) for i in range(15)]
new_list2 = [num for num, i in zip(random_list, random_list[:]) if random_list.count(i) == 1]

print(f'{some_list} --> {new_list},\n{random_list} --> {new_list2}')
