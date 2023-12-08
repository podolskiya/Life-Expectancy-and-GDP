import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv('clean_df.csv')

civlib = df['civlib_eiu']
gdp = df['gdp_per_capita']
life_expectancy = df['life_expectancy']

#Summary Statistics
mean_civlib = civlib.mean() #5.5608666666666675
median_civlib = civlib.median() #5.59
std_dev_civlib = civlib.std() #2.5761382931808683
min_civlib = civlib.min() #0.29
max_civlib = civlib.max() #9.71
quanties_civlib = civlib.quantile([0.25, 0.5, 0.75])  #0.25    3.53    0.50    5.59     0.75    7.65


mean_gdp = gdp.mean() #608904486723.8187
median_gdp = gdp.median() #64616482167.7475
std_dev_gdp = gdp.std() #2489412262753.0005
min_gdp = gdp.min() #1296089479.45824
max_gdp = gdp.max() #23315080560000.0
quanties_gdp = gdp.quantile([0.25, 0.5, 0.75])  #0.25    1.771673e+10    0.50    6.461648e+10    0.75    3.176127e+11


mean_life_expectancy = life_expectancy.mean() #71.18847463414633
median_life_expectancy = life_expectancy.median() #71.977
std_life_expectancy = life_expectancy.std() #7.904000772165062
min_life_expectancy = life_expectancy.min() #52.525
max_life_expectancy = life_expectancy.max() #84.4456097560976
quanties_life_expectancy = life_expectancy.quantile([0.25, 0.5, 0.75])  #0.25    65.288000    0.50    71.977000     0.75    76.671848


# Visualization
plt.hist(gdp / 1e12, bins=10, density=True)  # Dividing by 1e12 to display in trillions
plt.xlabel('GDP (in trillions)')
plt.ylabel('Density')
plt.title('GDP Histogram')
formatter = FuncFormatter(lambda x, _: f'{x:.0f}T')  
plt.gca().xaxis.set_major_formatter(formatter)
plt.show()
print(gdp.head(30))

plt.hist(civlib, bins = 10)
plt.xlabel('Liberty')
plt.ylabel('Density')
plt.title('Liberty Index Histogram')
plt.show()


plt.hist(life_expectancy)
plt.xlabel('Life Expectancy')
plt.ylabel('Density')
plt.title('Life Expectancy Histogram')
plt.show()


# Bivariate Statistics
plt.scatter(civlib, life_expectancy, color='blue', label='Data Points')
coefficients = np.polyfit(civlib, life_expectancy, 1)
poly = np.poly1d(coefficients)
plt.plot(civlib, poly(civlib), color='red', label='Fitted Line')
plt.xlabel('Civil Liberties')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy vs Civil Liberties')
plt.legend()
plt.grid(True)
plt.show()

sorted_df = gdp.sort_values(ascending=False)
print(sorted_df)
