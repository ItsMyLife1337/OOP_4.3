#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Car:
    def __init__(self, brand, cylinders, power):
        self.brand = brand
        self.cylinders = cylinders
        self.power = power

    def rebrand(self, new_brand):
        self.brand = new_brand

    def change_power(self, new_power):
        self.power = new_power

    def display_info(self):
        print(f"Brand: {self.brand}, Cylinders: {self.cylinders}, Power: {self.power} hp")


class Lorry(Car):
    def __init__(self, brand, cylinders, power, capacity):
        super().__init__(brand, cylinders, power)
        self.capacity = capacity

    def rebrand(self, new_brand):
        self.brand = new_brand

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity

    def display_info(self):
        print(f"Brand: {self.brand}, Cylinders: {self.cylinders}, Power: {self.power} hp, Capacity: {self.capacity} tons")


if __name__ == '__main__':
    car1 = Car("Toyota", 4, 200)
    car1.display_info()
    car1.rebrand("Honda")
    car1.change_power(250)
    car1.display_info()

    lorry1 = Lorry("Volvo", 6, 350, 10)
    lorry1.display_info()
    lorry1.rebrand("MAN")
    lorry1.change_capacity(15)
    lorry1.display_info()