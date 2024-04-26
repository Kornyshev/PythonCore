import sys
import timeit


class PointWithoutSlots:
    """Class without __slots__ to represent a point in 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointWithSlots:
    """Class with __slots__ to optimize memory usage for a point in 2D space."""
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


def measure_memory():
    """Function to measure the memory usage of instances."""
    point_no_slots = PointWithoutSlots(3.5, 4.5)
    point_with_slots = PointWithSlots(3.5, 4.5)
    print(point_no_slots.__dict__)
    try:
        print(point_with_slots.__dict__)
    except AttributeError:
        print("There was an error when tried to print '__dict__'!")

    size_no_slots = sys.getsizeof(point_no_slots) + sum(
        sys.getsizeof(getattr(point_no_slots, attr)) for attr in point_no_slots.__dict__)
    size_with_slots = sys.getsizeof(point_with_slots) + sum(
        sys.getsizeof(getattr(point_with_slots, attr)) for attr in PointWithSlots.__slots__)

    print("Memory used by instance without __slots__: {} bytes".format(size_no_slots))
    print("Memory used by instance with __slots__: {} bytes".format(size_with_slots))


def measure_performance():
    """Function to measure the performance of creating instances."""
    setup_code = """
from __main__ import PointWithoutSlots, PointWithSlots
"""
    test_code_no_slots = """
point = PointWithoutSlots(3.5, 4.5)
"""
    test_code_with_slots = """
point = PointWithSlots(3.5, 4.5)
"""
    no_slots_time = timeit.timeit(test_code_no_slots, setup=setup_code, number=10000000)
    with_slots_time = timeit.timeit(test_code_with_slots, setup=setup_code, number=10000000)

    print("Time to create 10,000,000 instances without __slots__: {:.6f} seconds".format(no_slots_time))
    print("Time to create 10,000,000 instances with __slots__: {:.6f} seconds".format(with_slots_time))


def main():
    """Main function to demonstrate the difference between classes with and without __slots__."""
    print("Comparing memory usage and performance:")
    measure_memory()
    measure_performance()


if __name__ == "__main__":
    main()
