
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text,shift_amount,chiper_direction):
    chiper_msg = ''
    if chiper_direction =='decode':
        shift_amount *=-1    
    for char in plain_text:
        if char in alphabet:
            position_num = alphabet.index(char)
        
            shift_text = position_num + shift_amount
            chiper_msg +=alphabet[shift_text]
        else:
            chiper_msg +=char
    
    print(f'The {chiper_direction}d text is {chiper_msg}')

flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
            
    shift %=26

    caesar(plain_text=text,shift_amount=shift,chiper_direction=direction)
    check_user_respons = input('Type yes to continue, otherwise type no to end: ')
    if check_user_respons =="no":
        flag = False
    print('Enjoy your day')