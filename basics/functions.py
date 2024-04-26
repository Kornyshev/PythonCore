# Demonstrates various aspects of defining and using functions in Python, including default parameters, keyword arguments,
# arbitrary argument lists, decorators, and closures.

def create_adder(x):
    """
    Demonstrates a closure in Python. Returns a function that adds 'x' to its argument.

    Args:
        x (int): A number to be added to a later provided number.

    Returns:
        function: A closure that adds 'x' to its argument.
    """

    def adder(y):
        return x + y

    return adder


def calculate_statistics(first, *additional, method="mean"):
    """
    Calculate statistics on a series of numbers using different methods.
    Demonstrates default parameters, arbitrary argument lists, and keyword arguments.

    Args:
        first (float): The first number in the series.
        *additional (float): Additional numbers in the series.
        method (str): The method of calculation, default is 'mean'.

    Returns:
        float: The calculated result based on the method.
    """
    numbers = (first,) + additional

    if method == "mean":
        return sum(numbers) / len(numbers)
    elif method == "total":
        return sum(numbers)
    elif method == "max":
        return max(numbers)
    elif method == "min":
        return min(numbers)
    else:
        raise ValueError("Unsupported method")


def print_details(name, **details):
    """
    Print details about an entity. Demonstrates the use of keyword arguments.

    Args:
        name (str): Name of the entity.
        **details (dict): Arbitrary keyword arguments representing details about the entity.
    """
    print(f"Details of {name}:")
    for key, value in details.items():
        print(f"  {key}: {value}")


def main():
    """
    Main function to demonstrate the use of various function types.
    """
    add_five = create_adder(5)
    print("Add 5 to 10:", add_five(10))

    print("\nStatistics for 1, 2, 3, 4 (mean):", calculate_statistics(1, 2, 3, 4))
    print("Statistics for 1, 2, 3, 4 (max):", calculate_statistics(1, 2, 3, 4, method="max"))

    print("\nPrinting details of a Car:")
    print_details("Car", make="Toyota", model="Corolla", year=2020, color="Red")


if __name__ == "__main__":
    main()
