class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __bytes__(self):
        return bytes(f"{self.name}:{self.age}", "utf-8")

    def __format__(self, format_spec):
        if format_spec == 'name':
            return str(self.name)
        return str(self)


# Creating and using the Person class
p = Person("John", 30)
print(repr(p))  # Uses __repr__
print(p)  # Uses __str__
print(bytes(p))  # Uses __bytes__
print(format(p, "name"))  # Uses __format__
