class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"


# Using the Vector class
v1 = Vector(2, 4)
v2 = Vector(1, -1)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 3
print(v3)  # Uses __add__
print(v4)  # Uses __sub__
print(v5)  # Uses __mul__
