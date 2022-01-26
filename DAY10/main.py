#Functions with output.
""" 
    def my_function():
        DO this with something
        Than do this 
        Finally do this
we can than use the function by calling the function this way my_function()

You can also have a function that return something. That means the function can have an output.
"""


def format_name(f_name,l_name):
    """ This take a firstname and lastname and 
        convert it to a Title case.
    """
    if f_name =="" or l_name =="":
        return "You didn't provide a valid name"
    firstname = f_name.title()
    lastname = l_name.title() 
    return f"{firstname} {lastname}"

formated_string = format_name()
print(formated_string)