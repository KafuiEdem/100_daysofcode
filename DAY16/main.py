# from turtle import  Turtle, Screen
# timmy = Turtle()

# timmy.shape('turtle')
# timmy.color('red','green')
# timmy.fd(100)

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",['Pikachu','Squirtle','Chamander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align ='l'

print(table)