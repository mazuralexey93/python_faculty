"""
 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
  При нажатии Enter должна выводиться сумма чисел.
   Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
     Но если вместо числа вводится специальный символ, выполнение программы завершается.
      Если специальный символ введен после нескольких чисел,
      то вначале нужно добавить сумму этих чисел к полученной ранее сумме
       и после этого завершить программу.

"""
def my_sum():
    result = 0
    flag = True
    while flag == 1:
        user_input = input('>>> ').split()
        current_result = 0

        for s in range(len(user_input)):
            if user_input[s] == 'Q' or user_input[s] == 'q':
                flag = -1
                break
            else:
                current_result = current_result + int(user_input[s])
        result = result + current_result
        print('Current result is ', current_result)
    print('Total sum is', result)

my_sum()
