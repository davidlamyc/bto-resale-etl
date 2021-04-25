import pandas as pd

df = pd.read_csv("./resaleflatprices-with-geo.csv")
min_df = pd.read_csv("./minimum-distance.csv")

df[['year','month']] = df['month'].str.split('-',expand=True)
df['year'] = df['year'].astype(str).astype(int)

print(df.dtypes)
print(min_df.dtypes)

agg_df = pd.merge(df, min_df, how='left', left_on=['full_address','year'], right_on = ['full_address','year'])

agg_df.to_csv('resaleflatprices-distance.csv', index=False)