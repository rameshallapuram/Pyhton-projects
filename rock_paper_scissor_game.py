rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
Option_list = [rock, paper, scissor]
option_string = ["rock", "paper", "scissor"]
#To make it best of 3 win the game. initialising the following variables to 0
count = 0
computer_score = 0
user_score = 0
#To run the loop 3 times
while count <=2:
  user_choice = int(input("Choose an option. '0' for rock, '1' for paper, '2' for scissors:"))
  print("User choice:",option_string[user_choice])
  print(Option_list[user_choice])

  computer_choice = random.randint(0,2) #random.randint chooses random integer between 0-2
  print("Computer choice is:",option_string[computer_choice])
  print(Option_list[computer_choice])

  if user_choice >= 3:
    print("Invalid input. You loose.")
  elif user_choice == 0 and computer_choice == 2:
    print("You win the match!!")
    user_score += 1
  elif user_choice == 2 and computer_choice == 0:
    print("You loose the match.")
    computer_score +=1 
  elif user_choice > computer_choice:
    print("You win the match!!")
    user_score += 1
  elif user_choice < computer_choice:
    print("You loose the match.")
    computer_score+=1
  elif user_choice == computer_choice:
    print("It's a tie!!")
  count +=1

if user_score > computer_score:
  print("You won the game!!")
elif user_score == computer_score:
  print("Game is draw.")
else:
  print("You lost the game!!") 