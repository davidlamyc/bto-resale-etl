import requests
import os, errno
import pandas as pd
import json

filename='unique-addresses.csv'

try:
    os.remove(filename)
except OSError:
    pass

df = pd.read_csv("./resaleflatprices_combined_raw.csv")

df['full_address'] = df['block'] + ' ' + df['street_name']

df['search_address'] = df['full_address'] + ', ' + df['town'] + ', SINGAPORE'

file = open(filename, "a")
file.write('unique_address,town,country\n')

for address in df.search_address.unique():
    file = open(filename, "a")
    file.write(f'{address}\n')
