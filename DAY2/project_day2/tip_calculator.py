""" 
This is the final project for day 2.
This is a tip calculator that calculate tip and share it among a number 
of person and give them the bill.
"""
banner = "Welcome to the tip calculator."
print(banner)
tip_input = input("What was the total bill? $")
tip_percentage = input("what percentage tip would you like to give? 10, 12, or 15? ")
num_of_persons = input("How many people to split the bill? ")

#calculate tip percentage 
tip_per = ((int(tip_percentage)/100)*float(tip_input))
total_percentage = tip_per + float(tip_input)
#calculate number of person to pay tip
num_tip_pay = total_percentage / int(num_of_persons)
total = f"Each person should pay: ${round(num_tip_pay,2)}"
print(total)
