"""
 Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
 Итоговый список сохранить в виде json-объекта в соответствующий файл.
  Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json
with open('hw7.txt', 'r', encoding='utf-8') as my_file_hw7:
    content = my_file_hw7.readlines()

lines = []
my_dict = {}
profits = []

for i in content:
    lines.append(i.strip().split())

for el in lines:
    profit = int(el[2]) - int(el[3])
    my_dict[el[0]] = profit
    if profit > 0:
        profits.append(profit)

average_profit = round(sum(profits) / len(profits))
result_list = [my_dict, {'average_profit': average_profit}]
print(result_list)

with open ('hw7.json', 'w', encoding='utf-8') as my_file_hw7:
    json.dump(result_list, my_file_hw7)
