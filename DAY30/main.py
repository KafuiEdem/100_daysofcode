import email
import json
def find_password():
    word = 'Amazon'

    with open("DAY29/project_day29/data.json",'r') as fp:
        data = json.load(fp)
    for i in data:
        if word == i:
            c = data[i]
            print(c['email'],c['password'])

find_password()