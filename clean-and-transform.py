import pandas as pd

df = pd.read_csv("./resaleflatprices_cpi.csv")

df.drop('_id', inplace=True, axis=1)

df.flat_model = df.flat_model.str.upper()

df['calculated_remaining_lease'] = 99 - (df.year - df.lease_commence_date)

df.to_csv('./resale-cleaned-and-transformed.csv', index=False)