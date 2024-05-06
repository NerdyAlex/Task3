import requests
import datetime as dt

api_key = "5548a2497a58c868fd9b26d8fc07dba8"
city = input("Enter city: ")


weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

temp = weather_data.json()

def kelivn_to_celsius(kel):    
    celsius = kel - 273.00
    print(f"The temperature is {celsius}C")


name = 'lexy'
name.capitalize
print(f"{name} is tall")

