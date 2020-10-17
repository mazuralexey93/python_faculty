"""
. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
 Значения данных атрибутов должны передаваться при создании экземпляра класса.
  Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
   необходимого для покрытия всего дорожного полотна.
   Использовать формулу: длина * ширина * масса асфальта
    для покрытия одного кв метра дороги асфальтом,
     толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self._width = width  # in meters
        self._length = length  # in meters

    def calculating_mass(self, length, width):
        mass_for_1sq_m = 50000  # mass of asphalt for covering one square meter of road with asphalt in grams
        depth = 0.10  # depth of asphalt in meters
        result = length * width * mass_for_1sq_m * depth
        print(f'resulting mass is {result ** 1 / 1000000} tons')


M34 = Road(3000, 10)
M34.calculating_mass(3000, 10)
M34.calculating_mass(1000, 20)
