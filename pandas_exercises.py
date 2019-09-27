#!/usr/bin/env python
# coding: utf-8

# In[22]:


from pydataset import data
import pandas as pd
import numpy as np

# Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
mpg = data('mpg')


# In[23]:


# How many different manufacturers are there?

# print(mpg['manufacturer'].unique().size)






# In[24]:


# On average, which manufacturer has the best miles per gallon?

mpg['manufacturer'].unique().size

mpg['average_mileage'] = (mpg['cty'] + mpg['hwy'])/2

manufacturers = mpg.groupby(['manufacturer']).mean()

# print(manufacturers['average_mileage'].idxmax())


# In[139]:


# How many different models are there?

models = mpg.groupby(['model']).mean()

# print(mpg.model.unique().size)


# In[35]:


# Do automatic or manual cars have better miles per gallon?

auto_trans = mpg[mpg['trans'].str.contains('auto')].groupby(['trans']).mean()
manual_trans = mpg[mpg['trans'].str.contains('manual')].groupby(['trans']).mean()
auto_mpg = auto_trans.average_mileage.mean() 
manual_mpg = manual_trans.average_mileage.mean()
print(auto_mpg)
print(manual_mpg)


# In[42]:


# Copy the users and roles dataframes from the examples above. What do you think a right join would look like? 
# An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
# print(users)

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
# print(roles)


# In[143]:


right_join = pd.merge(users, roles, left_on='role_id', right_on='id', how='right')
left_join = pd.merge(users, roles, left_on='role_id', right_on='id', how='left')
inner_join = pd.merge(users, roles, left_on='role_id', right_on='id', how='inner')
outer_join = pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')

# print(right_join)
# print(left_join)
# print(inner_join)
# print(outer_join)


# In[48]:


# Getting data from SQL databases

# Create a function named get_db_url. 
# It should accept a username, hostname, password, and database name
# and return a url formatted like in the examples in this lesson.

def get_db_url(user, password, host, database_name):
    from env import host, user, password
    return url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    
import pandas as pd
from env import host, user, password

database_name = "employees"
query = """SELECT * FROM employees"""

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

    


# In[52]:


# Use your function to obtain a connection to the employees database.

df = pd.read_sql(query, url)
df


# In[53]:


# Intentionally make a typo in the database url. What kind of error message do you see?

database_name = "employee"  # operational error

#      Intentionally make an error in your SQL query. What does the error message look like?

query = """SELECT * FROM employee""" # ProgrammingError


# In[55]:


# Read the employees and titles tables into two separate dataframes

employees_query = """SELECT * FROM employees"""
titles_query = """SELECT * FROM titles"""
employees = pd.read_sql(employees_query, url)
titles = pd.read_sql(titles_query, url)
titles
employees


# In[140]:


# Join the employees and titles dataframes together.
employees_and_titles = pd.merge(employees, titles)
employees_and_titles


# In[100]:


# For each title, find the hire date of the employee that was hired most recently with that title

employees_and_titles.sort_values('hire_date').groupby('title').tail(1)



# In[142]:


# Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)

dept_query = """SELECT * FROM departments join dept_emp on dept_emp.dept_no = departments.dept_no"""
dept_and_dept_emp = pd.read_sql(dept_query, url)
dept_and_dept_emp
t_dept_dept_emp = pd.merge(titles, dept_and_dept_emp)
t_dept_name = t_dept_dept_emp[['title', 'dept_name']]
titles_dept_name.groupby('dept_name').count()


# In[103]:


# Use your get_db_url function to help you explore the data from the chipotle database. 
# Use the data to answer the following questions:
    
database_name = "chipotle"
orders_query = """SELECT * FROM orders"""

url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

orders = pd.read_sql(orders_query, url)
orders


# In[135]:


# What is the total price for each order?

orders['stripped_price'] = orders['item_price'].str.replace('$',' ').str.strip().str.replace(',','_').astype(float)
orders

total_price_per_order = orders[['order_id', 'stripped_price']].groupby(['order_id']).sum()
print(total_price_per_order)


# In[134]:


# What are the most popular 3 items?
item_count = orders[['item_name', 'quantity']].groupby(['item_name']).count()
popular_items = item_count.sort_values('quantity', ascending = False).head(3)
print(popular_items)


# In[133]:


# Which item has produced the most revenue?
item_value = orders[['item_name', 'stripped_price']].groupby(['item_name']).sum()

most_revenue = item_value.sort_values('stripped_price', ascending = False).head(10)#(head()) I like lists
print(most_revenue)


# In[ ]:




