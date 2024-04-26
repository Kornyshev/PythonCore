import functools


def memoize(f):
    """
    Memoization decorator to cache results of function calls.
    """
    cache = {}

    @functools.wraps(f)
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def type_check(expected_types, return_type=None):
    """
    Decorator to enforce argument types and optionally the return type.
    """

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for a, t in zip(args, expected_types):
                assert isinstance(a, t), f"Argument {a} is not of type {t}"
            result = f(*args, **kwargs)
            if return_type:
                assert isinstance(result, return_type), f"Return value {result} is not of type {return_type}"
            return result

        return wrapper

    return decorator


@type_check((int, int), int)
def add(a, b):
    """
    Return the sum of two integers.
    """
    return a + b


def copy_func_properties(src):
    """
    Decorator to copy documentation and other attributes from the source function.
    """

    def decorator(dst):
        @functools.wraps(src)
        def wrapper(*args, **kwargs):
            return dst(*args, **kwargs)

        return wrapper

    return decorator


@copy_func_properties(fibonacci)
def fibonacci_decorated(n):
    """
    This docstring will be replaced by that of fibonacci.
    """
    return fibonacci(n)


def main():
    print("Fibonacci of 10:", fibonacci(10))
    print("Add 2 and 3:", add(2, 3))
    # print("Add 'String' and 3:", add("String", 3))
    print("Fibonacci decorated doc:", fibonacci_decorated.__doc__)


if __name__ == "__main__":
    main()
