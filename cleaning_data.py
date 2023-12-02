import csv
import pandas as pd
import pycountry

gdp_per_capita = pd.read_csv('raw_gdp_per_capita.csv')
life_expectancy = pd.read_csv('raw_life_expectancy.csv')
civil_liberties = pd.read_csv('raw_civil_liberties_index.csv')

#rename columns
gdp_per_capita.columns = ['Country', 'Indicator', 'Subject', 'Measure', 'Frequency', 'Date', 'GDP per Capita', 'Flag Codes']
life_expectancy.columns = ['Country', 'Indicator', 'Subject', 'Measure', 'Frequency', 'Date', 'Life Expectancy', 'Flag Codes']
civil_liberties.columns = ['Country', 'Country Code', 'Date', 'Value']

# sort date column and keep rows with latest data
gdp_data = gdp_per_capita[['Country', 'Date', 'GDP per Capita']]
df = pd.DataFrame(gdp_data)
df['Date'] = pd.to_datetime(df['Date'], format='%Y')
latest_gdp_data = df.sort_values(by='Date').groupby('Country').tail(1)

life_expectancy_data = life_expectancy[['Country', 'Date', 'Life Expectancy']]
df = pd.DataFrame(life_expectancy_data)
df['Date'] = pd.to_datetime(df['Date'], format='%Y')
latest_life_expectancy_data = df.sort_values(by='Date').groupby('Country').tail(1)

liberties_data = civil_liberties[['Country', 'Date', 'Value']]
df = pd.DataFrame(liberties_data)
df['Date'] = pd.to_datetime(df['Date'], format='%Y')
latest_liberties_data = df.sort_values(by='Date').groupby('Country').tail(1)

# rename country codes into full name


#combine datasets
