import random
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("Welcome to the number guessing game!")
easy_level_attempts = 10
medium_level_attempts = 7
hard_level_attempts = 5

def game_level():
    
    level = input("Choose the difficulty level. easy or medium or hard: ").lower()
    if level == "hard":
        return hard_level_attempts
    elif level == "easy":
        return easy_level_attempts
    elif level == "medium":
        return medium_level_attempts
    else:
        game_level() #to reinitilise if wromg input is given     
        
def check_number(num ,chosen_number):
    """ Checks the guess against chosen number"""
    if num < 0 or num > 100:
        print("Please enter a number between 1 and 100.")  
    if num > chosen_number:
        print("Too high")
    elif num < chosen_number:
        print("Too low")
    else:
        num == chosen_number
        print("You guessed the number. You win!!")
       
def game():
    chosen_number = random.randint(1,100)
    print("Selected a number between 1 and 100.")
    num = int()
    attempts = game_level() #sets the attempts count
    while num != chosen_number:
        print(f"You have {attempts} attempts.")
      #to have a compulsory integer input
        try:
            num = int(input("Guess the number: "))
            check_number(num, chosen_number)
            attempts -=1
        except ValueError:
            print("You must enter an integer")
            attempts -= 1

        if attempts == 0:
            print("You have tried all the attempts. You loose.")
            return
        elif num != chosen_number:
            print("Guess again")              

while input("Do you want to play? 'yes' or 'no': ") == "yes":
    clear()
    game()
else:
    print("Game over!Bye")
        
 

    


