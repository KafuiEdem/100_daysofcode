banner = '''  

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
*******************************************************************************

 "Welcome to Tresure Island".
 Your mission is to find the treasure.
'''
print(banner)
rf = "You fialed Game over"
win = "You Won!. You find the treasure."
lr = "A boat arrieve and gave you a ride to the treasure house"
gt = "You just wasted your life for no good reason shame on you. Looser, you died. Game Over"
score = 0
q1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n")
if q1 =="right":
    print(rf)
elif q1 =="left":
    q2 = input("Welcome to the river, do you want to swim or wait? Type 'swime' or 'wait'\n ")
    if q2 == "swime":
        print(rf)
        score +=1
    elif q2=="wait":
        print(lr)
        score +=1
        q3 = input("There are three door in the treasure house which one do you want to take? Type 'blue' or 'yellow' or 'red' ")
        if q3 =="red" or q3 =="blue":
            print(rf)
        elif q3 =="yellow":
            print(win)
            score +=1
    else:
        print(gt)
    
    score +=1
else:
    print(gt)

print("TOTAL SCORE: ",score)

