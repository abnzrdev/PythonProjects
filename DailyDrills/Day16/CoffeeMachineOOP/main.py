from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create an object named menu
menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()
available_items = menu.get_items() # getting the available items
drink_counter = 0
maint_count = 0
MAINTENANCE_TOGGLE = 2

def maintenance():
    global maint_count
    print("The machine is in maintenance mode")

while True:
    user_input = input(f"What do you want ({available_items}): ")
    # Serving the customer
    if user_input == "off":
        print("GoodBye👋")
        break

    elif user_input == "report":
        coffee.report()
        money.report()
        print(f"Number of drinks are {drink_counter}")
        continue

    elif user_input == "maintenance":
        maint_count += 1
        if maint_count % MAINTENANCE_TOGGLE == 1:
            print("The machine is in maintenance mode.")
        else:
            print("The machine is out of maintenance mode")
        continue

    elif maint_count % 2 == 0:
        drink = menu.find_drink(user_input)
        if not drink:
            continue

        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
            drink_counter += 1

    else:
        maintenance()
        continue