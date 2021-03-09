# PART I
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#-----------------------------------------------------------------------

#PART II (Nested if/else)
print("--------------------------------------------")

height = int(input("Enter your height in cm : "))
if height >= 120:
    print("You can ride!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age < 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")
    wants_photos = input("Do you want photos? (Y or N) ")
    if wants_photos == 'Y':
        print(f"Your total bill is: ${bill + 3}")
    else:
        print(f"Your total bill is: ${bill}")
else:
    print("You can't ride!")
print("--------------------------------------------")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight / (height * height)
if BMI < 18.5:
    print(f"Your BMI is {round(BMI,2)}, and you're underweight!")
elif BMI >=18.5 and BMI < 25:
    print(f"Your BMI is {round(BMI,2)}, and you have normal weight!")
elif BMI >=25 and BMI < 30:
    print(f"Your BMI is {round(BMI,2)}, and you're overweight!")
elif BMI >=30 and BMI < 35:
    print(f"Your BMI is {round(BMI,2)}, and you're obese!")
else:
    print(f"Your BMI is {round(BMI,2)}, and you're clinically obese!")

#-----------------------------------------------------------------------
# PART III
#CHECK LEAP YEAR
print("--------------------------------------------")

year = int(input("Which year do you want to check? "))
if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year!")
    else:
        print("This is a leap year.")

else:
    print("This is not a leap year!")

#-----------------------------------------------------------------------
#PART IV
print("--------------------------------------------")
print("    WELCOME TO PYTHON PIZZA DELIVERIES!     ")
print("--------------------------------------------")

size = input("What size pizza do you want? S,M,L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extre cheese? Y or N ")
price = 0
if size == 'S':
    price += 15
elif size == 'M':
    price += 20
else:
    price += 25

if add_pepperoni == 'Y':
    if size == 'M':
        price += 2
    else:
        price += 3
if extra_cheese == 'Y':
    price += 1

print(f"Your final bill is ${price}")


#PART IV
print("--------------------------------------------")
print("    Welcome to the LOVE calculator Game     ")
print("--------------------------------------------")

name1 = input("What's your name? \n".lower())
name2 = input("What's their name? \n".lower())
combined_names = name1 + name2
total_t = combined_names.count("t")
total_r = combined_names.count("r")
total_u = combined_names.count("u")
total_e = combined_names.count("e")
total_true = total_t + total_r + total_u + total_e

total_l = combined_names.count("l")
total_o = combined_names.count("o")
total_v = combined_names.count("v")
total_v = combined_names.count("e")
total_love = total_l + total_o + total_v + total_e

love_score = int(str(total_true) + str(total_love))
print(love_score)
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos LOL! ")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")



# PART VI
#Choose your own adventure Game
print("---------------------------------------------\n")
print("---------------------------------------------")
print("------Welcome to the OWN ADVENTURE GAME------")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************

''')
print("---------------------------------------------")
print("Welcome to Treasure Island. Your mission is to find the treasure\n")
choice = input("You\'re at a crossroad, where do you want to go? Type 'LEFT' or 'RIGHT': ".lower())

if __name__ == '__main__':
    if (choice == "right"):
        print("You fell into a hole. GAME OVER!!")
    elif (choice == "left"):
        second_choice = input("You've come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat. Type 'swim' to swim across. ".lower())
        if (second_choice == "swim"):
            print("GAME OVER!!")
        elif (second_choice == "wait"):
            third_choice = input("What do you prefer to open, BLUE, RED or GREEN door?".lower())
            if (third_choice == "red") :
                print("GAME OVER!!")
            elif (third_choice == "blue") :
                print("GAME OVER!!")
            else:
                print("YAAAAAAAA YOU WIN!!!!")




