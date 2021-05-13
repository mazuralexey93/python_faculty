from random import randint


def generate_numbers():
    count = 90
    minimum = 1
    maximum = 90
    my_l = []
    while len(my_l) < count:
        new = randint(minimum, maximum)
        if new not in my_l:
            my_l.append(new)
    return my_l


class LotoCard:
    data = None
    empty = 0
    intersection = -1

    def __init__(self):
        self.data = []
        numbers = generate_numbers()

        for i in range(3):
            sorted_fifteen = sorted(numbers[5 * i:5 * (i + 1)])
            for j in range(4):
                index_el = randint(0, len(sorted_fifteen))
                sorted_fifteen.insert(index_el, self.empty)
            self.data += sorted_fifteen

    def __str__(self):
        separator = '**************************'
        result = separator + '\n'

        for index_el, number in enumerate(self.data):
            if number == self.empty:
                result += '  '
            elif number == self.intersection:
                result += ' -'
            elif number < 10:
                result += f' {str(number)}'
            else:
                result += str(number)

            if (index_el + 1) % 9 == 0:
                result += '\n'
            else:
                result += ' '

        return result + separator

    def intersecting_number(self, number):
        for index_el, item in enumerate(self.data):
            if item == number:
                self.data[index_el] = self.intersection
                return

    def __contains__(self, item):
        return item in self.data

    def closed_card(self) -> bool:
        return set(self.data) == {self.empty, self.intersection}


class Game:
    def __init__(self):
        self.player_card = LotoCard()
        self.computer = LotoCard()
        self.barrels = generate_numbers()

    def start(self):
        while True:
            barrel = self.barrels.pop()

            print(f'New barrel: {barrel} (remains {len(self.barrels)})')
            print(f'********* Player *********\n{self.player_card}')
            print(f'******** Computer ********\n{self.computer}')

            answer = input('Is this number in your card? (y/n): ').lower().strip()

            if answer == 'y' and not barrel in self.player_card or answer != 'y' and barrel in self.player_card:
                print('Yo! You lose! ')
                break

            if barrel in self.player_card:
                self.player_card.intersecting_number(barrel)
                if self.player_card.closed_card():
                    print('Congratulations! You win')
                    break

            if barrel in self.computer:
                self.computer.intersecting_number(barrel)
                if self.computer.closed_card():
                    print('\n''Yo! You lose!')
                    break


game = Game()
game.start()

# print(player)
# print(computer)
