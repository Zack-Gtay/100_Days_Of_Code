####### DEBUGGING #########


############# Describe Problem ############
# First VERSION
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()


# Second VERSION after debugging
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()


############## Reproduce the bug ##############
# First VERSION
from random import randint
dice_img = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)        # the problem is here; we have 6 items in the list but we start from index 0 so we have to increase by 1 randint(1, 5)
#print(dice_img[dice_num])


# Second VERSION after debugging
dice_img = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 5)
#print(dice_img[dice_num])


################## Play Computer ##############
# First VERSION
year = int(input("What'S your year of birth?: "))
if year > 1980 and year < 1994:
    print("You are a millenial")
elif year > 1994:
    print("You are a Gen Z")

# Second VERSION after debugging
year = int(input("What'S your year of birth?: "))
if year > 1980 and year < 1994:
    print("You are a millenial")
elif year >= 1994:
    print("You are a Gen Z")



################## Print is our friend ##############

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)



################## Use a Debugger ##############
# Online one http://pythontutor.com/visualize.html#mode=edit
# Or Thonny Editor

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 8, 14, 9])

# After debugging I find that b_list append just the last item in the list so I have to enter b_list.append(new_item) inside the for loop in that way it will add all the items multplied by 2
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 8, 14, 9])


################## Take a Break ##############
################## Ask a Friend ##############
################## Run Often ##############

# Exercice 1
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# Exercice 2
year = int(input("Which year do you want to check?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")

# Exercice 3
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)