class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price


# Comparing products
prod1 = Product("Apple", 1)
prod2 = Product("Banana", 2)
print(prod1 == prod2)  # Uses __eq__
print(prod1 < prod2)  # Uses __lt__
print(prod1 <= prod2)  # Uses __le__
