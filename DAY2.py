#PART I
print("123" + "345")
num_char = len(input("Enter your name: "))
new_num_char = str(num_char)
print("Your age has " + new_num_char + " characters.")

a = str(123)
print(type(a))
b = float(123)
print(type(b))

# PART II
#printing
print(str(123) + str(100))

two_digit_numbers = input("Type a two digit number: ")
result = int(two_digit_numbers[0]) + int(two_digit_numbers[1])
print(result)

#MBI
height = input("Enter your height in m: ")
weight = input("Enter your weight in Kg: ")


# PART III
BMI = float(weight) / float(height) ** 2
print(int(BMI))

print(6//3)
print(round(8 / 3))
print(round(8 / 3, 2))


# PART IV
age = input("Enter your age: ")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining  * 365
weeks_ramaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {years_remaining} years, {days_remaining} days, {weeks_ramaining} weeks, {months_remaining} months left")

# PART V (LAST)
# Paying bills program

bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay €{final_amount}")

