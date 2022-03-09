"""Write the function circleArea/CircleArea which takes in a Circle object and calculates the area of that circle."""

from math import pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, Point, radius):
        self.x = Point.x
        self.y = Point.y
        self.radius = radius


def circle_area(circle):
    return round(pi * circle.radius**2, 6)


print(circle_area(Circle(Point(10, 10), 30)))
