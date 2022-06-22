from hangman_art import * #to import all the contents 
from hangman_words import word_list
import random
from os import system, name

#defining a clear function to clear the output in terminal after each iteration
def clear():
    if name == 'nt': #for windopws os
        _ = system('cls')
    else:
        _ = system(clear) #for macand linux os

end_game = False
chances = 6
print(logo)
word_picked= random.choice(word_list)
word_length = len(word_picked)
print("pssst... picked word is:", word_picked)

#initialising an empty list where user letters will be appended
display = []
for _ in range(word_length):
    display += "_" #appending blanks to the empty list

while not end_game:
    user_guess = input("Guess a letter: ").lower()
    clear()

    if user_guess in display:
        print(f"guessed letter {user_guess} is already picked. Guess a new letter")
    #to check the position of each letter in the word-picked
    for position in range(word_length):
        letter = word_picked[position]

        #to check if the guessed letter mactches letter in  the picked word
        if user_guess == letter:
            display[position] = letter
            print("You guessed the letter.")

    if user_guess not in word_picked:
        print(f"Guessed letter {user_guess} not in the picked word. You loose a life.")
        chances -= 1
        print("Remaining chances: ", chances)

        if chances == 0:
            end_game = True
            print("You loose.")
    print(f"{' '.join(display)}")  #converting a list to a string and joining the letters.

    if '_' not in display:
        end_game = True
        print("You guessed the word right. You win!!")
    
    print(stages[chances]) #printing stages art using chances as index
        




    














 


