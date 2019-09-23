def is_two(x):
    if x == 2 or str(2):
        return True
    else:
        return False

# Define a function named is_two. It should accept one input
# and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == str(2):
        return True
    else:
        return False

print(is_two(3))
#
# # Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    x = str(x)[:0].lower()
    if x in "aeiou":
        return True
    else:
        return False

print(is_vowel('ab'))

# # Define a function named is_consonant.
# # It should return True if the passed string is a consonant, False otherwise.
# # Use your is_vowel function to accomplish this.
#
#
def is_consonant(x):
    if str(x)[0:].strip().lower() not in "aeiou":
        return True
    else:
        return False

print(is_consonant('ba'))

# # Define a function that accepts a string that is a word.
# # The function should capitalize the first letter of the word
# # if the word starts with a consonant.
#
#
def cap_a_word(x):
    x = str(x).lower()
    if x[0] not in "aeiou":
        return x.capitalize()
    else:
        return "Does not start with a consonant"


print(cap_a_word("awords"))
#
# # Define a function named calculate_tip.
# # It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
#
#
def calculate_tip(bill_total, tip_percentage):
    tip_percentage = tip_percentage/100
    tip_amount = bill_total * tip_percentage
    return "The tip amount is: " + '$' + str(round(tip_amount, 2))


# print(calculate_tip(34.95, 20))
#
# # Define a function named apply_discount. It should accept a original price,
# # and a discount percentage, and return the price after the discount is applied.
#
def discount_amount(initial_total, discount_percentage):
    discount_percentage = discount_percentage/100
    discount_total = initial_total * discount_percentage
    total_bill = initial_total - discount_total
    return "The price after discount is: " + '$' + str(round(total_bill, 2))

print(discount_amount(67.42, 13))

# # Define a function named handle_commas.
# # It should accept a string that is a number that contains commas in it as input,
# # and return a number as output.
#

def handle_commas(x):
   return float(x.replace(',', ''))
    

print(handle_commas('1,234,567.95'))


# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(num_grade):
    num_grade = int(num_grade)
    if num_grade >= 96:
        return 'A+'
    elif num_grade < 96 and num_grade >= 92:
        return 'A'
    elif num_grade < 88 and num_grade >= 86:
        return 'B+'
    elif num_grade < 86 and num_grade >= 83:
        return 'B'
    elif num_grade < 83 and num_grade >= 80:
        return 'B-'
    elif num_grade < 80 and num_grade >= 75:
        return 'C+'
    elif num_grade < 74 and num_grade >= 70:
        return 'C'
    elif num_grade < 70 and num_grade >= 66:
        return 'C-'
    elif num_grade < 66 and num_grade >= 64:
        return 'D+'
    elif num_grade < 64 and num_grade >= 62:
        return 'D'
    elif num_grade < 62 and num_grade >= 60:
        return 'D-'
    else:
        return 'FFFFFFFFFFFFFFFFFFFFaaaaiiiiilllll'


print(get_letter_grade(67))


# Define a function named remove_vowels that
# accepts a string and returns a string with all the vowels removed.


def remove_vowels(word):
    new_word = word
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in word.lower():
        if x in vowels:
            new_word = new_word.replace(x, "")

    return new_word


print(remove_vowels("David Espinola looks like an $%&^("))


# Define a function named normalize_name. It should accept a string and
# return a valid python identifier, that is:
#
# anything that is not a valid python identifier should be removed
#
# leading and trailing whitespace should be removed
#
# everything should be lowercase
#
# spaces should be replaced with underscores
#     for example:
#     Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(x):
    new_word = x
    if x.isdigit() == False and x.isidentifier() == False and x.isspace() != False:
        new_word = x.replace(x, "")

    new_word = new_word.lower().replace(" ", "_")

    return new_word


print(normalize_name(' Ho$w@dy Dud@e&y'))

# Write a function named cumsum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.

def cum_sum(lst):
    total = 0
    new_lst = []
    for num in lst:
        total += num
        new_lst.append(total)
    return new_lst

print(cum_sum([1,2,3,4]))


def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:

    # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

print(convert24("08:05:45 PM"))

