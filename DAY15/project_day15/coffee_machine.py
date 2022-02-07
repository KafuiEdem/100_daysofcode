from machine_data import  MENU, resources

cash = 0
check_machine = True


def is_more_resource(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_paid,drink_cost):
    if money_paid >= drink_cost:
        change = round(money_paid - drink_cost,2)
        print(f"Here is your change {change}")
        global cash
        cash +=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink,ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {drink}")
    
    return drink

while check_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input =='off':
        check_machine = False
    elif user_input =='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {cash}")
    else:
        drink = MENU[user_input]
        if is_more_resource(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(money_paid=payment,drink_cost=drink['cost']):
                make_coffee(user_input,drink["ingredients"])

