class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, increment=1):
        """
        Make the object callable and increase the count by the specified increment.
        """
        self.count += increment
        return self.count


# Using the Counter class as a callable
counter = Counter()
print(counter())  # Calls __call__, output: 1
print(counter())  # Calls __call__, output: 2
print(counter(5))  # Calls __call__ with argument, output: 7
