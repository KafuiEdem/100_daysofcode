import pandas

data = pandas.read_csv('DAY26/project_day26/nato_phonetic_alphabet.csv')
# print(type(h))

phonetic_dic = {v.letter:v.code for (k,v) in data.iterrows()}
print(phonetic_dic)
#TODO 1. Create a dictionary in this format:


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

check_expection = True
while check_expection:
    
    user_input = list(input('Enter a word : ').title())
    try:
        nato_word = [phonetic_dic[n.upper()] for n in user_input ]
    except KeyError:
        print("Sorry  oly letters in the alphabet please")

    else:
        print(nato_word)
        check_expection = False
