money = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. CALCULATING THE IF THE MONEY IS ENOUGH.
# TODO 2. CHECKING IF THERE ARE ENOUGH RESOURCES
# TODO 3. UPDATE THE RESOURCES
# TODO 4. GENERATING A REPORT


def is_resources_sufficient(drink):
    coffee = MENU[drink]
    for resource in resources:
        if coffee['ingredients'][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True


def process_coins():
    """ Accepts money from users and returns the total result"""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def make_coffee(user_input, profit):
    coffee = MENU[user_input]
    for ingredient in coffee["ingredients"]:
        resources[ingredient] -= coffee['ingredients'][ingredient]
    global money
    money += profit
    change = profit - coffee["cost"]
    print(f"Here is ${change} in change")


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")

    else:
        if is_resources_sufficient(choice):
            user_money = process_coins()
            if user_money >=  MENU[choice]["cost"]:
                make_coffee(choice, user_money)
            else:
                print("Sorry that's not enough money")
""" Enjoy your coffee"""

























