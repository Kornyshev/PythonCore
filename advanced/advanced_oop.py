class Vehicle:
    """
    Base class for all types of vehicles.
    """
    base_sale_price = 0  # This should be overridden by subclasses

    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self._miles = 0  # Protected attribute, not meant to be accessed directly outside the class

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def drive(self, miles):
        self._miles += miles
        return f"Driven {miles} miles."

    @classmethod
    def is_motorcycle(cls):
        return False

    @staticmethod
    def check_mileage(miles):
        return True if miles > 0 else False

    @property
    def miles(self):
        return self._miles

    @miles.setter
    def miles(self, value):
        if Vehicle.check_mileage(value):
            self._miles = value
        else:
            raise ValueError("Mileage must be positive")

    def sale_price(self):
        """Return the sale price for this vehicle as a new vehicle."""
        if self.base_sale_price == 0:
            raise NotImplementedError("Derived classes must override base_sale_price.")
        return self.base_sale_price - (0.1 * self.miles)


class Car(Vehicle):
    base_sale_price = 20000

    def drive(self, miles):
        super().drive(miles)
        return f"Car has been driven for {miles} miles."

    @classmethod
    def is_motorcycle(cls):
        return False


class Motorcycle(Vehicle):
    base_sale_price = 5000

    def drive(self, miles):
        super().drive(miles)
        return f"Motorcycle zooms for {miles} miles!"

    @classmethod
    def is_motorcycle(cls):
        return True


def main():
    car = Car("Toyota", "Corolla", 2021, 1500)
    print(car)
    print(car.drive(100))
    print(f"Sale Price: ${car.sale_price():,.2f}")

    bike = Motorcycle("Harley", "Chopper", 2019, 300)
    print(bike)
    print(bike.drive(200))
    print(f"Sale Price: ${bike.sale_price():,.2f}")
    print(f"Is Motorcycle: {bike.is_motorcycle()}")


if __name__ == "__main__":
    main()
