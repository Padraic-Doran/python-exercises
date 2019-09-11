# greeting = "Hi, you knuckle dragging caveman!"
# print(greeting)
#
#
# print(type(99.9))
#


# You have rented some movies for your kids:
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules
# (1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?


movie_rental = [{'Title': 'The Little Mermaid', 'Duration': 3, 'Price': 3},
                {'Title': 'Brother Bear', 'Duration': 5,'Price': 3},
                {'Title': 'Hercules', 'Duration': 1,'Price': 3}]

total_charge = 0

for movie in movie_rental:
    total_charge += movie['Duration'] * movie['Price']

print("Rental charges come to", '$', total_charge)

# Suppose you're working as a contractor for 3 companies:
# Google, Amazon and Facebook, they pay you a different rate per hour.
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
# How much will you receive in payment for this week?
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.


pay =[{'Company': 'Google', 'Pay': 400, "Hours Worked": 6},
{'Company': 'Amazon', 'Pay': 380, "Hours Worked": 4},
{'Company': 'Facebook', 'Pay': 350, "Hours Worked": 10}]

cash_money = 0

for company in pay:
    cash_money += company['Pay'] * company['Hours Worked']

print('My rubber band bank for the week is',' $', cash_money)


# Use the following code to follow the instructions below:
#
# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
#
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

password = input("please select a password:")
password = " "
While (len(password)) < 5 = True
print("Too short homie, make it longer")
input('please select a password:')
else:
    print("Too short homie, make it longer")
    input('please select a password:')

password_again = input("please re-type your password")
loop=raw_input("Password does not match. Please try again")
if password_again==password:
    print("password created")
else: input(loop)




