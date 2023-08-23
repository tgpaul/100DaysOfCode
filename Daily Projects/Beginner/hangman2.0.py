# A simple hangman game (My code) Overworked things
# Day Goal: Work with lists and strings more

import random
import re

# Function to get the random word from a predefined list of words
def get_word():
    words_list = ["Stranger Things", "The Walking Dead", "Money Heist", "The Squid Game", "Breaking Bad"]

    word = random.choice(words_list)

    return word

# Function to get the initial hidden word
def get_initial_word_state(word, state):
    if state == "":
        state =  "_"*len(word)
    
    if " " in word:
        state_list = [i for i in state]
        pos =  [ match.start() for match in re.finditer(" ", word)]
        for index in pos:
            state_list[index] = " "

        state = ""
        for ele in state_list:
            state += ele
        return (state)



# Function to check if a letter is present in the word. Populates state with all the occurences of the guessed letter.
# Returns nothing
def check_letter(word, state, letter, lives):

    # Checking
    # Case that guessed letter is present
    if letter in word:
        print(f"\nGood guess. {letter} is present in the word.")
        
        # Converting state(string) into list
        state_list = [i for i in state]

        # Finding the index of every occurences of the word
        pos =  [ match.start() for match in re.finditer(letter, word)]

        # Replacing the occurences in the state
        for index in pos:
            state_list[index] = letter
        
        # Converting state back to a string
        state = ""
        for ele in state_list:
            state += ele
        return (state, lives)
        

    # Case that guessed letter is not present in the word
    else:
        lives -= 1
        print(f"\nSorry you guessed wrong. '{letter}' is not present in the word.\nYou have lost a life. REMAINING LIVES = {lives}")
        return (state, lives)

def check_stopping_condition(word, state, lives):
    if lives == 0:
        print("\nOh no! You have run out of lives.\nYOU LOSE")
        return True
    elif word == state:
        print(f"\nCongarts! You guessed the word right.\nThe word was: {word.upper()}\nYOU WIN")
        return True
    else:
        return False
        


if __name__ == "__main__":
    random_word = get_word().lower()
    remaining_lives = 6
    word_state = ""

    print("Welcome to Hangman!".center(100,"-"))
    print("""
The rules are simple. You have to guess an english series that I have chosen.
You have to guess the letters of the words in the series.
          If the letter you gave is present in the words, then I will show you it's postion.
          And if you are able to guess the entire word then you win.
          However, for every wrong letter that you guess you lose a life. If you run out of lives, you will lose.

Let us begin the game.
""")
    
    word_state = get_initial_word_state(random_word, word_state)
    print("The word given is ", word_state)

    while not check_stopping_condition(random_word, word_state, remaining_lives):
        user_guess = input("Enter your guess: ").lower()

        (word_state, remaining_lives) = check_letter(random_word, word_state, user_guess, remaining_lives)
        print(remaining_lives)

        print("\nPresent state of the word is: ", word_state)