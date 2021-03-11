import random
 # PART I
random_integer = random.randint(1, 10)
print(random_integer)

#Random decimal number between 0 and 5
random_float = random.random() * 5
print(round(random_float))

# PART II

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


states_of_america = ["Delawarw", "pebbsylvania","New jersey", "Georgia", "Connecticut", "Maryland","Rhode Island","Vermont","Kentucky", "Tennessee","Pregon"]
print(states_of_america[-1])
states_of_america[0] = "Illinois"
print(states_of_america)
states_of_america.append("Alabama")
print(states_of_america)
states_of_america.extend(["Angelaland", "New Mexico"])
print(states_of_america)



# PART III
#Yaaaa who will pay today's meal?
names_string = input("Give me eveybody's name, separated by a comma.")
names = names_string.split(", ")
name_randomly = random.choice(names)
print(f"{name_randomly} will pay today's meal :)")

# PART IV

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
Vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, Vegetables]
print(dirty_dozen)


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you wanna put the Treasure? XY: ")
X = int(position[0]) - 1
Y = int(position[1]) - 1
print(X, Y)
map[X][Y] = "X"
print(f"{row1}\n{row2}\n{row3}")

# PART V

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors"))
comp_choice = random.choice(choices)
print(f"You chose {choices[user_choice]}\n Computer chose {comp_choice}" )
if choices[user_choice] == rock and comp_choice == scissors:
    print("You win!!")
elif choices[user_choice] == scissors and comp_choice == paper:
    print("You win!!")
elif choices[user_choice] == paper and comp_choice == rock:
    print("You win!!")
elif choices[user_choice] == comp_choice:
    print("It's a draw")
else:
    print("You lose :(")

