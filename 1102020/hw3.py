"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
request = int(input('Type the number of month (1 - 12): '))

my_list = ['winter', 'spring', 'summer', 'autumn']
if request == 12 or request < 3: # зима
    print(my_list[0])
elif request == 3 or request < 6: # весна
    print(my_list[1])
elif request == 7 or request < 9: # лето
    print(my_list[2])
else:
    print(my_list[3]) # else

# решение через list

my_dict = {'winter': [12, 1, 2],
           'spring' : [3, 4, 5],
           'summer': [6, 7, 8],
           'autumn' : [9, 10, 11]}

request = int(input('Type the number of month (1 - 12) : '))

for key in my_dict.keys():
    if request in my_dict[key]:
        print(key)

# решение через dict






