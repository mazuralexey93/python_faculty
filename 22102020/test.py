#
from random import randint
import random
barrels = random.sample(range(1, 91), 90)
print(barrels.pop())


# def generate_numbers():
#     count = 90
#     minimum = 1
#     maximum = 90
#     my_l = []
#     while len(my_l) < count:
#         new = randint(minimum, maximum)
#         if new not in my_l:
#             my_l.append(new)
#     return my_l
#
# barrels = generate_numbers()
# print(barrels)