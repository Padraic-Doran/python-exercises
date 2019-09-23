

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]



# Exercise 1 - rewrite the above example code using list comprehension syntax. \
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]


uppercased_fruits = [fruit.upper() for fruit in fruits]

print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like
# ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.

def is_vowel(character):
    vowels = "AEIOUaeiou"
    if character in vowels:
        return True
    else:
        return False


print(is_vowel("R"))

def v_count(word):
    count = 0
    for character in word:
        if is_vowel(character):
            count += 1
    return count

print(v_count("Banana"))

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if v_count(fruit) > 2]

print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [fruit for fruit in fruits if v_count(fruit) == 2]

print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters


fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]

print(fruits_with_more_than_five_characters)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruits_with_five_characters = [fruit for fruit in fruits if len(fruit) == 5]

print(fruits_with_five_characters)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]

print(fruits_with_less_than_five_characters)



# Exercise 8 - Make a list containing the number of characters in each fruit.
# Output would be [5, 4, 10, etc... ]


characters_in_fruit_name = [len(fruit) for fruit in fruits]

print(characters_in_fruit_name)

# Exercise 9 - Make a variable named fruits_with_letter_a
# that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]

print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [number for number in numbers if number % 2 == 1]

print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [number for number in numbers if number > 0]

print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if number < 0]

print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce
# a list of numbers with 2 or more numerals
two_or_more_numerals = [number for number in numbers if abs(number) >= 10]

print(two_or_more_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared.
# Output is [4, 9, 16, etc...]

numbers_squared = [number ** 2 for number in numbers]

print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers
# that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]

print(odd_negative_numbers)



# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.


numbers_plus_five = [number + 5 for number in numbers]

print(numbers_plus_five)
