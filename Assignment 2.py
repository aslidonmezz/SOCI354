#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np
import pandas as pd



# 1.LOAD THE DATASET:
url_pop = "https://raw.githubusercontent.com/fuatkina/Social-Sciences-and-Computing-2024-Spring/7fd77793a91a51a1740e08b51e81d36bc8a1f902/Datasets/gapminder/population.csv"
url = "https://raw.githubusercontent.com/fuatkina/Social-Sciences-and-Computing-2024-Spring/7fd77793a91a51a1740e08b51e81d36bc8a1f902/Datasets/gapminder/life%20expectancy.csv"
url_gdp = "https://raw.githubusercontent.com/fuatkina/Social-Sciences-and-Computing-2024-Spring/7fd77793a91a51a1740e08b51e81d36bc8a1f902/Datasets/gapminder/gdp_pcap.csv"

pop = pd.read_csv(url_pop)
exp = pd.read_csv(url)
gdp = pd.read_csv(url_gdp)



# 2.DATA MERGING:
data_1 = pd.merge(pop, gdp, on='country')

data = pd.merge(data_1, exp, on='country')
data = pd.melt(data, id_vars=['country'], var_name='year', value_name='value')


#Changing string to float
def convert_value(value):
    if pd.isna(value) or not isinstance(value, str):
        return value
    elif value[-1] == 'k':
        return float(value[:-1]) * 1e3
    elif value[-1] == 'M':
        return float(value[:-1]) * 1e6
    elif value[-1] == 'B':
        return float(value[:-1]) * 1e9
    else:
        return float(value)
data['value'] = data['value'].apply(convert_value)

print(data)


#Categorizing type
data[['year', 'type']] = data['year'].str.split('_', expand=True) 
data['type'] = data['type'].replace('x', 'Population')
data['type'] = data['type'].replace('y', 'GDP')
data['type'] = data['type'].replace(np.nan, 'Life Expectancy')
population = data[data["type"] == "Population"]
life_expectancy = data[data["type"] == "Life Expectancy"]


# Rearrange columns
data = data[['country', 'year', 'type', 'value']]
data = pd.DataFrame(data)

print("DATA:")
print(data)

life_expectancy = data[data["type"] == "Life Expectancy"]
print(life_expectancy)
gdpp = data[data["type"]=="GDP"]
print(gdpp)




# In[87]:


# 3.DATA CLEANING AND PREPARATION:

#Identifying missing values 
missing_values = data.isnull()
num_missing = missing_values.sum()
print("")
print("DATA MISSING:")
print(num_missing) 
print("")

#Filling missing values
data["value"]=data["value"].fillna(method="ffill") 



# In[88]:


# 4.DATA EXPLORATION:
    
#First 5 Row
print("")
print("FIRST 5 ROW:")
print(data.head())
print("")
#Last 5 Row
print("")
print("LAST 5 ROW:")
print(data.tail())
print("")

#Year Base Data
yearbase_data = data[data["year"]=="2000"]
print("")
print("YEAR:2000")
print(yearbase_data)
print("")


# In[84]:


# 5. DATA FILTERING:

#Adding Continent 
url_cont = "https://github.com/dbouquin/IS_608/raw/77c1523be1684e04ed7d3c1a5fb584cbfcf9196e/NanosatDB_munging/Countries-Continents.csv"
cont = pd.read_csv(url_cont)
cont.rename(columns={'Country': 'country'}, inplace=True)
new_data = pd.merge(data,cont,how="inner")

#Choose Continent
cont_data = new_data[new_data['Continent']=="Africa"]
print("")
print("DATA OF AFRICA:")
print(cont_data)
print("")
#Population Less Than 1M
population_data = new_data[new_data["type"]=="Population"]
population_small= population_data[population_data["value"] < 1e6 ]
print("")
print("LESS THAN 1M POPULATION:")
print(population_small)
print("")




# In[89]:


# 6.DATA ORGANIZATION:
    
#Sorted Data
life_expectancy = new_data[new_data["type"] == "Life Expectancy"]
sorted_data = life_expectancy.sort_values(by='value', ascending=True)
print("")
print("LIFE EXPECTANCY:")
print(sorted_data)
print("")

#New Column
population_data.loc[:,"Level"] = "Low"
population_data.loc[population_data["value"] < 10e6, "Level"] = "Low"
population_data.loc[(population_data["value"] >= 10e6) & (population_data["value"] < 100e6), "Level"] = "Medium"
population_data.loc[population_data["value"] >= 100e6, "Level"] = "High"
print("")
print("POPULATION LEVEL")
print(population_data)
print("")


# In[85]:


# 7.BASIC DATA ANAYSIS:
    
#Gdp per capita
gdp_data = new_data[new_data["type"] == "GDP"]
population_data = new_data[new_data["type"] == "Population"]
gdp_per_capita = pd.merge(gdp_data, population_data, on=["country", "year", "Continent"])
gdp_per_capita["GDP_per_capita"] = gdp_per_capita["value_x"] / gdp_per_capita["value_y"]
gdp_per_capita = gdp_per_capita[["country", "year", "Continent", "GDP_per_capita"]]
max_life_expectancy = life_expectancy.loc[life_expectancy.groupby('year')['value'].idxmax()]
print("")
print("GDP PER CAPITA:")
print(gdp_per_capita)
print("")
#Highest life expectancy
max_life_expectancy = life_expectancy.loc[life_expectancy.groupby('year')['value'].idxmax()]
print("")
print("MAX LIFE EXPECTANCY BY YEAR:")
print(max_life_expectancy[['year', 'country', 'value']])
print("")


# In[90]:


# 8.DATA VISUALIZATION
norway_data = life_expectancy[life_expectancy["country"]=="Norway"].copy()
norway_data['year'] = norway_data['year'].astype(float)

norway_data = norway_data.sort_values(by="year")
norway_data.plot(x='year', y='value', kind='line', title='Life Expectancy Graph of Norway')
print(norway_data)



# In[23]:





# In[ ]:




