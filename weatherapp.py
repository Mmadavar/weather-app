import requests
import json
API = '69877f05f4462e7077666d60b0712f19'

city_input = input("Enter City:")

data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API}")

weather = data.json()['weather']
temperature = data.json()['main']['temp']
temperature_max = data.json()['main']['temp_max']
temperature_min = data.json()['main']['temp_min']
print(f'The temperature is {temperature}')
print(f'The maximum temperature is {temperature_max}')
print(f'The minimum temperature is {temperature_min}')


