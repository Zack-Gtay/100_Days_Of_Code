from turtle import Turtle, Screen
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")

#timmy.color("coral")
#timmy.forward(100)
#timmy.left(90)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

#table = PrettyTable()
#new_city = "CasaBlanca"
#
#table.add_column("Type", [f"{new_city}", "Water", "Fire"])
#table.add_column("Website", ["Pikachu", "Squirty", "Charmander"])
#
#table.align = "l"
#print(table)


# COFFEE MAKER OBJECT
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?: {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



