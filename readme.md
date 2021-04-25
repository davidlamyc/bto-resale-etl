# HBD Resale Data

The following table describes the data available in `resale-cleaned-and-transformed.csv`. (The file is too big to upload to github, sadly I cannot make it available directly in this repo)

The main data source is from [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices).

You may get an idea of how derived columns were made by referring to the scripts in this repo. (I might make a continuous pipe if I have the time. :sunglasses:)


|             | data source | derivation  | notes       |
| ----------- | ----------- | ----------- | ----------- |
| town        | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |
| flat_type   | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |
| flat_model  | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none | raw data was a mixture of capitalised and non-capitalised string, made all capitalised
| flat_type   | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |                    
| floor_area_sqm | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |    
| street_name | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |           
| resale_price | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |     
| month   | derived | using original data from [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices), split the 'month' column with a format of "YYYY-MM" to get just the month of sale |               
| lease_commence_date  | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |      
| storey_range | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |                 
| block  | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |            
| remaining_lease  | [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) | none |     
| full_address  | derived | using original data from [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices), joined 'block' and 'street_name' columns with a space(' ') |           
| latitude    | [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview) | none |
| longitude  | [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview) | none |
| year   | derived | using original data from [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices), split the 'month' column with a format of "YYYY-MM" to get just the year of sale|     
| minimum_distance (poorly named, to be renamed in the next iteration)  | derived | distance to closest MRT station calculated using distance formula, with the origin point's coordinates from the 'latitude' and 'longitude' columns, and with the destination point's coordinates from [here](https://github.com/hxchua/datadoubleconfirm/blob/master/datasets/mrtsg.csv) | in degrees
| closest_station  | derived | corresponding nearest station to 'minimum_distance' column | 
| cpi  | [MAS CPI calculator](https://eservices.mas.gov.sg/statistics/calculator/GoodsAndServices.aspx)| none  | base year is 2019, as data for 2020 and 2021 was unavailable, I assumed a CPI of 100
| adjusted_price | derived | calculated using the 'CPI' column, where cost of market basket in current period / cost of market basket in base period * 100 |
| calculated_remaining_lease | derived | 99 years - (year - lease_commence_date) | 