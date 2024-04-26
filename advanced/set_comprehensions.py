def unique_squares(numbers):
    """
    Uses a set comprehension to find the squares of numbers, removing any duplicates.
    """
    squares = {x ** 2 for x in numbers}
    print(f"Unique squares: {squares}")


def common_elements(sequences):
    """
    Uses set comprehensions to find common elements in multiple lists.
    """
    common = set.intersection(*(set(seq) for seq in sequences))
    print(f"Common elements across all sequences: {common}")


def unique_normalized_texts(texts):
    """
    Normalize texts to a standard form and remove duplicates.
    """
    normalized = {text.strip().lower() for text in texts}
    print(f"Unique normalized texts: {normalized}")


def even_numbers_range(n):
    """
    Uses a set comprehension to generate all even numbers up to n.
    """
    evens = {x for x in range(n + 1) if x % 2 == 0}
    print(f"Even numbers up to {n}: {evens}")


def main():
    numbers = [1, 2, 2, 3, 4, 4, 4, 5, -1, -2, 6]
    sequences = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    texts = [" Hello World ", "hello world", "HELLO WORLD "]

    print("Processing with set comprehensions:")
    unique_squares(numbers)
    common_elements(sequences)
    unique_normalized_texts(texts)
    even_numbers_range(10)


if __name__ == "__main__":
    main()
