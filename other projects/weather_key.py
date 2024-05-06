import requests
import datetime as dt

def run():

    api_key = "5548a2497a58c868fd9b26d8fc07dba8"
    city = input("Enter city: ")
    
    print("Your weather report")
    weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}").json()
    
    if weather_data['cod'] == "404":
        
        print(f"{city} not found")
    else:
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        temp_max = weather_data['main']['temp_max']
        humi = weather_data['main']['humidity']
        wind = weather_data['wind']['speed']
        weather = weather_data['weather'][0]['description']
        sunset = dt.datetime.utcfromtimestamp(weather_data['sys']['sunset'] - weather_data['timezone'])
        sunrise = dt.datetime.utcfromtimestamp(weather_data['sys']['sunrise'] - weather_data['timezone'])
           
        print(f"Temperature in {city}: {temp}°C\n")
        print(f"Temperature feels like: {feels_like}°C\n")
        print(f"Temperatures might actually reach: {temp_max}°C\n")
        print(f"Humidity in {city}: {humi}%\n")
        print(f"Wind speed in {city}: {wind}m/s\n")
        print(f"Weather condition in {city}: {weather}\n")
        print(f"Sunrise in {city}: {sunrise} \n")
        print(f"Sunset in {city}: {sunset} \n")


ok = True
print("WELCOME TO YOUR WEATHER REPORT\n")
print("PLEASE ENTER YOU DESIRED LOCATION\n")
while ok:
    run()
    p = input("Are you done(yes/ no): ")
    if p == "yes":
        print("Have a beautiful day")
        break
    
    else:
        continue




        
