#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Trapezium(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def calculate_area(self):
        return (self.a + self.b) * self.h / 2

    def calculate_perimeter(self):
        # Для трапеции периметр сложнее определить, так как у нее разные стороны, поэтому этот метод может остаться абстрактным
        pass

def print_figure_info(figure):
    print("Area:", figure.calculate_area())
    print("Perimeter:", figure.calculate_perimeter())

if __name__ == '__main__':
    rectangle = Rectangle(5, 10)
    circle = Circle(7)
    trapezium = Trapezium(3, 5, 4)

    print("Rectangle:")
    print_figure_info(rectangle)

    print("Circle:")
    print_figure_info(circle)

    print("Trapezium:")
    print_figure_info(trapezium)