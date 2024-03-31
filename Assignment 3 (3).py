#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install scrapy


# In[12]:


from scrapy import Selector
import requests

url = "https://www.paribucineverse.com/vizyondakiler"
html = requests.get(url).content
sel = Selector(text = html)

#Vizyondakiler

xpath_for_titles = '//*[@id="movieListRow"]/div/div/h3/text()'
movie_titles = sel.xpath(xpath_for_titles).extract()
movie_titles


# In[13]:


#Süre
xpath_for_time ="//*[@id='movieListRow']/div/div/p[1]/text()"
length = sel.xpath(xpath_for_time).extract()
length


# In[14]:


#Tür
xpath_for_type = "//*[@id='movieListRow']/div/div/p[2]/text()"
movie_type =sel.xpath(xpath_for_type).extract()
movie_type


# In[15]:


import pandas as pd
onscreen_movies = {"title":movie_titles, "genre":movie_type, "time":length}
movie_table = pd.DataFrame(onscreen_movies)
movie_table


# In[ ]:





# In[ ]:




