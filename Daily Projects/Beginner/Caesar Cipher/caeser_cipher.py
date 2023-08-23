# The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. 
# It's simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet.

# Day Goal: Learn about function parameters

from art import logo

def caesar_cipher(message, shift, decision):
    text = ""
    for letter in message:
        if not letter.isalpha():
            text += letter
            continue
        if decision == 'encode':
            new_letter = chr((ord(letter) + shift-97) % 26 + 97)
        elif decision == 'decode':
            new_letter = chr((ord(letter) - shift-97) % 26 + 97)
        else:
            print("You entered an invalid option!")
            return
        
        text += new_letter
    print(f"The {decision}d text is: {text}")

    

## I have optimized the code by making the separate decode and encode functions (shown below) into a single function (shown above)

# def encrypt(message, shift):
#     encrypt_message = ''
#     for plain_letter in message:
#         if plain_letter == " ":
#             encrypt_message += " "
#             continue
#         # Unicode of plain letter - shifted and looped in case of overflow within the alphabet
#         enc_letter = chr((ord(plain_letter) + shift-97) % 26 + 97)
#         encrypt_message += enc_letter
#     print("The encrypted text is ", encrypt_message)

# def decode(message, shift):
#     plain_message = ''
#     for encrypt_letter in message:
#         if encrypt_letter == " ":
#             plain_message += " "
#             continue
#         # Unicode of plain letter - shifted and looped in case of overflow within the alphabet
#         plain_letter = chr((ord(encrypt_letter) - shift-97) % 26 + 97)
#         plain_message += plain_letter
#     print("The decrypted text is ", plain_message)

if __name__ == "__main__":
    print(logo)

    user_continue = "yes"

    while user_continue == "yes":
        user_choice = input("1. Type 'encode' to encrypt\n2. Type 'decode' to decrypt\n").lower()

        msg = input("Type your message: ").lower()
        shift_number = int(input("Type the shift number: "))

        caesar_cipher(message=msg, shift=shift_number, decision=user_choice)
        # if user_choice == "encode":
        #     encrypt(msg, shift_number)

        # elif user_choice == "decode":
        #     decode(msg, shift_number)

        # else: 
        #     print("You chose an invalid option!")
    
        user_continue = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

    print("EXITING")