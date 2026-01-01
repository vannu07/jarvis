# in root dir, run -> python -m testing.weather_test

import os

from weather_fetcher import WeatherFetcher


def test_weather_fetcher():
    """Test the WeatherFetcher module"""
    print("🌤️  Jarvis Weather Fetcher Test Mode")
    print("-" * 50)

    # Get API key from environment
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    
    if not api_key:
        print("❌ Error: OPENWEATHERMAP_API_KEY not set in environment.")
        print("Please set it in your .env file or as an environment variable.")
        return

    fetcher = WeatherFetcher(api_key)
    
    print("Testing Weather Fetcher functionality...")
    print("-" * 50)

    # Test 1: Valid city - current weather
    print("\n📍 Test 1: Current weather for London")
    weather = fetcher.fetch_current_weather("London")
    if weather:
        print("✅ Current weather fetch successful!")
        print(fetcher.format_current_weather(weather))
    else:
        print("❌ Failed to fetch current weather for London")

    # Test 2: Valid city - forecast
    print("\n📍 Test 2: 5-day forecast for New York")
    forecast = fetcher.fetch_forecast("New York", days=5)
    if forecast:
        print("✅ Forecast fetch successful!")
        print(fetcher.format_forecast(forecast))
    else:
        print("❌ Failed to fetch forecast for New York")

    # Test 3: Invalid city
    print("\n📍 Test 3: Invalid city (should handle gracefully)")
    weather = fetcher.fetch_current_weather("InvalidCityNameXYZ123")
    if weather is None:
        print("✅ Correctly handled invalid city")
    else:
        print("❌ Should have returned None for invalid city")

    # Test 4: Different forecast lengths
    print("\n📍 Test 4: 3-day forecast for Paris")
    forecast = fetcher.fetch_forecast("Paris", days=3)
    if forecast and len(forecast) <= 3:
        print(f"✅ 3-day forecast successful! Got {len(forecast)} days")
        for day in forecast:
            print(f"  - {day['date']}: {day['temp_min']}°C to {day['temp_max']}°C")
    else:
        print("❌ Failed to fetch 3-day forecast")

    print("\n" + "=" * 50)
    print("Weather Fetcher Tests Complete!")
    print("=" * 50)


if __name__ == "__main__":
    test_weather_fetcher()
