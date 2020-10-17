# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __int__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f' Current speed is {self.speed}'

    def go(self):
        return ("Engine's sound")

    def stop(self):
        return ("Engine's sound is over")

    def turning(self, direction):
        return f' car is turning {direction}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Limit speed is 60, Current speed is {self.speed}, drive slowly'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 40:
            return(f'Limit speed is 40, Current speed is {self.speed}, drive slowly')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)

    def go(self):
        super().go()
        return ("Sweet engine's sound!")

    def turning(self, direction):
        super().turning(direction)
        return (f' car is drifting {direction}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)


    def go(self):
        return ("Siren's sound")

car1 = TownCar(70, 'gray' ,'volvo', False)
print(car1.color, car1.name, car1.go(), car1.turning('left'), car1.show_speed(), car1.stop())

car2 = SportCar(120, 'red', 'Porshe', False)
print(car2.color, car2.name, car2.go(), car2.turning('around'), car2.show_speed())


car3 = PoliceCar(20, 'black-white', 'Cadillac', True)
print(car3.color, car3.name, car3.go(), car3.stop(), car3.is_police)

car4 = WorkCar(140, 'cyan-blue', 'lada2104', False)
print(car4.go(), car4.color, car4.name, car4.show_speed(), car4.stop())
