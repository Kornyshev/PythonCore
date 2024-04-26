# This script demonstrates the use of 'for' and 'while' loops in various scenarios.
# It covers iterating over lists, strings, dictionaries, nested loops, and control flow with break/continue.

def for_loop_over_list():
    """
    Iterates over a list of integers and prints each element.
    Demonstrates basic 'for' loop structure and enumeration.
    """
    numbers = [10, 20, 30, 40, 50]

    for index, number in enumerate(numbers):
        # The 'enumerate' function returns a tuple containing the index and value at that index.
        print(f"Index: {index}, Number: {number}")


def for_loop_over_string():
    """
    Iterates over a string and prints each character.
    Demonstrates 'for' loop with strings.
    """
    message = "Python"

    for char in message:
        print(f"Character: {char}")


def for_loop_over_dictionary():
    """
    Iterates over a dictionary's keys and values.
    Demonstrates 'for' loop with dictionaries.
    """
    student_grades = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Diana": 92,
    }

    for student, grade in student_grades.items():
        print(f"Student: {student}, Grade: {grade}")


def nested_for_loops():
    """
    Demonstrates nested 'for' loops to create a multiplication table.
    """
    rows = 5
    columns = 5

    # Outer loop iterates over the rows.
    for i in range(1, rows + 1):
        # Inner loop iterates over the columns.
        row_result = []
        for j in range(1, columns + 1):
            # Multiplying row and column indices to create multiplication table.
            row_result.append(i * j)
        print(" ".join(map(str, row_result)))


def while_loop_example():
    """
    Demonstrates a basic 'while' loop to countdown from a given number to zero.
    """
    countdown = 5

    while countdown >= 0:
        print(f"Countdown: {countdown}")
        countdown -= 1  # Decrease the countdown by 1 each iteration.


def loop_control_flow():
    """
    Demonstrates the use of 'break' and 'continue' in loops.
    """
    numbers = list(range(1, 11))

    # Using 'continue' to skip even numbers.
    print("Skipping even numbers:")
    for number in numbers:
        if number % 2 == 0:
            continue  # Skip to the next iteration if the number is even.
        print(f"Odd number: {number}")

    # Using 'break' to exit loop when a condition is met.
    print("\nBreaking the loop when number is greater than 7:")
    for number in numbers:
        if number > 7:
            break  # Exit the loop when the number is greater than 7.
        print(f"Number: {number}")


def main():
    """
    Main function to run various loop examples.
    """
    print("For loop over list:")
    for_loop_over_list()

    print("\nFor loop over string:")
    for_loop_over_string()

    print("\nFor loop over dictionary:")
    for_loop_over_dictionary()

    print("\nNested for loops (Multiplication Table):")
    nested_for_loops()

    print("\nWhile loop (Countdown):")
    while_loop_example()

    print("\nLoop control flow with break and continue:")
    loop_control_flow()


if __name__ == "__main__":
    main()
