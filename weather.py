import requests
import json

api_key = "bfd33d92367b025e1494b536e64d8b25"  # Replace with your actual API key
city = input("enter your city")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(f"Temperature in {city}: {data['main']['temp']-273.15} celcius")
