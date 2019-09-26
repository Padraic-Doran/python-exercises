#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd


fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits = pd.Series(fruits)

print(fruits)


# In[38]:


Run .describe() on the series to see what describe returns for a series of strings.

# fruits.describe()


# In[24]:


Run the code necessary to produce only the unique fruit names.

# fruits.unique()


# In[39]:


fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]


# In[40]:


print(fruits)


# In[41]:


fruits = pd.Series(fruits)


# In[42]:


fruits


# In[51]:


Determine how many times each value occurs in the series.

fvalcount = pd.Series(fruits).value_counts()
fvalcount


# In[65]:


# Determine the most frequently occurring fruit name from the series.
fvalcount.idxmax()
# Determine the least frequently occurring fruit name from the series.

fvalcount.idxmin()


# In[74]:


fruits.astype('str')


# In[92]:


# Write the code to get the longest string from the fruits series.
fruits[fruits.apply(len).idxmax()]


# In[93]:


print(fruits)


# In[97]:


# Find the fruit(s) with 5 or more letters in the name.
fruits[fruits.apply(lambda n: True if len(n) > 5 else False)]


# In[101]:


# Capitalize all the fruit strings in the series.
fruits.apply(lambda n: n.capitalize())


# In[102]:


# Count the letter "a" in all the fruits (use string vectorization)

def count_a(word):
    count = 0
    for letter in word:
        if letter in "a":
            count += 1
    return count

fruits.apply(count_a)


# In[103]:


# Output the number of vowels in each and every fruit.

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

fruits.apply(count_vowels)


# In[124]:


# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

froots = fruits[lambda x: fruits.str.count('o') >= 2]
froots


# In[130]:


# Write the code to get only the fruits containing "berry" in the name
fruits[fruits.str.contains('berry')]


# In[131]:


# Write the code to get only the fruits containing "apple" in the name

fruits[fruits.str.contains('apple')]


# In[137]:


# Which fruit has the highest amount of vowels?

fruits[fruits.apply(count_vowels).max()]


# In[139]:


# Use pandas to create a Series from the following data:
    
moola = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

moola = pd.Series(moola)

moola


# In[205]:


# What is the data type of the series?
# Use series operations to convert the series to a numeric data type.

mulla = moola.str.replace("$", "")
mulla = mulla.str.replace(",", "")
mulla = mulla.str.replace(".", "")
mulla = mulla.astype(int)
mulla


# In[209]:


# What is the maximum value? The minimum?
mulla.max()
mulla.min()


# In[225]:


# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
mulla
binz = pd.cut(mulla, 4,)
binz_count = binz.value_counts()
binz_count


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




