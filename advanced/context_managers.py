import contextlib


# Class-based context manager
class Resource:
    """
    Class-based context manager to manage a simulated resource.
    """

    def __enter__(self):
        print("Opening resource.")
        self.name = "Resource Name"
        return self  # This is what is returned to the "as" part of the "with" statement.

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing resource.")
        # Handle exceptions if necessary
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        # Return False to propagate exceptions, True to suppress them
        return False

    @staticmethod
    def process():
        print("Processing resource.")


# Decorator-based context manager
@contextlib.contextmanager
def temporary_change(obj, attr, value):
    """
    Temporarily changes an attribute of an object during the context.
    """
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, original)


# Use of the context managers
class Dummy:
    """ Example class to demonstrate temporary_change context manager. """

    def __init__(self, attribute):
        self.attribute = attribute


def main():
    # Using the class-based context manager
    with Resource() as res:
        res.process()

    # Using the decorator-based context manager
    dummy = Dummy("Original Value")
    print(f"Original: {dummy.attribute}")
    with temporary_change(dummy, 'attribute', "Changed Value"):
        print(f"Changed: {dummy.attribute}")
    print(f"Reverted: {dummy.attribute}")


if __name__ == "__main__":
    main()
