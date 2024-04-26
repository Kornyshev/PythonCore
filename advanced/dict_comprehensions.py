def map_indices_to_values(values):
    """
    Uses a dictionary comprehension to map each value to its index in the list.
    """
    index_map = {value: idx for idx, value in enumerate(values)}
    print(f"Index map: {index_map}")


def invert_dictionary(original_dict):
    """
    Inverts a dictionary to swap its keys and values using a dictionary comprehension.
    """
    inverted_dict = {value: key for key, value in original_dict.items()}
    print(f"Inverted dictionary: {inverted_dict}")


def count_word_occurrences(text):
    """
    Counts occurrences of each word in a given text string using a dictionary comprehension.
    """
    words = text.split()
    word_count = {word.lower(): words.count(word) for word in words}
    print(f"Word occurrences: {word_count}")


def filter_positive_numbers(numbers):
    """
    Filters and keeps only positive numbers from a dictionary using a comprehension.
    """
    positive_numbers = {key: val for key, val in numbers.items() if val > 0}
    print(f"Positive numbers: {positive_numbers}")


def main():
    values = ['apple', 'banana', 'cherry']
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    text = "Hello world world"
    numbers = {'a': 1, 'b': -2, 'c': 3, 'd': -4, 'e': 5}

    print("Processing with dictionary comprehensions:")
    map_indices_to_values(values)
    invert_dictionary(original_dict)
    count_word_occurrences(text)
    filter_positive_numbers(numbers)


if __name__ == "__main__":
    main()
