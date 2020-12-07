class Car:
    numberOfWheels=4
    _color = "Black"
    __yearOfManafuator =2017

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color", self._color)


car =Car()
print("Public attribute numberOfWheels", car.numberOfWheels)
bmw=Bmw()
""" This is not the way to deal with private"""
#print("Private attribute yearOfManafuator",car.__yearOfManafuator)
print("Private attribute yearOfManafuator",car._Car__yearOfManafuator)
