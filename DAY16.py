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

my_menu = Menu()
print(my_menu.get_items())
print(my_menu.find_drink("latte"))
print(my_menu.find_drink("cappuccino"))
#menu_items = MenuItem()
#print(menu_items)
 
make_coffee = CoffeeMaker()
print(make_coffee.report())
print(make_coffee.make_coffee("Latte"))
