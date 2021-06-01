"""
2. Для списка реализовать обмен значений соседних элементов,
 т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""
#
my_list = []
i = 0
index = 0
num_of_el = int(input('How much elements will contain the list?: '))

while i < num_of_el:
    my_list.append(input('Write an element: '))
    i += 1
for element in range(int((len(my_list))/2)):
    my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    index += 2
print(my_list)



