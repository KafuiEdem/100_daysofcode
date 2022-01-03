"""
    This is day is on datatype.
    To see the datatype you are working with, than you can use the type() function.
    The type function will shows you the type of data you are dealing with.
    This help to check the datatype.
    
    You can also you type casting to convert a datatype o another datatype.
"""
"""
#Assignment 1
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num_split = int(two_digit_number[0]) + int(two_digit_number[1])
print(num_split)
"""

"""
 PEMDAS
    ()
    **
    */
    +-
"""

"""
ASSIGNMENT 2
    import math
    # 🚨 Don't change the code below 👇
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    squ_h = float(height)**2
    cal =  float(weight)//(squ_h)
    print(int(cal))
"""

"""
    In python you an use round to round function decimals.
    The round can take two element thus round(num,number of decimals to round to)
    you can also round a number using (//).
"""

""""
ASSIGNMENT 3

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ls = 90
ls_day = ls * 365
day = ls_day - (365 * int(age))
week = (ls * 52) - int(age)*52
month = (ls * 12) - int(age)*12

final_out = f"You have {day} days, {week} weeks, and {month} months left."
print(final_out)
"""