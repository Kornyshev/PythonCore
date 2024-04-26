class Number:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return Number(-self.value)

    def __pos__(self):
        return Number(+self.value)

    def __abs__(self):
        return Number(abs(self.value))

    def __str__(self):
        return str(self.value)


# Using the Number class
n = Number(-5)
print(-n)  # Uses __neg__
print(+n)  # Uses __pos__
print(abs(n))  # Uses __abs__
