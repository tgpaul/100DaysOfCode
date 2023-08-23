# A simple program to create a blind auction.
# Day Goal: Learn more about dictionaries

import os
 
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
import art
if __name__ == "__main__":
    biding_finished = False
    bids = {}
    def find_highest_bidder():
        highest_bid = 0
        winner = None
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with the highest bid of {highest_bid} dollars. Congratulations!")
            
    while not biding_finished:
        clear()
        print(art.logo)
        print("Welcome to the blind auction")
        bidder_name = input("Please enter your name: ")  
        bid_value = int(input("Please enter your bid: "))
        bids[bidder_name] = bid_value

        clear()
        answer = input("Is there another bidder? (Yes/No): ").lower()
        if answer == 'no': 
            biding_finished = True

    find_highest_bidder()

