from os import system,name
import time
def clear():
    if name == 'nt':
        _ = system('cls') #for windows
    else:
        _ = system('clear')

from art import logo
print(logo)
continue_bidding  = True
biddders_count = 0
bidder_list = {}
while continue_bidding:
    bidder_name = input("Enter bidder's name: ").title()
    #to mandate a float type of input 
    def user_input() -> float: 
        while True: 
            try: 
                return float(input("Enter bid amount: ")) 
            except: 
                pass 
    bid_amount = (user_input())       
    print(f"The bidder {bidder_name} has bidded ${bid_amount}.")

    bidder_list[bidder_name] = bid_amount #appendind data to bidder_list
    biddders_count += 1
    time.sleep(2) #to hold the output for 2 sec before clearing
    clear()
    user_choice = input("Do you wanna continue bidding? 'yes' or 'no'").lower()
    if user_choice == "no":
        continue_bidding = False
print(bidder_list)
print("Total bidders are:",biddders_count)

highest_bid = 0
for bids in bidder_list:
    if bidder_list[bidder_name] > highest_bid:
        highest_bid = bidder_list[bidder_name]
print(f"The winner of the aution is {bidder_name} and the bid amount is ${highest_bid}")

