from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


check_machine = True
make_drink = CoffeeMaker()
add_money = MoneyMachine()
menu = Menu()

def get_cost(item,drinks):
    for items in item:
        if drinks in items.name:
            return items.cost


while check_machine:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    
    
    if user_input == "off":
        check_machine = False
    elif user_input =="report":
        make_drink.report()
        add_money.report()
      
    else:
        drink = menu.find_drink(user_input)
        if make_drink.is_resource_sufficient(drink):
            payment = get_cost(menu.menu,drinks=user_input)
            if add_money.make_payment(payment):
                make_drink.make_coffee(drink)
            