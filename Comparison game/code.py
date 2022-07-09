import os
from art import logo, vs
from game_data import data
import random

def clear():
   os.system('cls')

def compare(item1, item2):
    item1_followers = item1['follower_count']
    item2_followers = item2['follower_count']
    # return item2_followers, item1_followers
    
    user_guess = input("Who has more followers? A or B: ").lower()
    if item2_followers >= item1_followers and user_guess == 'b':
        return ("Right guess!! You win!")
        
    elif item2_followers < item1_followers and user_guess == 'a':
        return ("Right guess!! You win!")
        
    else:
        return ("You loose")

def game():
    print("Welcome to the higher lower guessing game...")
    print(logo)
    game_over = False
    points = 0 
    item1 = random.choice(data)
    item2 = random.choice(data)
    while not game_over:
        item1 = item2
        item2 = random.choice(data)
        print("current score:", points)
        print(f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}.")
        print(vs)
        print(f"Against B: {item2['name']}, a {item2['description']}, from {item2['country']}.")
        face_off = (compare(item1, item2))
        if face_off == "Right guess!! You win!":
            points+=1     
        else:
            print("Wrong answer. You loose.")
            print("Final score: ", points)
            game_over = True
        
while input("Do you want to play? 'yes' or 'no': ") == "yes":
    clear()
    game()
else:
    print("Thank you for playing. Bye!")




        

        

    


    





