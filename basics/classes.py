from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing a generic animal.
    All animals in the zoo must derive from this class and implement its methods.
    """

    def __init__(self, name):
        self._name = name  # Encapsulated attribute

    @abstractmethod
    def make_sound(self):
        """
        Produce the sound specific to the animal.
        """
        pass

    def describe(self):
        """
        Describes the animal.
        """
        print(f"I am a {self.__class__.__name__} named {self._name}.")


class Bird(Animal):
    """
    A concrete class representing birds.
    """

    def make_sound(self):
        print(f"{self._name} says tweet")


class Mammal(Animal):
    """
    A concrete class representing mammals.
    """

    def make_sound(self):
        print(f"{self._name} says grunt")


class Fish(Animal):
    """
    A concrete class representing fish.
    """

    def make_sound(self):
        print(f"{self._name} is silent because fish don't make sounds")


class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird demonstrating multiple inheritance.
    """

    def make_sound(self):
        print(f"{self._name} says splash and tweet")


def main():
    animals = [
        Bird("Sparrow"),
        Mammal("Elephant"),
        Fish("Goldfish"),
        FlyingFish("Magicarp")
    ]

    for animal in animals:
        animal.describe()
        animal.make_sound()


if __name__ == "__main__":
    main()
