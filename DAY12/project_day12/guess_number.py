import imp
import random
from art import logo

#logo
print(logo)
#This part contain all the variable needed for the game.
computer_guess= []
hard = 5
easy = 10
check_game = True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")


def numbers_list(l):
    """ This function generate range of 
        numbers from 1 to 100 and append the
        generated number to a list
    """
    for i in range(1,101):
        l.append(i) 

def computer_think_number(list):
    """ This function produce random numbers from a list and 
        return the random generated number
    """
    secret_number =  random.choice(list)
    return secret_number

numbers_list(computer_guess)

computer_secrete_guess = computer_think_number(computer_guess)
game_level=input("Chose a difficulty. Type (h ='hard') OR Type (e ='easy'): ")



while check_game:

    #this part inform the player the number of attempt left.
    if game_level =='h':
        print(f"You have {hard} attempt to guess the number")
    else:
        print(f"You have {easy} attempt to guess the number")
    user_guess = int(input("Make Guess: "))

    #This is the game logic
    if user_guess > computer_secrete_guess:
       
        print('Too high')
        print("Guess again.")
        
    elif user_guess < computer_secrete_guess:
      
        print('Too low')
        print("Guess again.")  
    elif user_guess == computer_secrete_guess:
        print(f"You got it!. The answer was {computer_secrete_guess}")
        check_game = False
    
    #This part checks if the player has choose the easy level
    if game_level == 'e':
        if user_guess > computer_secrete_guess or user_guess < computer_secrete_guess:
            easy -=1
            
        if easy == 0:
            check_game = False
            print("You've run out of guesses")
    
    #This part checks if the player has chose the hard level
    elif game_level =='h':
        if user_guess > computer_secrete_guess or user_guess < computer_secrete_guess:
            hard -=1
           
        if hard == 0:
            check_game = False
            print("You've run out of guesses")
            
    
