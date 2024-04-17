import requests
import json

api_key = "bfd33d92367b025e1494b536e64d8b25"  # Replace with your actual API key
city = input("enter your city")
#url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a991141538230103&q={city}"
#url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#url=f"https://tile.openweathermap.org/map/appid={api_key}"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
#print(response.text)
data = response.json()

print(f"Temperature in {city}: {data['main']['temp']-273.15} celcius")