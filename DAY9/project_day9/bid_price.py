import os

from art import logo

clear = lambda:os.system('clear')

print(logo)



user_db = {}
def add_user_to_db(name,bid):
    user_db[name] = bid

def try_again():
    other_bider =input("Are there any other bidders?: yes or no: ")
    return other_bider
bid_again = True
while bid_again:

    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: "))

    add_user_to_db(name=user_name,bid=user_bid)
    other_bider =try_again()
    
    if other_bider =='no':
        high = max(user_db,key=user_db.get)
        msg = f" The winner is {high} with a bid of ${user_db[high]}"
        clear()
        print(msg)
        bid_again = False
    elif other_bider == 'yes':
        clear()
    else:
        print("Please Type yes or no ")
        bid_again = False
        

