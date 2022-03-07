# write to file
def write_letter_to_file(name,letter):
    with open(f"DAY24/project_day24/Mail-Merge-Project-Start/Output/ReadyToSend/letter_for_{name}.txt",mode='w') as data:
        data.write(letter)

# read every name from the invited names

with open("DAY24/project_day24/Mail-Merge-Project-Start/Input/Names/invited_names.txt") as data:
    each_name = data.readlines()


# reade the starting letter from the latter text file
with open("DAY24/project_day24/Mail-Merge-Project-Start/Input/Letters/starting_letter.txt") as data:
    new_letter = data.read()


#loop through the names and insert it to the latter.

for name in each_name:
    c =new_letter.replace('[name]',name.strip())
    write_letter_to_file(name,c.replace('Angela','Edem'))
    


