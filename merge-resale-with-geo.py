import pandas as pd

resale_df = pd.read_csv("./resaleflatprices_combined_raw.csv")
geo_df = pd.read_csv("./google-geocoding.csv")

resale_df['full_address'] = resale_df['block'] + ' ' + resale_df['street_name']

merged_df = resale_df.merge(geo_df, on='full_address', how='left')

# print(merged_df.head(50))

merged_df.to_csv('resaleflatprices-with-geo.csv', index=False)
