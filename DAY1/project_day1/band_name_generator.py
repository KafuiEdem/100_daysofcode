"""
    This project helps to generate a band name for you.
    It first ask of the city your grew up in, and 
    also asked for your pet's name. After that the program
    combines the city and pet name to generate your band name.
    
"""
banner = "Welcome to the Band Name Generator."
print(banner)
city = input("What's name of the city our grew up in?\n")
pet = input("What's your pet's name?\n")
name_generate = "Your band could be "+ city +" "+pet 

print(name_generate)