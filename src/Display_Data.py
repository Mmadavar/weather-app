import json


def result_data(data):



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

    #print description of the weather.
    print("Here's the general description of the weather.")
    print(weather)

    # printing the temperature in Farenheit and Celsius
    print(f'The temperature in Farenheit is {Farenheit} degrees')
    print(f'The temperature in Celsius is {Celsius} degrees')

    # printing the maximum and minimum temperature
    print('The maximum temperature in Farenheit is ' + str((temperature_max - 273.15) * 9/5 + 32) + ' degrees')
    print('The maximum temperature in Celsius is ' + str(temperature_max - 273.15) + ' degrees')
    print('The minimum temperature in Farenheit is ' + str((temperature_min-273.15) * 9/5 + 32) + ' degrees')
    print('The minimum temperature in Celsius is ' + str(temperature_min - 273.15) + ' degrees')


