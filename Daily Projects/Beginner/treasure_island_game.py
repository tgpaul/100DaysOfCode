# A kind of game where the user makes their decisions
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
# Day Goal: Learn about control flow and logical operators

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input("""\nYou are at a cross road.
Do you want to go left or right? (L or R): """).lower()

if choice == "l":
    choice = input("""\nYou take the path to the left.
You came across a lake. There is an island in the middle of the lake.
Do you wait or swim? (Type 'wait' or 'swim'): """).lower()
    
    if choice == "wait":
        choice = input("""\nYou wait for some time. A person with a boat comes along and takes you across the river.
You reach the island safely!
There is a house with 3 doors in fornt of you. One red, one yellow and one blue.
Which door do you choose? (Type 'red','yellow' or 'blue'): """).lower()     
        
        if choice == "red":
            print("""\nYou walk into the room with the red door.
Suddenly the room bursts into flames.
You died. :(
Game Over!""")
        
        elif choice == "blue":
            print("""\nYou walk into the room with the blue door.
Suddenly three huge beasts lunges at you and tear you into pieces.
You Died. :(
Game Over!""")
        
        elif choice == "yellow":
            print("""\nYou walk into the room with the yellow door. You are amazed to find a treasure chest filled to the brim with diamonds. 
YOU WIN!!! :)
Game Over!""")
        else:
            print("\nYou choose and option not given. You have been smited by the game gods.\nYou died. :(\nGame Over")
    else:
        print("\nYou try to swim and are attacked by trout.\nYou died. :(\nGame Over!")
else:
    print("\nYou take the path to the right.\nSorry you fell into a hole.\nYou died. :(\nGame Over!")
