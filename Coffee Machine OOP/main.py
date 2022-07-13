from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"Enter your choice. ({options}): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


