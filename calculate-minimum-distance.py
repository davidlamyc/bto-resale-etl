import pandas as pd
import os, errno
import math

mrt_df = pd.read_csv("./mrt-with-year-transformed.csv")
df = pd.read_csv("./resaleflatprices-with-geo.csv")

df['full_address'] = df['block'] + ' ' + df['street_name']

df[['year','month']] = df['month'].str.split('-',expand=True)

df['year'] = df['year'].astype(str).astype(int)

df_unique_address_and_year = df.groupby(['full_address','year', 'latitude', 'longitude']).size().reset_index().rename(columns={0:'count'})

filename='minimum-distance.csv'

try:
    os.remove(filename)
except OSError:
    pass

file = open(filename, "a")
file.write("full_address,year,minimum_distance,closest_station\n")

for _, row in df_unique_address_and_year.iterrows():

    print(row['full_address'], row['year'], row['latitude'], row['longitude'])
    minimum_distance = 9999999999
    closest_station = ''
    full_address = row['full_address']
    street_latitude = row['latitude']
    street_longitude = row['longitude']
    street_year = row['year']
    for _, stn_row in mrt_df.iterrows():
        stn = stn_row['STN_NAME']
        stn_latitude = stn_row['Latitude']
        stn_longitude = stn_row['Longitude']
        stn_year = stn_row['year']
        calculated_distance = math.sqrt(pow(street_latitude - stn_latitude, 2) + pow(street_longitude - stn_longitude, 2))
        if (calculated_distance < minimum_distance and street_year >= stn_year):
            minimum_distance = calculated_distance
            closest_station = stn

    file = open(filename, "a")
    file.write(f"{full_address},{street_year},{minimum_distance},{closest_station}\n")