# imported the request library so I can use the get method eventually to extract data from the OpenWeather API so I can get the data for the weather.
import requests

# imported json to format the data from the OpenWeather API and once when I eventually use requests.get() and call
# the weather data points by .json() it puts everything together in a python dictionary 
import json

# This is the API key
API = '69877f05f4462e7077666d60b0712f19'

# Have the user input the City
city_input = input("Enter City:")

# Getting the data from OpenWeather
data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API}")

# getting different data points about the weather.
weather = data.json()['weather']
temperature = data.json()['main']['temp']
humidity = data.json()['main']['humidity']
wind_speed = data.json()['wind']['speed']
temperature_max = data.json()['main']['temp_max']
temperature_min = data.json()['main']['temp_min']
weather_description = data.json()['weather'][0]['description']

# converting from Kelvin to farenheit to Celsius
Farenheit = (temperature - 273.15) * 9/5 + 32
Celsius = temperature - 273.15

# printing the temperature in Farenheit and Celsius
print(f'The temperature in Farenheit is {Farenheit} degrees')
print(f'The temperature in Celsius is {Celsius} degrees')

# printing the maximum and minimum temperature
print('The maximum temperature in Farenheit is' + ((temperature_max - 273.15) * 9/5 + 32) + 'degrees')
print('The minimum temperature in Farenheit is' + ((temperature_min-273.15) * 9/5 + 32) + 'degrees')



