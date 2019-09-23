#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

b = a[a < 0]

print(len(b))


# In[5]:


# How many positive numbers are there?

b = a[a > 0]

print(len(b))


# In[8]:


# How many even positive numbers are there?

b = a[a % 2 == 0]
c = b[b > 0]
print(len(c))


# In[10]:


# If you were to add 3 to each data point, how many positive numbers would there be?

b = a +1
print(b)
c = b[b >0]
print(len(c))


# In[26]:


# If you squared each number, what would the new mean and standard deviation be?

b = np.square(a)
print(b)

c = np.std(b)
print(c)

d = np.mean(b)
print (d)


# In[28]:


# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.


centered = a - a.mean()
print(centered)



# In[30]:


# Calculate the z-score for each data point. Recall that the z-score is given by:

# Z
# =
# x
# −
# μ
# σ

def z_score(array):
    return (a - a.mean())/a.std()

print(z_score(a))


# In[32]:


import numpy as np
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list


sum_of_a = sum(a)

print(sum_of_a)


# In[33]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print(min_of_a)


# In[34]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
print(max_of_a)


# In[37]:


# Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = np.mean(a)
print(mean_of_a)


# In[38]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = np.prod(a)

print(product_of_a)


# In[40]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = np.square(a)

print(squares_of_a)


# In[45]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

a = np.array(a)
print(a)

odds_in_a = a[a % 2 == 1]

print(odds_in_a)


# In[46]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a[a % 2 ==0]

print(evens_in_a)


# In[50]:


## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
    ]

b = np.array(b)

#  Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
    
sum_of_b = np.sum(b)
print(sum_of_b)


# In[52]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 

min_of_b = b.min()
print(min_of_b)


# In[54]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
print(max_of_b)


# In[55]:


# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))

mean_of_b = b.mean()
print(mean_of_b)


# In[58]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        
product_of_b = np.product(b)
print(product_of_b)


# In[61]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
        
number_of_squares = np.square(b)
print(number_of_squares)


# In[62]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
print(odds_in_b)


# In[63]:


# # Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# In[66]:


# Exercise 9 - print out the shape of the array b

print(np.shape(b))


# In[67]:


# Exercise 10 - transpose the array b.


print(np.transpose(b))


# In[68]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

reshaped_b = np.reshape(b, 6)
print(reshaped_b)


# In[79]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

reshaped_b = np.reshape(b, (6,1))
print(reshaped_b)


# In[81]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)

min_of_c = np.min(c)
max_of_c = np.max(c)
sum_of_c = np.sum(c)
product_of_c = np.product(c)

print(min_of_c, max_of_c, sum_of_c, product_of_c)


# In[82]:


# Exercise 2 - Determine the standard deviation of c.

std_c = np.std(c)
print(std_c)


# In[83]:


# Exercise 3 - Determine the variance of c.

var_c = np.var(c)
print(var_c)


# In[84]:


# Exercise 4 - Print out the shape of the array c

print(np.shape(c))


# In[85]:


# Exercise 5 - Transpose c and print out transposed result.

transpose_c = np.transpose(c)
print(transpose_c)


# In[89]:


# Exercise 6 - Multiply c by the c-Transposed and print the result.

sum_of_tc = np.sum(transpose_c)

together = c * transpose_c
print(together)

sum_of_together = np.sum(together)
print(sum_of_together)


# In[90]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum_of_together = np.sum(together)
print(sum_of_together)


# In[91]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

product_transposed_c = np.product(transpose_c)

total_product = product_transposed_c * product_of_c
print(total_product)


# In[101]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d

sin_of_d = np.sin(d * np.pi / 180.)
                  
print(sin_of_d)


# In[103]:


# Exercise 2 - Find the cosine of all the numbers in d

cos_of_d = np.cos(d* np.pi / 180.)
print(cos_of_d)


# In[104]:


# Exercise 3 - Find the tangent of all the numbers in d

tan_of_d = np.tan(d * np.pi / 180.)
print(tan_of_d)


# In[106]:


# Exercise 4 - Find all the negative numbers in d

neg_d_numbers = d[d < 0]
print(neg_d_numbers)


# In[107]:


# Exercise 5 - Find all the positive numbers in d

pos_d_numbers = d[d > 0]


# In[115]:


# Exercise 6 - Return an array of only the unique numbers in d.
unique = np.unique(d)
print(unique)


# In[116]:


# Exercise 7 - Determine how many unique numbers there are in d.

unique = np.unique(d)
print(len(unique))


# In[117]:


# Exercise 8 - Print out the shape of d.

print(np.shape(d))


# In[118]:


# Exercise 9 - Transpose and then print out the shape of d.

transpose_d = np.transpose(d)
print(transpose_d)


# In[121]:


# Exercise 10 - Reshape d into an array of 9 x 2

reshaped_d = np.reshape(d, (9,2))
print(reshaped_d)


# In[ ]:




