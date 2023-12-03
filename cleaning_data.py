import csv
import pandas as pd
import pycountry

gdp_per_capita = pd.read_csv('raw_gdp_per_capita.csv')
life_expectancy = pd.read_csv('raw_life_expectancy.csv')
civil_liberties = pd.read_csv('raw_civil_liberties_index.csv')

# rename columns
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

# join gdp and life expectancy dataframes
gdp_life_expectancy = latest_gdp_data.merge(latest_life_expectancy_data)

# rename country codes into full name
def get_country_name(code):
    try:
        country = pycountry.countries.get(alpha_3=code)
        return country.name
    except AttributeError:
        return 'Unknown'

gdp_life_expectancy['Country'] = gdp_life_expectancy['Country'].apply(get_country_name)

# save files
fields = ['Country', 'Date', 'GDP per Capita', 'Life Expectancy']

with open('gdp_life_expectancy.csv', 'w', newline='') as output_csv:
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    output_writer.writeheader()
    
    for index, row in gdp_life_expectancy.iterrows():
        output_writer.writerow(row.to_dict())

fields = ['Country', 'Date', 'Value']

with open('liberty_data.csv', 'w', newline='') as output_csv:
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    output_writer.writeheader()
    
    for index, row in gdp_life_expectancy.iterrows():
        output_writer.writerow(row.to_dict())
