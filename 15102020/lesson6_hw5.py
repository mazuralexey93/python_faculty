"""
. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
  В каждом из классов реализовать переопределение метода draw.
  Для каждого из классов методы должен выводить уникальное сообщение.
   Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return ('Starting draw')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'{self.title} starting draw, use it wisely')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'delicate {self.title} starting draw')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f"{self.title}'s turn")

something = Stationery('something')
print(something.draw())
pen = Pen('blue pen')
print(pen.draw())
pencil = Pencil('graphite pencil')
print(pencil.draw())
handle = Handle('Mr. Black Handle')
print(handle.draw())
