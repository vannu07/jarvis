import os
from datetime import datetime

import requests


class WeatherFetcher:
    """
    Weather fetching module using OpenWeatherMap API.
    Fetches current weather and 5-day forecast for any city.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def fetch_current_weather(self, city):
        """
        Fetch current weather for a given city.

        Args:
            city (str): City name

        Returns:
            dict: Weather data or None if error
        """
        endpoint = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # Use Celsius
        }

        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "wind_speed": round(data["wind"]["speed"] * 3.6, 1),  # Convert m/s to km/h
                "pressure": data["main"]["pressure"]
            }
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"City '{city}' not found.")
            else:
                print(f"HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except KeyError as e:
            print(f"Unexpected API response format: {e}")
            return None

    def fetch_forecast(self, city, days=5):
        """
        Fetch weather forecast for a given city.

        Args:
            city (str): City name
            days (int): Number of days (3-5)

        Returns:
            list: List of forecast data or None if error
        """
        # Limit days to 5 (API provides 5-day forecast)
        days = min(max(days, 3), 5)

        endpoint = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Group forecasts by day
            daily_forecasts = {}
            for item in data["list"]:
                # Get date from timestamp
                dt = datetime.fromtimestamp(item["dt"])
                date_key = dt.strftime("%Y-%m-%d")

                if date_key not in daily_forecasts:
                    daily_forecasts[date_key] = {
                        "date": dt.strftime("%A, %B %d"),
                        "temp_min": item["main"]["temp_min"],
                        "temp_max": item["main"]["temp_max"],
                        "condition": item["weather"][0]["description"],
                        "humidity": item["main"]["humidity"]
                    }
                else:
                    # Update min/max temperatures
                    daily_forecasts[date_key]["temp_min"] = min(
                        daily_forecasts[date_key]["temp_min"],
                        item["main"]["temp_min"]
                    )
                    daily_forecasts[date_key]["temp_max"] = max(
                        daily_forecasts[date_key]["temp_max"],
                        item["main"]["temp_max"]
                    )

            # Return only the requested number of days
            forecast_list = []
            for date_key in sorted(daily_forecasts.keys())[:days]:
                forecast = daily_forecasts[date_key]
                forecast["temp_min"] = round(forecast["temp_min"])
                forecast["temp_max"] = round(forecast["temp_max"])
                forecast_list.append(forecast)

            return forecast_list

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"City '{city}' not found.")
            else:
                print(f"HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except KeyError as e:
            print(f"Unexpected API response format: {e}")
            return None

    def format_current_weather(self, weather_data):
        """
        Format current weather data for display.

        Args:
            weather_data (dict): Weather data from fetch_current_weather

        Returns:
            str: Formatted weather string
        """
        if not weather_data:
            return "Unable to fetch weather data."

        return (
            f"Weather in {weather_data['city']}, {weather_data['country']}:\n"
            f"Temperature: {weather_data['temperature']}°C (Feels like {weather_data['feels_like']}°C)\n"
            f"Condition: {weather_data['condition'].capitalize()}\n"
            f"Humidity: {weather_data['humidity']}%\n"
            f"Wind Speed: {weather_data['wind_speed']} km/h\n"
            f"Pressure: {weather_data['pressure']} hPa"
        )

    def format_forecast(self, forecast_data):
        """
        Format forecast data for display.

        Args:
            forecast_data (list): Forecast data from fetch_forecast

        Returns:
            str: Formatted forecast string
        """
        if not forecast_data:
            return "Unable to fetch forecast data."

        lines = [f"\n{len(forecast_data)}-Day Weather Forecast:"]
        for forecast in forecast_data:
            lines.append(
                f"\n{forecast['date']}:\n"
                f"  Temperature: {forecast['temp_min']}°C to {forecast['temp_max']}°C\n"
                f"  Condition: {forecast['condition'].capitalize()}\n"
                f"  Humidity: {forecast['humidity']}%"
            )

        return "\n".join(lines)


if __name__ == "__main__":
    """
    Standalone usage example for testing.
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        print("Error: OPENWEATHERMAP_API_KEY environment variable not set.")
        print("Please set it in your .env file or environment.")
        exit(1)

    fetcher = WeatherFetcher(api_key)

    print("Welcome to Weather Fetcher!")
    print("Commands: weather <city>, forecast <city>, exit\n")

    while True:
        command = input("Enter command: ").strip()

        if command.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        elif command.lower().startswith("weather "):
            city = command[8:].strip()
            if city:
                weather = fetcher.fetch_current_weather(city)
                print(fetcher.format_current_weather(weather))
            else:
                print("Please specify a city name.")

        elif command.lower().startswith("forecast "):
            city = command[9:].strip()
            if city:
                forecast = fetcher.fetch_forecast(city, days=5)
                print(fetcher.format_forecast(forecast))
            else:
                print("Please specify a city name.")

        else:
            print("Invalid command. Use: weather <city>, forecast <city>, or exit")
