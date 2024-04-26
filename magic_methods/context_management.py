class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        """
        Open the file and return it.
        """
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the file and handle any exceptions if necessary.
        """
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"Exception has occurred: {exc_type} with value '{exc_val}'")
        return True  # Prevents the exception from propagating


# Using the ManagedFile class with a context manager
with ManagedFile('hello.txt') as file:
    file.write('Hello, world!')
    raise ValueError("Just testing exception handling!")
