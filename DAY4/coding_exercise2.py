import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_seed = random.randint(0,len(names))

if test_seed < names_seed -1:
    print("Members are more the seed")
else:
    msg = f"{names[names_seed -1]} is going to buy the meal today!"
    print(msg)

#edem,john,mark,paul,mike