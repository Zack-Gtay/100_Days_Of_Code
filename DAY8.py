# FUNCTIONS WITH INPUTS
# ARGUMENTS & PARAMETERS
import math

#Simple function
def greet():
    print("Hello Zack")
    print("How do you do Jack Bauer")
    print("Isn't the weather nice today?")
greet()

#Function that allows for input (parameter/Argument)
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
greet_with_name("Billie")

#Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Anna", "Nowhere")

# Positional argument
greet_with("Nowhere", "Anna")

# Function with Keyword arguments
greet_with(location="Nowhere", name="Anna")

#PAINT AREA CALCULATOR
def point_calc(height, width, cover):
    num_of_cans = (height * width)/cover
    print(f"You'll need {math.floor(num_of_cans)} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
point_calc(height=test_h,  width=test_w, cover=coverage )



#PRIME NUMBER
def prime_checker(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
    if flag:
        print("It's prime number.")
    else:
        print("It's not prime number!.")


n = int(input("Check this number: "))
prime_checker(number=n)




alphabet = ["a","b","c","d","e","f","g","o","h","i","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"]
def encode(text_to_encode, shift_num):
    cipher_text = []
    for letter in text_to_encode:
        position = alphabet.index(letter)
        new_position = position + shift_num
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(cipher_text)


def decode(text_to_decode, shift_num):
    cipher_text_decoded = []
    for letter in text_to_decode:
        position = alphabet.index(letter)
        new_position = position - shift_num
        new_letter = alphabet[new_position]
        cipher_text_decoded += new_letter
    print(cipher_text_decoded)



count = 1
while count:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))
    if direction == "encode":
        encode(text_to_encode=text, shift_num=shift_number)
    else:
        decode(text_to_decode=text, shift_num=shift_number)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if repeat == "yes":
        count = 1
    else:
        count = 0
































