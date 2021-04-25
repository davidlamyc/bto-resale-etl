import pandas as pd
import os, errno
import math

resale_df = pd.read_csv("./resaleflatprices-distance.csv")
cpi_df = pd.read_csv("./housing-cpi.csv")

df = pd.merge(resale_df, cpi_df, how='left', left_on=['year'], right_on = ['year'])

df['adjusted_price'] = df['resale_price'] / df['cpi'] * 100

df.to_csv('./resaleflatprices_cpi.csv', index=False)