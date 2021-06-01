"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
  Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
 для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
 Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.

"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size  # for suit size is the height, for coat size is the size of clothes

    @abstractmethod
    def calculating_fabric_costs(self):
        pass


class Suit(Clothes):
    @property
    def calculating_fabric_costs(self):
        return f"On this suit {self.size} height requires {round(self.size * 2 + 0.3, 2)} square metres of material"


class Coat(Clothes):
    @property
    def calculating_fabric_costs(self):
        return f"On this coat {self.size}'s size requires {round(self.size / 6 + 0.3, 2)} square metres of material"


suit1 = Suit(1.73)
coat1 = Coat(52)
print(suit1.calculating_fabric_costs)
print(coat1.calculating_fabric_costs)
