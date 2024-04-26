# data_loader.py: Loads data for weather analysis.

def load_weather_data(filename):
    """
    Simulates loading weather data from a file.

    Args:
        filename (str): The name of the file containing weather data.

    Returns:
        list of dict: A list of dictionaries where each dictionary represents daily weather data.
    """
    print(f"Loading data from {filename}")
    # Simulating data loading process
    return [
        {"day": "Monday", "temp": 22, "humidity": 30},
        {"day": "Tuesday", "temp": 24, "humidity": 35},
        {"day": "Wednesday", "temp": 19, "humidity": 40},
    ]
