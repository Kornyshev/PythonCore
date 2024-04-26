from functools import reduce

# Example data
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35, 40]

# Using map to square numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Using reduce to calculate the product of numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)

# Using zip to combine lists
zipped_names_ages = list(zip(names, ages))
print("Zipped names and ages:", zipped_names_ages)

# Using all to check if all numbers are positive
all_positive = all(x > 0 for x in numbers)
print("All numbers are positive:", all_positive)

# Using any to check if any name starts with 'A'
any_names_start_A = any(name.startswith('A') for name in names)
print("Any names start with 'A':", any_names_start_A)

# Using enumerate to get index and value from list
indexed_names = list(enumerate(names))
print("Indexed names:", indexed_names)

# Using sorted to sort names
sorted_names = sorted(names)
print("Sorted names:", sorted_names)

# Using reversed to reverse the list of numbers
reversed_numbers = list(reversed(numbers))
print("Reversed numbers:", reversed_numbers)
