# main.py: Main module to run the weather analysis.

from analysis import analyze_temperature, analyze_humidity
from data_loader import load_weather_data


def main():
    """
    Main function to coordinate the loading and analysis of weather data.
    """
    data = load_weather_data("weather_data.txt")
    avg_temp = analyze_temperature(data)
    avg_humidity = analyze_humidity(data)

    print(f"Average Temperature: {avg_temp}°C")
    print(f"Average Humidity: {avg_humidity}%")


if __name__ == "__main__":
    main()
