# utilities.py: Utility functions for data processing.

def average(values):
    """
    Calculate the average of a list of numbers.

    Args:
        values (list): A list of numbers.

    Returns:
        float: The average of the list.
    """
    return sum(values) / len(values) if values else 0
