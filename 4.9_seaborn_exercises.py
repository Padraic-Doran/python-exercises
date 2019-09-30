#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


iris = sns.load_dataset('iris')


# In[4]:


iris.dtypes


# In[5]:


sns.distplot(iris.petal_length)


# In[15]:


g = sns.relplot(x = 'petal_length', y = 'petal_width', hue = 'species', data=iris)


# In[14]:


f = sns.relplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data=iris)


# In[16]:


anscombe = sns.load_dataset('anscombe')


# In[19]:


anscombe.dtypes


# In[58]:


dset = anscombe.groupby('dataset').describe()
dset.transpose()


# In[62]:


sns.relplot(x='x', y='y', col='dataset', hue = 'y', data=anscombe)


# In[190]:


from pydataset import data
bug = data('InsectSprays')
bug


# In[192]:


plt.figure(figsize=(12, 10))
# plt.suptitle('Boxplots of Spray Data')

# plt.subplot(321)
sns.boxplot(data=bug, y= 'count', x= 'spray')
plt.title('Spray Effectiveness')


# In[201]:


from pydataset import data
swiss = data('swiss')
swiss.dtypes
swiss.Catholic > 50
swiss['is_catholic'] = swiss.Catholic > 50


swiss


# In[205]:


sns.relplot(x = 'Fertility', y = 'Catholic', hue = 'is_catholic', data=swiss)


# In[206]:


plt.figure(figsize=(7,7))
sns.heatmap(swiss.corr(),
            vmin=-1,
            cmap='coolwarm',
            annot=True);


# In[213]:


from env import host, user, password
    
def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

url = get_db_url(user, host, password, 'chipotle')
query = 'select * from orders'
chipotle = pd.read_sql(query,url)


# In[216]:


chipotle['price'] = chipotle['item_price'].apply(lambda x: float(x[1:]))
revenues = chipotle.groupby('item_name')['price'].sum().sort_values()

top_revenues = pd.Series(revenues.tail(4))

to_bar = pd.DataFrame()
to_bar['item'] = top_revenues.index
to_bar['revenue'] = top_revenues.values
sns.barplot(x='item', y='revenue', data=to_bar)


# In[232]:


from pydataset import data
sleep = data('sleepstudy')
sleep
sns.set_style('dark')
sns.set_context(font_scale=1,rc={"grid.linewidth": .5, "axes.linewidth": .5, "ytick.major.width": .5, "xtick.major.width": .5,"lines.linewidth": 0.5})
palette = sns.color_palette("husl", 18)
sns.lineplot(x='Days', y='Reaction', hue='Subject', data=sleep, palette=palette)
sns.set_context(rc={"lines.linewidth": 2})
sns.lineplot(x='Days', y='Reaction', data=sleep, ci=None)
# sns.despine()
plt.show()


# In[ ]:




