# Define custom exception classes

class Error(Exception):
    """Base class for other exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input."""

    def __init__(self, message):
        self.message = message


class CalculationError(Error):
    """Exception raised for errors during a calculation process."""

    def __init__(self, message, expression):
        self.message = message
        self.expression = expression


# Function that may raise custom exceptions

def divide(x, y):
    try:
        if y == 0:
            raise CalculationError("Cannot divide by zero.", f"{x} / {y}")
        result = x / y
    except CalculationError as e:
        print(f"Caught an error: {e.message} - Failed to evaluate expression: {e.expression}")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Executing finally clause.")


def process_input(user_input):
    try:
        value = int(user_input)
        if value < 0:
            raise InputError("Input must be a non-negative integer.")
        return value
    except ValueError:
        raise InputError("Invalid input: must be an integer.")


# Main function to use the above functionality

def main():
    try:
        x = process_input(input("Enter a non-negative integer for x: "))
        y = process_input(input("Enter a non-negative integer for y: "))
        print("Trying to divide x by y...")
        result = divide(x, y)
        if result is not None:
            print(f"Result: {result}")
    except InputError as e:
        print(f"Input error: {e.message}")


if __name__ == "__main__":
    main()
