""" 
    This is a ticketing system for a rollercoaster
"""

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can't ride the rollercoaster ")
# else:
#     print("You can ride the rollercoaster.")

""" 
    Comparision operators
    
    ==
    <
    <
    We use this operators to compare items 
"""

""" 
    Exercise 1 (Odd or Even)
"""

# num = int(input("Enter a number: "))

# if num % 2 ==0:
#     print("Even number")
# else:
#     print("Odd number")

# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇

# bmi = round(weight / (height**2))

# if bmi < 18.5:
#     print("You are are underweight")
# elif bmi < 25:
#     print("You have a normal weight")
# elif bmi < 30:
#     print("You are slightly overweight")
# elif bmi < 35:
#     print("You are obese")
# else:
#     print("You are clinically obese.")


# 🚨 Don't change the code below 👇
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# leap_year = year % 4

# if year % 4 ==0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Leap year")
# elif year % 400 ==0:
#     print("Leap year")
    
# else:
#     print("Not leap year")


"""  
    Multiple If statment
    This type of condictional statment contains multiple if statment.
    The condiction will run when it turns out to be true.
    example:
           if a is true:
             run A
           if b is true:
             run B
           if c is true:
             run C
    This type of statment will run one after the other. 
"""


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >=120:
#     print("You can ride the rollercoaster ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Your ticket is ${bill}")
#     elif age <=18:
#         bill = 7
#         print("Your ticket is ${bill}")
#     else:
#         bill = 12
#         print("Adult ticket is ${bill}")
#     want_photo = input("Do you want a photo taken? Y or N.")
#     if want_photo == "Y":
#         bill +=3
#     print(f"Your final bill is ${bill}")
# else:
#     print("You can't ride the rollercoaster.")
    
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# bill = 0

# if add_pepperoni =="N":
#     if size =="S":
#         bill = 15
#     elif size =="M":
#         bill =20
#     elif size =="L":
#         bill = 25
#     if extra_cheese =="Y":
#         bill +=1
#     print(f"Your final bill is: ${bill}")
# else:
#     if size =="S":
#         bill = 15 + 2
#     elif size =="M":
#         bill =20 + 3
#     elif size =="L":
#         bill = 25 +3
#     if extra_cheese =="Y":
#         bill +=1
#     print(f"Your final bill is: ${bill}")

"""  
    LOGICAL OPERATORS
    {AND} =>   With this operator items to combine should be true to evalute it to be true.
    {OR} => this is use if you need only one statment to be true
    {NOT} => this reverse the condiction
"""
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >=120:
#     print("You can ride the rollercoaster ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Your ticket is ${bill}")
#     elif age <=18:
#         bill = 7
#         print("Your ticket is ${bill}")
#     elif age >=45 and age <=55:
#         bill = 0
#         print(f"You have a free ride ticket is ${bill}")
        
#     else:
#         bill = 12
#         print(f"Adult ticket is ${bill}")
#     want_photo = input("Do you want a photo taken? Y or N.")
#     if want_photo == "Y":
#         bill +=3
#     print(f"Your final bill is ${bill}")
# else:
#     print("You can't ride the rollercoaster.")

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
check_word1="true"
check_word2 ="love"
score1= 0
score2 = 0

combined_string = name1 + name2
for i in check_word1:
  n = combined_string.lower().count(i)
  score1 +=n 

for i in check_word2:
  n = combined_string.lower().count(i)
  score2 +=n
  
k = f"{score1}{score2}"
love_score = int(k)

if love_score <10 or love_score >90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >=40 and love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")


