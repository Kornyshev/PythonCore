class DynamicAttributes:
    def __getattr__(self, item):
        return f"{item} not found!"

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __delattr__(self, item):
        del self.__dict__[item]


# Using DynamicAttributes
d = DynamicAttributes()
d.x = 5
print(d.x)
print(d.y)  # Uses __getattr__
del d.x
print(d.x)  # Uses __getattr__
