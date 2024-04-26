# Variables and Data Types 

# This script demonstrates the use of variables and different data types in Python.
# Python is dynamically typed, meaning variables do not need to be declared with a type.

# Integer - int
# Represents whole numbers, positive or negative, without decimals.
integer_example = 42
print("Integer example:", integer_example)

# Floating Point Number - float
# Represents real numbers, can be positive or negative, containing one or more decimals.
float_example = 3.14159
print("Float example:", float_example)

# String - str
# Represents text. A string is a sequence of characters enclosed in single, double, or triple quotes.
string_example = "Hello, Python!"
print("String example:", string_example)

# Boolean - bool
# Represents truth values. Can be either True or False.
boolean_example = True
print("Boolean example:", boolean_example)

# NoneType - None
# Represents the absence of a value or a null value.
none_example = None
print("NoneType example:", none_example)

# Demonstrating dynamic typing
# Variables in Python can be reassigned to different data types.
dynamic_variable = 10
print("Dynamic variable initial type:", type(dynamic_variable))

dynamic_variable = "Now I'm a string"
print("Dynamic variable after reassignment:", dynamic_variable)
print("Dynamic variable new type:", type(dynamic_variable))


def demonstrate_variable_operations():
    """
    This function demonstrates basic operations with different data types,
    including arithmetic, concatenation, and type conversion.
    """
    print("\nFunction demonstrate_variable_operations():\n")

    # Arithmetic with int and float
    num1 = 10
    num2 = 3.5
    result = num1 + num2
    print("Adding int and float:", result)
    print("Adding int and float - type of result:", type(result))

    # String concatenation
    greeting = "Hello"
    name = "Alice"
    personalized_greeting = greeting + ", " + name + "!"
    print("String concatenation:", personalized_greeting)

    # Boolean in conditional
    flag = True
    if flag:
        print("Flag is True")
    else:
        print("Flag is False")

    # Converting float to int
    floating_point = 9.8
    integer_point = int(floating_point)
    print("Converted float to int:", integer_point)

    # Converting int to string
    age = 30
    age_string = str(age)
    print("Converted int to string:", age_string)


# Calling the function to demonstrate variable operations
demonstrate_variable_operations()

"""
Explanation
Integers and Floats: Demonstrates basic numeric types in Python with examples of both integer 
and floating-point numbers, followed by arithmetic operation.
Strings: Showcases string manipulation, including creation and concatenation of strings.
Booleans: Introduces boolean values and their use in a simple conditional statement to demonstrate logical operations.
NoneType: Presents the use of None, Python's null value equivalent, to represent the absence of a value.
Dynamic Typing: Python's dynamic typing capability is showcased by reassigning a variable initially set 
with an integer value to a string, demonstrating Python's flexibility in handling variable data types.
Function demonstrate_variable_operations: A detailed demonstration of operations including arithmetic operations, 
string concatenation, boolean logic, and type conversion among int, float, and str.

This script not only explores the basic data types and variable assignment in Python but also touches upon 
dynamic typing, basic operations, and type conversion, 
providing a comprehensive introduction to variables and data types in Python.
"""
