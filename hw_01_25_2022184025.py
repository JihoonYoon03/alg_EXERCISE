from random import randint as rint

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

points = [Point(rint(10, 99), rint(10, 99)) for _ in range(10)]