from game_data import data
from art import logo,vs
import random
import os

clear = lambda:os.system('clear')

print(logo)
score = 0
check_pay = True
def format_person(person):
    """ This function to format all the names from our database"""
    person_name = person['name']
    person_descr = person['description']
    person_country = person['country']
    
    return f"{person_name}, a {person_descr}, from {person_country}"

def check_correct_answer(user_input,person_a_follower,person_b_follower):
    if person_a_follower > person_b_follower:
        return user_input =='a'
    else:
        return user_input =='b'

person_b = random.choice(data)

while check_pay:
 
    person_a = person_b
    person_b = random.choice(data)
    
    while person_a == person_b:
        person_b = random.choice(data)


    A =format_person(person_a)
    B= format_person(person_b)


    print(f"Compare A: {A}")
    print(vs)
    print(f"Against B: {B}")
    
    person_a_follower = person_a['follower_count']
    person_b_follower = person_b['follower_count']
    #Ask user to guess who has more follow
    user_input = input("Who has more follower? Type 'A' or 'B': ").lower()
  
    is_correct = check_correct_answer(user_input=user_input,person_a_follower=person_a_follower,person_b_follower=person_b_follower)
    clear()
    print(logo)
    
    if is_correct:
        score+=1
        print(f"You are correct, your current score is {score}")
      
    else:
        check_pay =False
        print(f"You are wrong, your final score is {score}")
        