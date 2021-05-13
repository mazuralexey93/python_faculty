import random
from random import randint

fifteen_numbers = random.sample(range(1, 91), 15)


class LotoCard:

    def __init__(self, name):
        self.data = []
        self.name = name
        for i in range(3):
            sorted_fifteen = sorted(fifteen_numbers[5 * i:5 * (i + 1)])
            for j in range(4):
                index = randint(0, len(sorted_fifteen))
                sorted_fifteen.insert(index, 0)
            self.data += sorted_fifteen

    def __str__(self):
        separator = '**************************'
        result = separator + '\n'

        for index_el, num in enumerate(self.data):
            if num == 0:
                result += '  '
            elif num < 10:
                result += f' {str(num)}'
            else:
                result += str(num)

            if (index_el + 1) % 9 == 0:
                result += '\n'
            else:
                result += ' '
        return result + separator


player = LotoCard('Player')

print(player)
