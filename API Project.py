import requests
import json

movie = input("Please enter a movie title: ")

API_KEY = "4a111d85"
URL = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"

response = requests.get(URL)

data = response.json()

if data["Response"] == "True":
    fields = ["Title", "Year", "Genre", "Director", "Actors"]
    print()
    for field in fields:
        print(f"{field}: {data[field]}")

else:
    print("Movie not found.")