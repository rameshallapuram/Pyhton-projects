from data import *


def ingredients_available(order_ingredients):
    """Checks if the resources are sufficient to process the order"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! Insufficient {item}. Can't process your order for {choice}.")
            return False
    return True


def add_coins():
    """ returns total for the added coins"""
    total = 0
    print("Please enter the coins.")
    total += int(input("No. of quarters: "))*0.25
    total += int(input("No. of  dimes: "))*0.10
    total += int(input("No. of nickles: "))*0.05
    total += int(input("No. of pennies: "))*0.01
    return total


def payment_successful(money_added, drink_cost):
    """Returns true if payment is successful"""
    if money_added >= drink_cost:
        change = round(money_added - drink_cost, 2)
        print(f"Please collect {change}$ in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Insufficient coins inserted. Please collect your coins and try again.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deducts resources and processes order"""
    for items in drink_ingredients:
        resources[items] -= drink_ingredients[items]
    print(f"Here's your {drink_name}. Enjoy and have a good day!")


profit = 0
machine_on = True
while machine_on:
    choice = input("What would you like to have? espresso/latte/cappuccino: ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}gm.")
        print(f"Total amount: {profit}$")
    else:
        drink = MENU[choice]
        if ingredients_available(drink['ingredients']):
            payment = add_coins()
            if payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


































