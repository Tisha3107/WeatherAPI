import requests
import json
import pyttsx3 as pt

robo = pt.init()
city = input("Enter the City Name :")
url = f"https://api.weatherapi.com/v1/current.json?key=506463fd41a84a10b4822326242606&q={city}"

r = requests.get(url)
dict = json.loads(r.text)
w = dict["current"]["temp_c"]
condition_text = dict["current"]["condition"]["text"]
print(f"The Current Temperature of {city} is {w}°C and weather is {condition_text}")
robo.say(f"The Current Temperature of {city} is {w}°C and weather is {condition_text}")
robo.runAndWait()
