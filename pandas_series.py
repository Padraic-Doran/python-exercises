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


# In[377]:


Run the code necessary to produce only the unique fruit names.

# fruits.unique()


# In[378]:


fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]


# In[379]:


print(fruits)


# In[380]:


fruits = pd.Series(fruits)


# In[381]:


fruits


# In[382]:


Determine how many times each value occurs in the series.

fvalcount = pd.Series(fruits).value_counts()
print(fvalcount)


# In[383]:


# Determine the most frequently occurring fruit name from the series.
print(fvalcount.idxmax())
# Determine the least frequently occurring fruit name from the series.

print(fvalcount.idxmin())


# In[384]:


print(fruits.astype('str'))


# In[385]:


# Write the code to get the longest string from the fruits series.
print(fruits[fruits.apply(len).idxmax()])


# In[386]:


print(fruits)


# In[387]:


# Find the fruit(s) with 5 or more letters in the name.
print(fruits[fruits.apply(lambda n: True if len(n) >= 5 else False)])


# In[388]:


# Capitalize all the fruit strings in the series.
print(fruits.apply(lambda n: n.capitalize()))


# In[389]:


# Count the letter "a" in all the fruits (use string vectorization)

def count_a(word):
    count = 0
    for letter in word:
        if letter in "a":
            count += 1
    return count

print(fruits.apply(count_a))


# In[390]:


# Output the number of vowels in each and every fruit.

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

print(fruits.apply(count_vowels))


# In[391]:


# Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

froots = fruits[lambda x: fruits.str.count('o') >= 2]
print(froots)


# In[392]:


# Write the code to get only the fruits containing "berry" in the name
print(fruits[fruits.str.contains('berry')])


# In[393]:


# Write the code to get only the fruits containing "apple" in the name

print(fruits[fruits.str.contains('apple')])


# In[394]:


# Which fruit has the highest amount of vowels?

print(fruits[fruits.apply(count_vowels).max()])


# In[395]:


# Use pandas to create a Series from the following data:
    
moola = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

moola = pd.Series(moola)

moola


# In[396]:


# What is the data type of the series?
# Use series operations to convert the series to a numeric data type.

mulla = moola.str.replace("$", "")
mulla = mulla.str.replace(",", "")
mulla = mulla.str.replace(".", "")
mulla = mulla.astype(int)
print(mulla)


# In[397]:


# What is the maximum value? The minimum?
print(mulla.max())
print(mulla.min())


# In[398]:


# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
mulla
binz = pd.cut(mulla, 4,)
binz_count = binz.value_counts()
print(binz_count)


# In[399]:


# Plot a histogram of the data. Be sure to include a title and axis labels.
import matplotlib.pyplot as plt

histogram = mulla.plot.hist(bins=4,title="Price Distribution")
histogram.set_xlabel("Price")


# In[400]:


# Use pandas to create a Series from the following exam scores:

scorez = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

scorez = pd.Series(scorez)


# In[401]:


# What is the minimum exam score? The max, mean, median?

print(scorez.min())
print(scorez.mean())
print(scorez.median())


# In[402]:


# Plot a histogram of the scores.

histogram = scorez.plot.hist(bins=4,title="Score Distribution")
histogram.set_xlabel("Score")


# In[403]:


# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
def letter_grade(num_grade):
    if num_grade >=96:
        return('A+')
    elif num_grade <96 and num_grade >=92:
        return('A')
    elif num_grade <88 and num_grade >=86:
        return('B+')
    elif num_grade <86 and num_grade >=83:
        return('B')
    elif num_grade <83 and num_grade >=80:
        return('B-')
    elif num_grade <80 and num_grade >=75:
        return('C+')
    elif num_grade <74 and num_grade >=70:
        return('C')
    elif num_grade <70 and num_grade >=66:
        return('C-')
    elif num_grade <66 and num_grade >=64:
        return('D+')
    elif num_grade <64 and num_grade >=62:
        return('D')
    elif num_grade <62 and num_grade >=60:
        return('D-')
    else:
        return('F')
    
print(scorez.apply(letter_grade))


# In[404]:


# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

print(scorez.max())
print(rounded_scorez = scorez + (100 - scorez.max()))


# In[405]:


# Use pandas to create a Series from the following string:

welsh = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

welsh = list(welsh)
welsh = pd.Series(welsh)
welsh

welsh_count_values = welsh.value_counts()
print(welsh_count_values)


# In[406]:


# What is the most frequently occuring letter? Least frequently occuring?

welsh_count_values = welsh.value_counts()
most_freq_char = welsh_count_values.idxmax()
print(most_freq_char)

least_freq_char = welsh_count_values.idxmin()
print(least_freq_char)




# In[407]:


# How many vowels are in the list?
vowel_count = welsh.isin(list("aeiou")).sum()  

print(vowel_count)
                          


# In[408]:


consonant_count = welsh.size - welsh.isin(list("aeiou")).sum()
print(consonant_count)


# In[409]:


print(welsh.str.upper())

to_bar = welsh.value_counts()[:7]

print(to_bar.plot.bar())


# In[ ]:





# In[ ]:




