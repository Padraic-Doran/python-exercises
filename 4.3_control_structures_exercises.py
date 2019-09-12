# # Conditional Basics
# #
# # prompt the user for a day of the week, print out whether the day is Monday or not
# #
# # prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# #
# # create variables and make up values for
# #
# # the number of hours worked in one week
# # the hourly rate
# # how much the week's paycheck will be
# # write the python code that calculates the weekly paycheck.
# # You get paid time and a half if you work more than 40 hours
#
day_of_week = input("Enter a day of the week: ")
if day_of_week in ["Monday"]:
    print("It's Monday my dudes")
else:
    print("It is not Monday, my dudes")

weekend_or_not=input("Enter a day of the week")
if weekend_or_not in ['Saturday','Sunday']:
    print("It's the weekend!,Let's party")
else:
    print("Sorry it's a workday")


hours_worked = 50
hourly_rate = 12


if hours_worked < 40:
    paycheck = hours_worked * hourly_rate

else:
    paycheck = (hours_worked - 40)* (1.5*hourly_rate) + (40 * hourly_rate)

print("This week's rubberband bank will be" , "$", paycheck)

i=5
while i<=15:
    print(i)
    i+=1


for i in range(0,101,2):
    print(i)


for i in range (100,-10,-5):
    print(i)


i=2
while i**2<1000000:
    i=i**2
    print(i)


for i in range(100,0,-5):
    print(i)


num =input("Enter a number")
num =int(num)
for i in range(1,11):
    print(str(num) + '*' + str(i) + "=" + str(num * i))


for num in range(1,11):
    print(str(num)*num)

odd_num = ""
while True:
    odd_num = input("Gimme dat number! ")
    if odd_num.isdigit() and int(odd_num) % 2 == 1 and int(odd_num) > 1 and int(odd_num)<50:
        break
for i in range(1,50,2):
    if i == int(odd_num):
        print("You're number is lame sauce. Skipping " + str(i))
        continue
    print("Here is a better odd number than yours: " + str(i))



pos_num = ""
while True:
    pos_num = input("Gimme a positive number: " )
    if pos_num.isdigit() and int(pos_num) > 0:
        break
for i in range(1, int(pos_num) + 1):
    print(i)


pos_num = ""
while True:
    pos_num = input("Gimme a positive number: " )
    if pos_num.isdigit() and int(pos_num) > 0:
        break
for i in range(int(pos_num),0,-1):
    print(i)

for n in range (1,101):
    if n % 3 == 0 and n % 5 ==0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)



go_again = True
while go_again:
    number = []
    squared = []
    cubed = []
    num = ""
    num = input("Please enter a number: ")
    print('Here we go')
    print("{:7s}| {:9s}| {:5s}".format('number ', 'squared ','cubed'))
    print("{:7s}| {:9s}| {:5s}".format('------', '-------', '-----'))
    for num in range(int(num) + 1):
        number.append(num)
        squared.append(num ** 2)
        cubed.append(num ** 3)
        print("{:<7}| {:<9}| {:<5}".format(number[num], squared[num], cubed[num]))

    go_again = input('Wanna keep this training rolling? Y/N: ').upper() == "Y"


while True:
    num_grade=input("Please enter a grade between 0 and 100: ")
    num_grade=int(num_grade)
    if num_grade >=96:
        print('A+')
    elif num_grade <96 and num_grade >=92:
        print('A')
    elif num_grade <88 and num_grade >=86:
        print('B+')
    elif num_grade <86 and num_grade >=83:
        print('B')
    elif num_grade <83 and num_grade >=80:
        print('B-')
    elif num_grade <80 and num_grade >=75:
        print('C+')
    elif num_grade <74 and num_grade >=70:
        print('C')
    elif num_grade <70 and num_grade >=66:
        print('C-')
    elif num_grade <66 and num_grade >=64:
        print('D+')
    elif num_grade <64 and num_grade >=62:
        print('D')
    elif num_grade <62 and num_grade >=60:
        print('D-')
    else:
        print('FFFFFFFFFFFFFFFFFFFFaaaaiiiiilllll')
    prompt_user_continue=input("Would you like to continue? Y/N: ")
    if prompt_user_continue.upper() == "N":
        break


book_list=[{'title':"Nudge",'author':"Richard Thaler",'genre':"Economics"},
           {'title':"Justice",'author':"Michael Sandel",'genre':"Philosophy"},{'title':"Extreme Discipline",'author':"Jocko Willink",'genre':"Business"},{'title':"The Outpost",'author':"Jake Tapper",'genre':"War"}]
for book in book_list:
    print("The book title is: "+book['title'])
    print("The book author is: "+book['author'])
    print("The book genre is: "+book['genre'])


#Exercise 6.a
genre_filter=input("Please enter a genre: ")
for book in book_list:
    if book['genre'] == genre_filter:
        print('The following are entries in your desired genre: ')
        print("The book title is: "+book['title'])
        print("The book author is: "+book['author'])