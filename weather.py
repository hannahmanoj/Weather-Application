# This line imports the requests library, which is used to send HTTP requests in Python.
import requests  

# Defines a constant API_KEY that stores the API key needed for accessing data from the OpenWeatherMap API.
API_KEY = 'yourAPIKEY'    
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'  # base url for OpenWeatherMap


 #  Function for retrieving data for specified city 
def get_weather_data(city):

    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)


    # If response is successfull it will store the JSON data as a dictionary in var data.
    if response.status_code == 200:
        data = response.json()  # Convert the JSON response into a Python dictionary
        return data
    else:
        print(f"City '{city}' not found. Please check the spelling.")
        return None
    
    
# Function to display the weather data.   
def display_weather_info(data):
    city_name = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather_description = data['weather'][0]['description']

    print(f"\nWeather Information for {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Condition: {weather_description.capitalize()}")

def main():
       city = input("Enter city name: ")
       weather_data = get_weather_data(city)

       if weather_data:
          display_weather_info(weather_data)

if __name__ == '__main__':
    main()
