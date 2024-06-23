import random

# Define the options for the game
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([1, -1, 0])  # Computer randomly selects an option
youstr = input("Enter your choice from 's', 'w', 'g': ")  # User inputs their choice
youdict = {"s": 1, "w": -1, "g": 0}  # Dictionary mapping user input to the game options
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}  # Dictionary to reverse map game options

you = youdict[youstr]  # Assign the user's choice based on the input

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")  # Print user and computer choices

if computer == you:  # Check for a draw
    print("It's a draw")
else:
    # Determine the winner based on the choices
    if computer == -1 and you == 1:
        print("You Win!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You Win!")
    elif computer == 0 and you == -1:
        print("You Win!")
    elif computer == 0 and you == 1:
        print("You Lose!")
    else:
        print("Something Went Wrong")
