#!/usr/bin/env python3
"""
Minimal test for weather_fetcher module without external dependencies.
Tests core functionality with mock data.
"""

import sys
sys.path.insert(0, '/home/runner/work/jarvis/jarvis')

from weather_fetcher import WeatherFetcher


def test_formatting():
    """Test formatting functions with mock data"""
    print("=" * 60)
    print("Testing Weather Fetcher Formatting Functions")
    print("=" * 60)
    
    fetcher = WeatherFetcher('test_api_key')
    
    # Test 1: Current weather formatting
    print("\n1. Testing current weather formatting:")
    print("-" * 60)
    mock_weather = {
        'city': 'Paris',
        'country': 'FR',
        'temperature': 22,
        'feels_like': 20,
        'humidity': 55,
        'condition': 'clear sky',
        'wind_speed': 8.2,
        'pressure': 1015
    }
    result = fetcher.format_current_weather(mock_weather)
    print(result)
    assert "Paris" in result
    assert "22°C" in result
    print("✅ PASS: Current weather formatting works correctly")
    
    # Test 2: Forecast formatting
    print("\n2. Testing forecast formatting:")
    print("-" * 60)
    mock_forecast = [
        {
            'date': 'Wednesday, January 03',
            'temp_min': 15,
            'temp_max': 25,
            'condition': 'sunny',
            'humidity': 50
        },
        {
            'date': 'Thursday, January 04',
            'temp_min': 14,
            'temp_max': 23,
            'condition': 'partly cloudy',
            'humidity': 58
        },
        {
            'date': 'Friday, January 05',
            'temp_min': 16,
            'temp_max': 26,
            'condition': 'clear sky',
            'humidity': 45
        }
    ]
    result = fetcher.format_forecast(mock_forecast)
    print(result)
    assert "3-Day Weather Forecast" in result
    assert "Wednesday" in result
    print("✅ PASS: Forecast formatting works correctly")
    
    # Test 3: None handling
    print("\n3. Testing None handling:")
    print("-" * 60)
    result = fetcher.format_current_weather(None)
    print(result)
    assert "Unable to fetch" in result
    print("✅ PASS: None handling works correctly")
    
    result = fetcher.format_forecast(None)
    print(result)
    assert "Unable to fetch" in result
    print("✅ PASS: Forecast None handling works correctly")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✅")
    print("=" * 60)


def test_api_structure():
    """Test that WeatherFetcher has all required methods"""
    print("\n" + "=" * 60)
    print("Testing Weather Fetcher API Structure")
    print("=" * 60)
    
    fetcher = WeatherFetcher('test_api_key')
    
    required_methods = [
        'fetch_current_weather',
        'fetch_forecast',
        'format_current_weather',
        'format_forecast'
    ]
    
    for method in required_methods:
        assert hasattr(fetcher, method), f"Missing method: {method}"
        print(f"✅ Method '{method}' exists")
    
    print("\n✅ All required methods present")
    print("=" * 60)


if __name__ == "__main__":
    try:
        test_api_structure()
        test_formatting()
        print("\n🎉 All weather_fetcher tests completed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
