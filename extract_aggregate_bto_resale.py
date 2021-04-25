import requests
import os, errno
import pandas as pd
import json

# Resale transacted prices. Prior to March 2012, data is based on date of approval for the resale transactions.
# For March 2012 onwards, the data is based on date of registration for the resale transactions.

# Resale Flat Prices (Based on Registration Date), From Jan 2017 onwards
# https://data.gov.sg/api/action/datastore_search?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee&limit=5

# Resale Flat Prices (Based on Registration Date), From Jan 2015 to Dec 2016
# https://data.gov.sg/api/action/datastore_search?resource_id=1b702208-44bf-4829-b620-4615ee19b57c&limit=5

# Resale Flat Prices (Based on Registration Date), From Mar 2012 to Dec 2014
# https://data.gov.sg/api/action/datastore_search?resource_id=83b2fc37-ce8c-4df4-968b-370fd818138b&limit=5

# Resale Flat Prices (Based on Approval Date), 2000 - Feb 2012
# https://data.gov.sg/api/action/datastore_search?resource_id=8c00bf08-9124-479e-aeca-7cc411d884c4&limit=5

# Resale Flat Prices (Based on Approval Date), 1990 - 1999
# https://data.gov.sg/api/action/datastore_search?resource_id=adbbddd3-30e2-445f-a123-29bee150a6fe&limit=5
    
dataset_list = [
    {
        'resource_id': '42ff9cfe-abe5-4b54-beda-c88f9bb438ee',
        'duration': 'jan2017_present'
    },
    {
        'resource_id': '1b702208-44bf-4829-b620-4615ee19b57c',
        'duration': 'jan2015_dec2016'
    },
    {
        'resource_id': '83b2fc37-ce8c-4df4-968b-370fd818138b',
        'duration': 'mar2012_dec2014'
    },
    {
        'resource_id': '8c00bf08-9124-479e-aeca-7cc411d884c4',
        'duration': '2000_feb2012'
    },
    {
        'resource_id': 'adbbddd3-30e2-445f-a123-29bee150a6fe',
        'duration': '1990_1999'
    }
]

for dataset in dataset_list:
    filename=f'resaleflatprices_{dataset["duration"]}_raw.csv'

    # remove file if it already exists
    try:
        os.remove(filename)
    except OSError:
        pass

    # make api call to fetch data
    json_data = requests.get(f'https://data.gov.sg/api/action/datastore_search?resource_id={dataset["resource_id"]}&limit=1000000').json()

    # read json data into a dataframe
    df = pd.read_json(json.dumps(json_data['result']['records']))

    # write to file
    df.to_csv(filename, index=False)

try:
    os.remove('./resaleflatprices_combined_raw.csv')
except OSError:
    pass

df_1 = pd.read_csv("resaleflatprices_1990_1999_raw.csv")
df_2 = pd.read_csv("resaleflatprices_2000_feb2012_raw.csv")
df_3 = pd.read_csv("resaleflatprices_mar2012_dec2014_raw.csv")
df_4 = pd.read_csv("resaleflatprices_jan2015_dec2016_raw.csv")
df_5 = pd.read_csv("resaleflatprices_jan2017_present_raw.csv")

# combine dataframes
cdf = pd.concat([df_1,df_2,df_3,df_4,df_5], axis=0)

count = len(df_1.index) + len(df_2.index) + len(df_3.index) + len(df_4.index) + len(df_5.index)

# write to file
cdf.to_csv('resaleflatprices_combined_raw.csv', index=False)

print('Count: ' + str(count))

