# from CU_function_exercises import remove_vowels
# remove_vowels('RGJJweapr')



# import CU_function_exercises as cfe

# from CU_function_exercises import remove_vowels as rv 

# print(rv('wfjnqergpvpoqweoaf'))

How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# import itertools

# print(list(e for e in itertools.product('ABC', '123')))

# print(len(list(e for e in itertools.product('ABC', '123'))))

How many different ways can you combine two of the letters from "abcd"?

# print(len(list(e for e in itertools.combinations_with_replacement('ABCD', 2))))

# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:

import json

profiles = open('profiles.json')

profiles_data = json.load(profiles)

# Total number of users
""" Remember, profiles_data is a list. Iterate like a list """

user_total = len(profiles_data)

# Number of active users

"""Remember isActive is boolean. x = a dictionary, so "for each dictionary in the list of dictionaries called
# profile_data, where the key isactive is set to True"
# """

active_total = len([x for x in profiles_data if x["isActive"]])

# print(active_total)

"""Same thing as above, but boolean is switched to False"""

inactive_total = len([x for x in profiles_data if not x["isActive"]])
# print(inactive_total)


# Grand total of balances for all users

"""Remember, the balances have unwanted character in the list, so they need to be removed.
Create a function to accomplish this task"""

def handle_balance(s):
    return float(s[1:].replace(',', ''))  """ Could also add a seconnd .replace() for $ """

""" Now that that/s accomplished, pass the all balance keys through the function. 
List comprehension looks like this: """

balances = [handle_balance(x['balance']) for x in profile_data]

""" Above means that the variable /balances/ GETS the values of the key named /balance/ for all dictionaries "x" 
in the list profile_data """

# print(balances)

# Average balance per user

""" Take the sum of balances and divide it by the number of balances """

total_balance = sum(balances)
average_balance = sum(balances) / len(balances)

# User with the lowest balance

""" from the lecture, Zach explained that anchoring the lowest balance to the first dictionary in the list
simplifies the program writing, because you're looping and replacing against a known index. As Kevin pointed out,
this could create a situation where multiple accounts have the lowest balance, and this code would not flag that """

user_with_the_lowest_balance
user_with_the_lowest_balance = profile_data[0]
for user in profile_data[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
        user_with_the_lowest_balance = user

""" The variable user_with_the_lowest_balance is set to the first index of profile_data. 
For each user(dictionary) in the list profile_data, starting at the SECOND index, 
if the balance key(having been run through the balance cleaning function) is less than the current
lowest balance, the variable user_with_the_lowest_balance is set to that user. """

# User with the highest balance

""" Same as above; just flipping the results from < to > and altering the variable name. """

user_with_the_highest_balance = profiles[0]
for user in profiles[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_the_highest_balance['balance']):
        user_with_the_highest_balance = user

### Alternative with a custom key function

""" The min function has key that you can manipulate. Here, the key is changed to read the lambda function """

min(profiles, key=lambda profile: handle_balance(profile['balance']))

""" Function created to pass the balances through the cleaning function. 
Said function is then made the key in min() """


def extract_balance(profile):
    return handle_balance(profile['balance'])
min(profiles, key=extract_balance)

# Most common favorite fruit
# Least most common favorite fruit

""" Using an import from a library called collection, 
importing just one function called Counter. Because the function was specifically imported, there is no need
to us collections.Counter. The datatype created is a !!!Countertype!!! """

from collections import Counter
Counter([p['favoriteFruit'] for p in profile_data])

"""The list comprehension reads, roughly, the Counter function to counter the variable
 of the dictionary (p) key 'favoriteFruit'
 for all dictionaries 'p'
 in the list of dictionaries called profile_data """

# For loop to create a dictionary of 'favoriteFruits'
 fruit_counts = {}
for profile in profile_data:
    fruit = profile['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

""" This creates a dictionary as the end results, as opposed to what the Counter function would produce """

# Total number of unread messages for all users

""" The number needed for the answer is buried in a string in the key['greeting'].
A function needs to be created to extract the digits from the string. """

greetings = [profile['greeting'] for profile in profile_data]
def extract_digits(s):
    return int(''.join([c for c in s if c.isdigit()]))
n_unread_messages = [extract_digits(greeting) for greeting in greetings]
sum(n_unread_messages)
