"""
Workflow of the project:
1. Input of the user choice (Rock, paaper, scissor)
2. Input of the user choice (Rock, paper, scissor)
computer choice is raandom.
3. Print the result of the game (Win, Lose, Draw)

Cases:
A - Rock 
Rock/Rock = draw
Rock/Paper = lose
Rock/Scissor = win
B - Paper 
Paper/paper = draw
paper/Rock = win
Paper/Scissor = lose
C - Scissor
Scissor/Scissor = draw
scissor/Rock = lose
Scissor/Paper = win


"""

import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your choice (Rock, Paper, Scissor): ")
computer_choice = random.choice(item_list)

print("user choice is :" , user_choice)
print("computer choice is :" , computer_choice)

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("You Win!")
    else:
        print("You Lose!")

elif user_choice =="paper":
    if computer_choice =="Rock":
         print("You Win!")
    else:
        print("You Lose!")


elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You Win!")
    else: 
        print("You Lose!")

