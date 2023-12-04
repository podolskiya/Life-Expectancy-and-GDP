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
merge_gdp_expectancy = pd.merge(final_gdp, final_life_expectancy)

# Standardize country names
liberty_2022.rename(columns={'Entity': 'Country Name'}, inplace = True)
def normalize_name(name):
    try:
        return pycountry.countries.lookup(name).name
    except LookupError:
        return name

liberty_2022['Country Name'] = liberty_2022['Country Name'].apply(normalize_name)
merge_gdp_expectancy['Country Name'] = merge_gdp_expectancy['Country Name'].apply(normalize_name)

liberty_2022.rename(columns={'Entity': 'Country Name'}, inplace = True)

merged_liberty_life = pd.merge(liberty_2022, merge_gdp_expectancy, on='Country Name', how='inner')

print(merged_liberty_life)
merged_liberty_life.to_csv('ready_df.csv')
