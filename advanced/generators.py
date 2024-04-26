def populate_large_file(file_path, num_lines):
    """
    Populates a file with a specified number of lines for testing the read_large_file generator.

    Args:
        file_path (str): The path to the file where the data will be written.
        num_lines (int): The number of lines to write to the file.
    """
    with open(file_path, 'w') as file:
        for i in range(num_lines):
            # Write a line of data. Here, we simply repeat the line number several times.
            # You could customize this content as needed.
            file.write(f"Line {i + 1}: " + " ".join([str(i + 1)] * 5) + "\n")


def read_large_file(file_path):
    """
    A generator function to read a large file line by line.
    This approach is memory-efficient as it only loads one line into memory at a time.
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def fibonacci_sequence():
    """
    A generator function to produce an infinite sequence of Fibonacci numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def transform_data(data):
    """
    Processes numbers by squaring them. This generator takes an iterable of numbers as input.
    """
    for number in data:
        yield number ** 2


def filter_even(numbers):
    """
    Filters only even numbers from the input iterable using a generator.
    """
    for number in numbers:
        if number % 2 == 0:
            yield number


def main():
    # Define the path to the file and the number of lines you want to write
    file_path = 'large_data.txt'
    num_lines = 10  # Number of lines to write

    # Call the function to populate the file
    populate_large_file(file_path, num_lines)
    print(f"File '{file_path}' has been populated with {num_lines} lines of data.")

    # Example use of the large file reader
    for line in read_large_file('large_data.txt'):
        print(line)  # Process each line

    # Example use of the Fibonacci sequence generator
    fib_gen = fibonacci_sequence()
    for _ in range(10):  # Print first 10 Fibonacci numbers
        print(next(fib_gen))

    # Example of using a pipeline of generator functions
    numbers = range(10)
    squared_numbers = transform_data(numbers)
    even_squares = filter_even(squared_numbers)
    for number in even_squares:
        print(number)  # Print even squares of numbers from 0 to 9


if __name__ == "__main__":
    main()
