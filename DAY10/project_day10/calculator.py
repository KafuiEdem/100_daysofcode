import os
from art import logo

clear = lambda:os.system('clear')


#Calculator 

def add(n1,n2):
    return n1 + n2 

#subtract 
def subtract(n1,n2):
    return n1 - n2

#Multiply 
def multiply(n1,n2):
    return n1 * n2 

#Divid 
def divid(n1, n2):
    return n1 / n2 

operations = {

    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divid,
}
print(logo)
def calculator():
    
    flag = True
    answer = ''
    num1 = float(input("What's the first number?: "))


    while flag:

        operations_symbol = input("Pick an operation : ")
        num2 = float(input("What's the second number?: "))

        for symbol in operations:
            print(symbol)

        calculate_function = (operations[operations_symbol])
        answer = calculate_function(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        keep_cal = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation: ")

        if keep_cal =='y':
            num1 = answer
        else:
            flag = False
            clear()
            calculator()

calculator()
