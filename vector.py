import math
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.vector = [self.x, self.y]

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __getitem__(self, item):
        return self.vector[item]

    def get_angle(self):
        if self.x == 0:
            return 0

        else:
            return math.atan(self.y / self.x)