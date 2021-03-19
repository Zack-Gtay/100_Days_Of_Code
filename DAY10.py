# FUNCTIONS WITH OUTPUTS
# CALCULATOR DAY
import ArtDay10
def format_name(f_name, l_name):
    # if f_name == "" or l_name = "":

    formatted_name = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_name} {formatted_lname}"


print(format_name(input("What is your name? "), input("what is your last name? ")))


# LEAP YEAR
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap_year(year) and month == 2:
        return 29
    return month_days[month]

year = int(input("Enter year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

print("-------------------------------------")
print("-------easy calculator--------".upper())
print(ArtDay10.logo)
print("-------------------------------------")
def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

should_continue = True
while should_continue:
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]

    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit") == "y":
        num1 = answer
    else:
        should_continue = False
