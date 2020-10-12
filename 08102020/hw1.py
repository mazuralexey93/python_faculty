"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

params = sys.argv
hours = 100
payment_per_hour = 100
award = 5000

if 'help' in params or 'h' in params:
    print('This programm counts wages.'
          ' If you want change payment_per_hour, run the script with param -p, default = 100 \n'
          'or if you want change award, run the script with param -a, default = 5000\n'
          'or change hours, with the -t, default = 200/n'
          'To perform a calculation for specific values, you must run a script with parameters.')
elif 'p' in params:
    payment_per_hour = int(input('enter payment per hour: '))
elif 'a' in params:
    award = int(input('enter award: '))
elif 't' in params:
    payment_per_hour = int(input('enter payment per hour: '))

total_sum = (payment_per_hour * hours) + award
print(f'Total sum is {total_sum}\n''For info run with param -h or -help')
