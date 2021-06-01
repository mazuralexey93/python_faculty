"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
with open('hw3.txt', 'r', encoding='utf-8') as my_file_hw3:
    line_counter = 0
    total_salary = 0
    for line in my_file_hw3.readlines():
        line_counter += 1
        person_list = line.split()
        total_salary += int(person_list[2])
        if int(person_list[2]) < 20000:
            print(person_list[1])
    awerage_salary = total_salary/line_counter
    print(f'awerage salary is {awerage_salary}')
