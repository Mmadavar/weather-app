# imported the request library so I can use the get method eventually to extract data from the OpenWeather API so I can get the data for the weather.
import requests

# imported json to format the data from the OpenWeather API and once when I eventually use requests.get() and call
# the weather data points by .json() it puts everything together in a python dictionary 
import json

# This is the API key
API = '69877f05f4462e7077666d60b0712f19'

def get_data():
    
    # Here I am using the api.openweathermap.org api to get the weather data
    data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={API}")

    # Have the user input the City
    city_input = input("Enter City:")
    
    # Making sure to see if the request came through.
    if data.status_code != 200:
        raise Exception(f"Request failed with {data.status_code}")
    
    #Here we return data 
    return data