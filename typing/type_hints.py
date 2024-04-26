def add_numbers(a: int, b: int) -> int:
    """
    Introduced in Python 3.5, type hints allow developers to explicitly state the expected data types of
    function arguments, return values, and variables. This can make Python code more readable and
    can be leveraged by static type checkers like mypy to catch bugs before runtime.
    """
    return a + b


if __name__ == '__main__':
    print(add_numbers("\nFirst String", "\nSecond String"))
