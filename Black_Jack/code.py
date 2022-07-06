from os import system,name
import random
import art
print("Welcome to the game of BlackJack!!")
print(art.logo)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def deal():
    """ Returns a random card """
    card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(card_list)
    return card

def calculate_score(cards):
    """ Calculates the sum of cards in the list """
    sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    #to replace 11 in the card_list if the sum of cards in the player list exceeds 11
    if 11 in cards and sum(cards) > 11:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 


def compare(user_score, dealer_score):
    """ Compares the scores of the inputs passed """
    if user_score > 21 and dealer_score > 21:
        return "You went over. You lose"
    elif user_score == dealer_score:
        return "Draw"
    elif dealer_score == 21:
        return " You loose, opponent has Blackjack"
    elif user_score == 21:
        return "Win with a Blackjac "
    elif user_score > 21:
        return "You went over. You loose"
    elif dealer_score > 21:
        return "Opponent went over. You win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You loose"


def game():
    game_over = False
    user_hand = []
    dealer_hand = []
    
    for i in range(2):
        user_hand.append(deal())
        dealer_hand.append(deal())

    while not game_over:
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"   Your cards: {user_hand}, current score: {user_score}")
        print(f"   dealers's first card: {dealer_hand[0]}")

        if user_score == 21 or dealer_score == 21 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_hand.append(deal())
            else:
                game_over = True

    while dealer_score != 21 and dealer_score < 17:
        dealer_hand.append(deal())
        dealer_score = calculate_score(dealer_hand)
    
    print(f"Your final hand is {user_hand} and final score is {user_score}.")
    print(f"Dealer's final hand is {dealer_hand} and final score is {dealer_score}.")
    print(compare(user_score, dealer_score))

while input("Do you want to play? 'yes' or 'no'") == "yes":
    clear()
    game()
else:
    game_over = True
    print("Thank you playing. Bye!")