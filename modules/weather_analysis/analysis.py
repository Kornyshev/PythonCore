# analysis.py: Provides analysis tools for weather data.

from utilities import average


def analyze_temperature(data):
    """
    Analyze temperature data to find the average temperature.

    Args:
        data (list of dict): Weather data.

    Returns:
        float: The average temperature.
    """
    temperatures = [day["temp"] for day in data]
    return average(temperatures)


def analyze_humidity(data):
    """
    Analyze humidity data to find the average humidity.

    Args:
        data (list of dict): Weather data.

    Returns:
        float: The average humidity.
    """
    humidities = [day["humidity"] for day in data]
    return average(humidities)
