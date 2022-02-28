"""Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.
Write a function calculating circumference of a Circle.
Tests round answers to 6 decimal places."""


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


def circle_circumference(circle):
    return round(2 * circle.radius * pi, 6)


print(circle_circumference(Circle(Point(25, -70), 30)))
