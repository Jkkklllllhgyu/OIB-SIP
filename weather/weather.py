import requests

API_KEY = "234aa643d15ee2be34db847b0a4eaa2e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print("❌ City not found or API error")
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print("\n🌤️ Weather Report")
        print("--------------------")
        print(f"City        : {city_name}")
        print(f"Temperature : {temp} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {condition.capitalize()}")

    except Exception as e:
        print("❌ Error fetching weather data")
        print(e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
