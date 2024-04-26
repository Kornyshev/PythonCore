def read_data(file_path):
    """
    Attempts to read data from a file and convert it to an integer list.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            numbers = [int(item) for item in data.split()]
            return numbers
    except FileNotFoundError:
        print("Error: The file does not exist.")
        raise  # Re-raises the exception after logging
    except ValueError:
        print("Error: All items in the file must be integers.")
        raise  # Re-raises the current exception
    finally:
        print("Attempted to read data.")


def process_data(numbers):
    """
    Processes a list of numbers by performing division, which can fail if zero is involved.
    """
    try:
        result = 10 / numbers[0]  # This could throw if numbers[0] is zero or if numbers is empty
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except IndexError:
        print("Error: No items in the list.")
    else:
        print("Division successful.")
    finally:
        print("Processed data.")


def main():
    """
    Main function to demonstrate exception handling.
    """
    try:
        numbers = read_data('data_non_exist.txt')
        # numbers = read_data('data.txt')
        process_data(numbers)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Main operation complete. Cleanup can happen here.")


if __name__ == "__main__":
    main()
