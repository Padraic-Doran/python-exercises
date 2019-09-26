#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pydataset import data



# In[3]:


np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

print(df)


# In[13]:


# Create a column named passing_english that indicates whether each student has a passing grade in reading.



df = df.assign(passing_english = df.english >= 70)


# In[17]:


# Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='english', ascending = True)


# In[18]:


# Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. 
# The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

df.sort_values(['passing_english',"name"])


# In[21]:


# Sort the english grades first by passing_english, 
# and then by the actual english grade, similar to how we did in the last step.

df[df.passing_english].sort_values(by='english', ascending = False)


# In[23]:


# Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.

df.assign(overall_grade = ((df.math + df.english + df.reading)/3))


# In[25]:


# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

mpg = data('mpg')
mpg


# In[26]:


mpg.describe()


# In[27]:


mpg.info()


# In[28]:


mpg.shape


# In[29]:


mpg.dtypes


# In[45]:


mpg.describe()


# In[43]:


mpg[mpg['cty']>mpg['hwy']]


# In[44]:


# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
# Which car (or cars) has the highest mileage difference?

mpg['mileage_difference']=mpg['hwy']-mpg['cty']
mpg


# In[138]:


# Which car (or cars) has the highest mileage difference?
mpg.sort_values(by = 'mileage_difference', ascending = False).head(10)


# In[136]:


# Which compact class car has the lowest highway mileage? The best?

# mpg[mpg['class'] == 'compact'].sort_values('cty')
mpg[mpg['class'] == 'compact'].sort_values('hwy', ascending = False).max()


# In[135]:


mpg[mpg['class'] == 'compact'].sort_values('hwy', ascending = False).min()


# In[63]:


print(mpg[['manufacturer','model','hwy','cty']].groupby(['manufacturer','model']).agg(np.mean).sort_values(['hwy','cty'],ascending=False))


# In[42]:


mpg.manufacturer.describe()
len(mpg.manufacturer.unique())


# In[66]:


# Create a column named average_mileage that is the mean of the city and highway mileage.

print(mpg['average_mileage']=(mpg['hwy']+mpg['cty'])/2)


# In[67]:


# Which dodge car has the best average mileage? The worst?
print(mpg[mpg['manufacturer'] == 'dodge'].sort_values('average_mileage', ascending = False).max())


# In[68]:


# Which dodge car has the best average mileage? The worst?
print(mpg[mpg['manufacturer'] == 'dodge'].sort_values('average_mileage', ascending = False).min())


# In[76]:


# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

Mammals = data('Mammals')

# How many rows and columns are there?
Mammals.shape


# In[77]:


Mammals.describe()


# In[78]:


Mammals.info()


# In[79]:


Mammals


# In[102]:


# What is the the weight of the fastest animal?

# mammals.sort_values('speed', ascending = False)

print(mammals[['weight','speed']].sort_values(by='speed',ascending = False).head(1))


# In[127]:


# What is the overal percentage of specials?

# specials_count = Mammals[Mammals['specials'] == True].count()
# Mammals['specials'].count()
# overall_percentage = (specials_count / Mammals['specials'].count()). * 100
# print(overall_percentage)
print(Mammals.specials.mean()*100)


# In[133]:


# How many animals are hoppers that are above the median speed? What percentage is this?
# len(Mammals[(Mammals.hoppers==True)])
# Mammals.speed.median()
hopper_count = len(Mammals[(Mammals.hoppers==True) &(Mammals.speed>Mammals.speed.median())])/len(Mammals)*100

print(hopper_count)


# In[ ]:





# In[ ]:




