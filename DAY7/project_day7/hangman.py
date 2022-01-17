import imp
import random
import os
import hangman_words
import hangman_art


clear = lambda:os.system('clear')
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
check_num = False

#this are the stages for the UI
stages = hangman_art.stages


lives = 6

logo = hangman_art.logo
print(logo)

display = []
for each_letter in chosen_word:
    u =  "_"*len(each_letter)
    display.append(u)


while not check_num:
    guess = input("Guess a letter: ").lower()
    
    clear()
  

    for possition in range(word_length):
        
        letter = chosen_word[possition]
        if letter == guess:
            display[possition] = letter
       

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            check_num = True
            print('You lose')

    print(f"{' '.join(display)}")

   
    if '_' not in display:
        check_num = True
        print('you won')

    live_remaining = f"{stages[lives]}"
    print(live_remaining)
   