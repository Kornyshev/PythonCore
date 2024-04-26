# This script demonstrates the use of conditional statements in Python to make decisions based on different criteria.

def check_temperature(temp):
    """
    Function to recommend actions based on temperature.

    Args:
        temp (float): The current temperature in degrees Celsius.

    Returns:
        str: Recommended action based on the temperature.
    """
    if temp > 30:
        return "It's really hot! Consider staying indoors and drinking plenty of water."
    elif 20 <= temp <= 30:
        return "It's a nice day. Perfect for outdoor activities!"
    elif 10 <= temp < 20:
        return "It's a bit chilly. Wear a jacket if you're going out."
    else:
        return "It's very cold! Best to stay warm indoors."


def classify_number(number):
    """
    Classifies a number as positive, negative, or zero and checks for even/odd.

    Args:
        number (int): The number to classify.

    Returns:
        str: Classification of the number.
    """
    if number > 0:
        if number % 2 == 0:
            return f"{number} is positive and even."
        else:
            return f"{number} is positive and odd."
    elif number < 0:
        if number % 2 == 0:
            return f"{number} is negative and even."
        else:
            return f"{number} is negative and odd."
    else:
        return "The number is zero."


def user_permission(age, has_permission):
    """
    Determines if a user can access a restricted section based on age and permission flag.

    Args:
        age (int): The age of the user.
        has_permission (bool): Whether the user has explicit permission.

    Returns:
        str: Access message.
    """
    if age >= 18 and has_permission:
        return "Access granted."
    elif age >= 18 and not has_permission:
        return "Please obtain permission to access this section."
    else:
        return "Access denied due to age restrictions."


def main():
    """
    Main function to demonstrate the use of conditionals in Python.
    """
    # Example usage of the check_temperature function
    print(check_temperature(32))  # Hot scenario
    print(check_temperature(22))  # Pleasant scenario
    print(check_temperature(12))  # Chilly scenario
    print(check_temperature(2))  # Cold scenario

    # Example usage of the classify_number function
    print(classify_number(10))  # Positive even
    print(classify_number(-21))  # Negative odd
    print(classify_number(0))  # Zero

    # Example usage of the user_permission function
    print(user_permission(20, True))  # Adult with permission
    print(user_permission(20, False))  # Adult without permission
    print(user_permission(16, True))  # Minor with permission


if __name__ == "__main__":
    main()
