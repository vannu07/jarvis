#!/usr/bin/env python3
"""
Unit tests for weather_fetcher module using unittest and mocking.
Tests API interactions without requiring actual API credentials or network access.
"""

import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from weather_fetcher import WeatherFetcher


class TestWeatherFetcher(unittest.TestCase):
    """Test cases for WeatherFetcher class"""

    def setUp(self):
        """Set up test fixtures"""
        self.api_key = "test_api_key_12345"
        self.fetcher = WeatherFetcher(self.api_key)

    def test_initialization_with_valid_key(self):
        """Test WeatherFetcher initialization with valid API key"""
        fetcher = WeatherFetcher("valid_key")
        self.assertEqual(fetcher.api_key, "valid_key")
        self.assertEqual(fetcher.base_url, "https://api.openweathermap.org/data/2.5")

    def test_initialization_with_empty_key(self):
        """Test WeatherFetcher initialization with empty API key"""
        with self.assertRaises(ValueError):
            WeatherFetcher("")

    def test_initialization_with_none_key(self):
        """Test WeatherFetcher initialization with None API key"""
        with self.assertRaises(ValueError):
            WeatherFetcher(None)

    @patch('weather_fetcher.requests.get')
    def test_fetch_current_weather_success(self, mock_get):
        """Test successful current weather fetch"""
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "London",
            "sys": {"country": "GB"},
            "main": {
                "temp": 15.5,
                "feels_like": 13.2,
                "humidity": 72,
                "pressure": 1013
            },
            "weather": [{"description": "partly cloudy"}],
            "wind": {"speed": 3.5}
        }
        mock_get.return_value = mock_response

        weather_data, error = self.fetcher.fetch_current_weather("London")

        self.assertIsNone(error)
        self.assertIsNotNone(weather_data)
        self.assertEqual(weather_data['city'], "London")
        self.assertEqual(weather_data['country'], "GB")
        self.assertEqual(weather_data['temperature'], 16)  # rounded
        self.assertEqual(weather_data['feels_like'], 13)  # rounded
        self.assertEqual(weather_data['humidity'], 72)
        self.assertEqual(weather_data['condition'], "partly cloudy")
        self.assertEqual(weather_data['wind_speed'], 13)  # 3.5 m/s * 3.6 = 12.6, rounded to 13
        self.assertEqual(weather_data['pressure'], 1013)

    @patch('weather_fetcher.requests.get')
    def test_fetch_current_weather_city_not_found(self, mock_get):
        """Test current weather fetch with invalid city"""
        # Mock 404 response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404")
        mock_get.return_value = mock_response

        # Patch raise_for_status to raise HTTPError
        import requests
        with patch.object(mock_response, 'raise_for_status', side_effect=requests.exceptions.HTTPError(response=mock_response)):
            weather_data, error = self.fetcher.fetch_current_weather("InvalidCityXYZ")

            self.assertIsNone(weather_data)
            self.assertIsNotNone(error)
            self.assertIn("not found", error)

    @patch('weather_fetcher.requests.get')
    def test_fetch_current_weather_network_error(self, mock_get):
        """Test current weather fetch with network error"""
        import requests
        mock_get.side_effect = requests.exceptions.ConnectionError("Network error")

        weather_data, error = self.fetcher.fetch_current_weather("London")

        self.assertIsNone(weather_data)
        self.assertIsNotNone(error)
        self.assertIn("Network error", error)

    @patch('weather_fetcher.requests.get')
    def test_fetch_forecast_success(self, mock_get):
        """Test successful forecast fetch"""
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "list": [
                {
                    "dt": 1704067200,  # 2024-01-01 00:00:00
                    "main": {"temp_min": 10, "temp_max": 15, "humidity": 65},
                    "weather": [{"description": "clear sky"}]
                },
                {
                    "dt": 1704153600,  # 2024-01-02 00:00:00
                    "main": {"temp_min": 12, "temp_max": 18, "humidity": 60},
                    "weather": [{"description": "partly cloudy"}]
                },
                {
                    "dt": 1704240000,  # 2024-01-03 00:00:00
                    "main": {"temp_min": 11, "temp_max": 17, "humidity": 62},
                    "weather": [{"description": "cloudy"}]
                }
            ]
        }
        mock_get.return_value = mock_response

        forecast_data, error = self.fetcher.fetch_forecast("Paris", days=3)

        self.assertIsNone(error)
        self.assertIsNotNone(forecast_data)
        self.assertGreaterEqual(len(forecast_data), 1)
        self.assertIn('date', forecast_data[0])
        self.assertIn('temp_min', forecast_data[0])
        self.assertIn('temp_max', forecast_data[0])
        self.assertIn('condition', forecast_data[0])
        self.assertIn('humidity', forecast_data[0])

    def test_format_current_weather_with_data(self):
        """Test formatting current weather with valid data"""
        weather_data = {
            'city': 'Tokyo',
            'country': 'JP',
            'temperature': 25,
            'feels_like': 23,
            'humidity': 60,
            'condition': 'sunny',
            'wind_speed': 10,
            'pressure': 1015
        }

        result = self.fetcher.format_current_weather(weather_data)

        self.assertIn('Tokyo', result)
        self.assertIn('JP', result)
        self.assertIn('25°C', result)
        self.assertIn('23°C', result)
        self.assertIn('60%', result)
        self.assertIn('Sunny', result)
        self.assertIn('10 km/h', result)
        self.assertIn('1015 hPa', result)

    def test_format_current_weather_with_none(self):
        """Test formatting current weather with None"""
        result = self.fetcher.format_current_weather(None)
        self.assertIn('Unable to fetch', result)

    def test_format_forecast_with_data(self):
        """Test formatting forecast with valid data"""
        forecast_data = [
            {
                'date': 'Monday, January 01',
                'temp_min': 15,
                'temp_max': 25,
                'condition': 'sunny',
                'humidity': 50
            },
            {
                'date': 'Tuesday, January 02',
                'temp_min': 14,
                'temp_max': 23,
                'condition': 'cloudy',
                'humidity': 55
            }
        ]

        result = self.fetcher.format_forecast(forecast_data)

        self.assertIn('2-Day Weather Forecast', result)
        self.assertIn('Monday', result)
        self.assertIn('Tuesday', result)
        self.assertIn('15°C to 25°C', result)
        self.assertIn('Sunny', result)

    def test_format_forecast_with_none(self):
        """Test formatting forecast with None"""
        result = self.fetcher.format_forecast(None)
        self.assertIn('Unable to fetch', result)


if __name__ == "__main__":
    print("=" * 70)
    print("Running Weather Fetcher Unit Tests with Mocking")
    print("=" * 70)
    print()
    
    # Run tests with verbose output
    unittest.main(verbosity=2)

