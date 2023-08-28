# This is a simple blackjack game
# FYI: snake_case -> variables , camelCase -> functions
import os
import random
from blackjack_art import logo as blackjack_logo
 
# I believe using a class structure to keep all the values together would be easier, but the course has not reached 
# classes yet. So, I am gonna continue without classes
card_values = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': 11,
}



def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Function that prints the logo and header."""
    print(blackjack_logo)
    print(" Welcome to Blackjack! ".center(200, '-'))
    print()

def deal_card():
    """ Returns a random card"""
    card = random.choice(list(card_values))
    return card

def calculate_total_score( user_hand ):
    """ Calculate current total scores"""
    contains_ace = False
    total_score = 0
    for card in user_hand:
        if card == 'ace':
            contains_ace = True
        total_score += card_values[card]
    if total_score > 21 and contains_ace:
        total_score -= 10

    return total_score

def print_hand_total( reveal_dealer_hand, player_total_score, dealer_total_score, player_hand, dealer_hand, player_bank, player_bet ):
    """ Print hand & total scores to player """
    clear()
    print("Current bank balance: ", player_bank)
    print("Current bet: ", player_bet)
    print(f"\nYour hand:{player_hand}\nYour current total score: {player_total_score}\n")

    if reveal_dealer_hand:
        print(f"\nDealer hand:{dealer_hand}\nDealer current total score: {dealer_total_score}\n")
    else:
        print(f"\nDealer hand:['{dealer_hand[0]}',*]\nDealer current known score: {card_values[dealer_hand[0]]}\n")

# def player_wins():



def check_if_bust( total_score ):
    """ Function to check if BUST (i.e, when total score exceeds 21)"""
    if total_score > 21:
        return True
    return False

def check_if_push( player_total_score, dealer_total_score, reveal_dealer_hand ):
    """ Function to check if PUSH (i.e, when dealer and player total scores are equal))"""
    if reveal_dealer_hand:
        if player_total_score == dealer_total_score:
            return True
        return False
    else:
        print("ERROR dealer hand not revealed yet!")
        

        # Check if win




def start_round( round_count, player_bank ):
    """ Function that restarts the round. Bank value remains. """
    round_count += 1

    # Reset both hands
    player_hand = []
    dealer_hand = []

    # Reset total scores
    player_total_score = 0
    dealer_total_score = 0

    # Reset player bet
    player_bet = 0

    # Flag to decide whether hole card needs to be displayed
    reveal_dealer_hand = False

    clear()

    # Print round count
    print(f"Round : {round_count}")

    # Take bet from player.
    # If bank is empty, then kick the user out
    # If the bet placed is more than what is in the bank, then ask again.
    player_bet = 0
    if player_bank != 0:
        while True:
            print("Current bank balance: ", player_bank)   
            player_bet = input("\nPlace your bet: (Type the specific amount or type 'all in' to go all in): ").lower()
            if player_bet == 'all in':
                player_bet = player_bank
            else:
                player_bet = int(player_bet)

            if player_bet > player_bank:
                clear()
                print("Sorry you do not have that much in the bank!\n")
                continue

            player_bank -= player_bet
            break
    else:
        print("Sorry your bank does not sufficient funds!")
        return    

    # Assign the hands to both (2 cards each)
    for i in range(0,2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())
 

    # Calculate total score and display along with the hands
    player_total_score = calculate_total_score( player_hand )
    dealer_total_score = calculate_total_score( dealer_hand )
    print_hand_total( reveal_dealer_hand, player_total_score, dealer_total_score, player_hand, dealer_hand, player_bank, player_bet )



    ### check_if_blackjack()



    # Loop until Player decides to stop and stand
    players_move = True
    while players_move:
        print("".center(200, '-') )
        print("\n\nWhat is your next move? (Hit / Stand / Double /Surrender): ")
        choice = input()


        # HIT
        if choice.upper() == 'HIT':
            print("You have chosen to draw another card.")
            new_card = deal_card()
            print(f"You drew : {new_card}")
            player_hand.append(new_card)
            player_total_score = calculate_total_score( player_hand )
            print_hand_total(reveal_dealer_hand, player_total_score, dealer_total_score, player_hand, dealer_hand, player_bank, player_bet)

            # Check BUST
            if check_if_bust(player_total_score):
                print("\nYour total score exceeded 21!\n")
                print("*********************************************** BUST ***********************************************".center(200, ' '))
                
                player_bet = 0
                # Ask user if he wants to start another game or continue this game.
                if input("\nDo you want to continue this game or exit? ( cont / exit ): ").lower() == 'exit':
                    return player_bank, round_count
                player_bank, round_count = start_round( round_count, player_bank )
                players_move = False
                
            continue


        # STAND
        elif choice.upper() == 'STAND':
            break
        elif choice.upper() == 'DOUBLE':
            break
        elif choice.upper() == 'SURRENDER': 
            break
        else:
            print("Invalid option")

    return player_bank, round_count
    

    

def start_game():
    """Function to start the game. Restarts everything. Bank value is reset."""
    restart_game = False
    while restart_game == False:    
        clear()
        print_header()
        random = input("Press Enter to Start".center(200," "))       

        # Reset the round counter and the player's bank 
        round_count = 0
        player_bank = 1000
    
        # Start the new round. Get back the previous round stats.
        prev_bank, pre_rounds = start_round( round_count, player_bank )
        difference = 1000 - prev_bank
        print()
        print("---------------- PREV. ROUND STATS: ----------------".center(200,' '))
        print(f"Number of rounds played: {pre_rounds}".center(200," "))
        print(f"Remaining bank balance: {prev_bank}".center(200," "))      
        if prev_bank > 1000:
            print(f"You made: {difference}".center(200," "))
        else:
            print(f"You lost: {difference}".center(200," "))
        

        if input("Do you want to play another game of Blackjack!? (y/n) : ").lower() == 'n':
            restart_game = True

    


if __name__ == "__main__":
    start_game()