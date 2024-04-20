#!/usr/bin/env python
# coding: utf-8

# In[44]:


#LOAD AND EXPLORE THE DATASET

#Display first few rows
import pandas as pd
url = "https://github.com/fuatkina/Social-Sciences-and-Computing-2024-Spring/raw/7fd77793a91a51a1740e08b51e81d36bc8a1f902/Datasets/GSS_2022_stata/2022/GSS2022.dta"
data = pd.read_stata(url,convert_categoricals=False)

print(data.head())
print()

#Variables
print(list(data.columns))

#Missing Values
missing = data.isnull()
num = missing.sum()
print("Total Missing:",num)
data = data.fillna(method="bfill")


# In[45]:


#2.DESCRIPTIVE STATISTICS
import seaborn as sns
import os

#Basic statistics
print(data.describe())



# In[49]:


#Simple visualizations
sns.histplot(x=data['joblose'],bins=4,color="red")


# In[52]:


sns.boxplot(x=data['joblose'])


# In[54]:


#3.INFERENTIAL STATISTICS
#Hypothesis test
#Hypothesis: The likelihood of female workers facing the threat of jobloss is higher compared to male workers.
female_job = data[data["sex"]==2]["joblose"]
male_job = data[data["sex"]==1]["joblose"]
from scipy import stats 
stats.levene(female_job, male_job)


# In[57]:


#T-test
import statsmodels.stats.api as sms
table = sms.CompareMeans.from_data(female_job,male_job)
table.summary( usevar='pooled')


# In[61]:


#4.CORRELATION ANALYSIS
xy = sns.scatterplot(x="prestg10", y="educ",data=data)
xy.set_title("Education Leven vs. Prestige")
xy.set_xlabel("Prestige")
xy.set_ylabel("Education")
sns.lmplot(x="prestg10", y="educ",data=data)


# In[ ]:




