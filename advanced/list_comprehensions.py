# Generate squares of even numbers from 1 to 20
def generate_even_squares():
    squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]
    print("Squares of even numbers from 1 to 20:", squares)


# Flatten a list of lists using a nested list comprehension
def flatten_list_of_lists():
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat_list = [item for sublist in nested_list for item in sublist]
    print("Flattened list from nested lists:", flat_list)


# Create a list of employee names who earn above a certain salary
def high_earning_employees():
    employees = [
        {"name": "Alice", "salary": 55000},
        {"name": "Bob", "salary": 45000},
        {"name": "Charlie", "salary": 70000},
        {"name": "Diana", "salary": 65000},
    ]

    high_earners = [emp["name"] for emp in employees if emp["salary"] > 50000]
    print("Employees earning above 50,000:", high_earners)


# List comprehension with conditions and transformations
def create_word_length_dict():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    word_lengths = {word: len(word) for word in words if len(word) > 5}
    print("Words with length greater than 5:", word_lengths)


# Applying transformations with list comprehension
def convert_temperatures():
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = [(9 / 5 * celsius + 32) for celsius in celsius_temps]
    print("Converted temperatures from Celsius to Fahrenheit:", fahrenheit_temps)


def main():
    print("Generating squares of even numbers:")
    generate_even_squares()

    print("\nFlattening a list of lists:")
    flatten_list_of_lists()

    print("\nFinding high-earning employees:")
    high_earning_employees()

    print("\nCreating word length dictionary:")
    create_word_length_dict()

    print("\nConverting temperatures from Celsius to Fahrenheit:")
    convert_temperatures()


if __name__ == "__main__":
    main()
