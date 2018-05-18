
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[2]:


conn = sqlite3.connect("factbook.db")
q = "SELECT * FROM sqlite_master WHERE type='table';" 
pd.read_sql_query(q, conn)


# In[3]:


query = "select * from facts LIMIT 5;"
"""cursor.execute(query)
first_five = cursor.fetchall()
print(first_five)"""
pd.read_sql_query(query, conn)


# In[4]:


query1 = "select MIN(population), max(population), min(population_growth), max(population_growth) from facts;"
pd.read_sql_query(query1, conn)


# In[5]:


query2 = "select name from facts where population = 0;"
pd.read_sql_query(query2, conn)


# In[6]:


query3 = "select name from facts where population = (select max(population) from facts);"
pd.read_sql_query(query3, conn)


# There are country entries for Antarctica and the world, which arent really countries and certainly wouldnt be for the purposes of this analysis, so remember to remove them for any calculations etc

# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize =(10,10))
ax = fig.add_subplot(111)


query4 = "select population, population_growth, birth_rate, death_rate from facts where population !=(select max(population) from facts) and population != (select min(population) from facts);"
pd.read_sql_query(query4, conn).hist(ax=ax)


# In[8]:


query5 = "select name, cast(population as float) / cast(area_land as float) pop_density from facts order by pop_density limit 50;"
pd.read_sql_query(query5, conn)

