import csv
import pandas as pd
import pycountry

gdp_per_capita = pd.read_csv('raw_gdp_per_capita.csv')
life_expectancy = pd.read_csv('raw_life_expectancy.csv')
civil_liberties = pd.read_csv('raw_civil_liberties_index.csv')

# Select only the last column and values
gdp_per_capita_2022 = gdp_per_capita[['Country Name', '2021']]
life_expectancy_2022 = life_expectancy[['Country Name', '2021']]
liberty_2022 = civil_liberties[civil_liberties['Year'] == 2021]

# Merge three datasets by country to make one dataset, with inner join
final_gdp = gdp_per_capita_2022.rename(columns={'2021': 'gdp_per_capita'})
final_life_expectancy = life_expectancy_2022.rename(columns={'2021': 'life_expectancy'})
print(liberty_2022.head(10))
print(final_life_expectancy.head(10))
print(final_gdp.head(10))
