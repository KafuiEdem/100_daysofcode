import random

""" 
    GAME RULES 
    Rock wins against scissors
    Scissors win against paper
    Paper wins against rock
"""
computer_choice = ['rock','paper','scissors']
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

com_random = random.randint(0,len(computer_choice))
index_m = com_random -1


rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

   """
paper = """  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scissors = """  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

#Human part
if player_input == 0 and index_m  ==2:
    print(scissors,"Computer Choice")
    print(rock,"Your Choice")
    #rock win
    print("You wins")
elif player_input ==2 and index_m ==1:
    print(scissors,"Computer Choice")
    print(paper,"Your Choice")
    #paper wins
    print("You wins")
    
elif player_input ==1 and index_m ==0:
    print(paper,"Computer Choice")
    print(rock,"Your Choice")
    #rock win
    print("You wins")

#Compuer part    
elif com_random == 0 and player_input ==2:
    print(rock,"Computer Choice")
    print(scissors,"Your Choice")
    
    #rock win
    print("You loose")
elif com_random  ==2 and player_input ==1:
    print(scissors,"Computer Choice")
    print(paper,"Your Choice")
    #paper wins
    print("You loose")
    
elif com_random ==1 and player_input ==0:
    print(paper,"Computer Choice")
    print(rock,"Your Choice")
    #rock win
    print("You loose")
elif player_input == index_m:
 print("Draw")
else:
    print("TRY AGAIN")