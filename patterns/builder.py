class Meal:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ', '.join(self.parts)


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_main(self, main):
        self.meal.add_part(f"Main: {main}")
        return self

    def add_side(self, side):
        self.meal.add_part(f"Side: {side}")
        return self

    def add_drink(self, drink):
        self.meal.add_part(f"Drink: {drink}")
        return self

    def add_dessert(self, dessert):
        self.meal.add_part(f"Dessert: {dessert}")
        return self

    def build(self):
        return self.meal


def main():
    # Creating a meal with various components using the builder
    meal = (MealBuilder()
            .add_main("Steak")
            .add_side("Caesar Salad")
            .add_drink("Red Wine")
            .add_dessert("Cheesecake")
            .build())

    print("Meal Components:")
    print(meal.list_parts())


if __name__ == "__main__":
    main()
