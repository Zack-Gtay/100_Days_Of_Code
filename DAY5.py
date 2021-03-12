import random
import string
fruits = ["Apples", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

#PART I
student_heights = input("Input a list of student heights: ").split()
number_of_Students = 0
total = 0
for n in student_heights:
    total += int(n)
    number_of_Students += 1

print(f"There are a total of {number_of_Students} heights in student_heights!")
print(f"Total: {total}")
print(f"Average height rounded to the nearest whole number = {round((total/len(student_heights)),2)}")


#PART II
# HIGHER SCORE PROB

student_scores = input("Input a list of student score: ").split()



highest_score = student_scores[0]
for n in range(0, len(student_scores)):
    if student_scores[n] > highest_score:
        highest_score = student_scores[n]

print(f"The highest score in the class is: {highest_score}")



# PART III

total = 0
for number in range(1, 101):
    total += number
print(total)

# Adding Evens prob

#Method 1
sum = 0
for number in range(0, 101, 2):
    print(number)
    sum += number
print(sum)

#Method 2
sum2 = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum2 += number
    else:
        continue
print(sum2)


# PART IV
#Fizz Buzz problem


for number2 in range(1, 101):
    if number2 % 3 == 0 and number2 % 5 == 0:
        print("FIZZBUZZ")
    elif number2 % 5 == 0:
        print("BUZZ")
    elif number2 % 3 == 0:
        print("FIZZ")

    else:
        print(number2)

#PART V
# PASSWORD GENERATOR PROJECT
print("WELCOME TO PASSWORD GENERATOR :) ")
num_of_letters = int(input("How many letters would you like in your password?"))
num_of_symbols = int(input("How many symbols would you like? "))
num_of_numbers = int(input("How many numbers would you like? "))

letters = ['a', 'B', 'c', 'd', 'e', 'F', 'g', 'h', 'i', 'j', 'K', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'W', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_generated = []
for i in range(1, num_of_letters + 1):
    password_generated.append(random.choice(letters))


for i in range(1, num_of_numbers + 1):
    password_generated.append(random.choice(numbers))

for i in range(1, num_of_symbols + 1):
    password_generated.append(random.choice(symbols))
random.shuffle(password_generated)

password = ""
for char in password_generated:
    password += char
print(f"Your password is {password}")