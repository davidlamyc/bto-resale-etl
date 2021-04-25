import requests
import os, errno
import pandas as pd
import json

df = pd.read_csv("unique-addresses.csv")

filename='google-geocoding.csv'

try:
    os.remove(filename)
except OSError:
    pass

file = open(filename, "a")
file.write('full_address,latitude,longitude')

for _, address in df.iterrows():
    search_address=f"{address['unique_address']},{address['town']},{address['country']}"
    data = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={search_address}&key=<key>')
    json_data = json.loads(data.text)

    print(search_address + ':')
    print(json_data['results'][0]['geometry']['location']["lat"])
    print(json_data['results'][0]['geometry']['location']["lng"])

    latitude = json_data['results'][0]['geometry']['location']["lat"]
    longitude = json_data['results'][0]['geometry']['location']["lng"]

    file = open(filename, "a")
    file.write(f"{address['unique_address']},{latitude},{longitude}\n")