# 🌤️ Weather Forecast Application

A real-time weather application built with Python that provides current weather information and forecasts using API integration.

## 📋 Description

This Weather Application fetches real-time weather data from weather APIs to provide users with current conditions, forecasts, and various meteorological information for any location worldwide.

## ✨ Features

- **Real-Time Weather Data**: Get current weather conditions instantly
- **Location-Based Forecasts**: Search weather by city name or coordinates
- **Multiple Weather Parameters**:
  - Temperature (with feels-like)
  - Humidity levels
  - Wind speed and direction
  - Atmospheric pressure
  - Weather conditions (sunny, cloudy, rainy, etc.)
  - Visibility
- **Multi-Day Forecast**: View weather predictions for upcoming days
- **User-Friendly Interface**: Clean and intuitive design
- **Unit Conversion**: Switch between Celsius/Fahrenheit
- **Search History**: Quick access to previously searched locations

## 🛠️ Technologies Used

- **Python 3.x**
- **Requests**: For API calls
- **Weather API**: OpenWeatherMap or similar service
- **JSON**: For data parsing
- **tkinter/Flask**: (depending on your implementation) for UI

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Jkkklllllhgyu/OIB-SIP.git
```

2. Navigate to the weather folder:
```bash
cd OIB-SIP/weather
```

3. Install required dependencies:
```bash
pip install requests
```

4. Get your API key:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Copy your API key
   - Add it to the configuration file

5. Run the application:
```bash
python weather.py
```

## 💻 Usage

1. Run the script
2. Enter a city name or location
3. View current weather conditions
4. Check the extended forecast (if available)
5. Switch between temperature units as needed

## 🌡️ Weather Information Displayed

- **Current Conditions**: Real-time weather status
- **Temperature**: Current, minimum, and maximum
- **Feels Like**: Apparent temperature
- **Humidity**: Moisture percentage in the air
- **Wind**: Speed and direction
- **Pressure**: Atmospheric pressure
- **Visibility**: How far you can see
- **Sunrise/Sunset**: Times for the day

## 📸 Screenshots

*(Add screenshots of your application here)*

## 🎯 Use Cases

- Daily weather planning
- Travel preparation
- Outdoor activity planning
- Agricultural planning
- Event organization

## 🔑 API Configuration

Create a config file or add your API key directly:
```python
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
```

## 🌍 Supported Locations

- Search by city name
- Search by coordinates (latitude, longitude)
- Search by ZIP code
- International locations supported

## ⚠️ Note

- Requires active internet connection
- API rate limits may apply (check your API provider)
- Weather data accuracy depends on the API provider

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

**Jkkklllllhgyu**
- GitHub: [@Jkkklllllhgyu](https://github.com/Jkkklllllhgyu)

## 📝 License

This project is part of the Oasis Infobyte internship program.

## 🙏 Acknowledgments

- Oasis Infobyte for the internship opportunity
- OpenWeatherMap for weather data API
- Python requests library developers

## 🔮 Future Enhancements

- [ ] Hourly forecast
- [ ] Weather alerts and notifications
- [ ] Historical weather data
- [ ] Weather maps and radar
- [ ] Mobile responsive design

---

*Built with ❤️ during Oasis Infobyte Internship*