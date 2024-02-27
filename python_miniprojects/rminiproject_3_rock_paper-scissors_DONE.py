"""
Rock-Paper-Scissors Game
    take in a number 0-2 from the user that represents their hand
    generate a random number 0-2 to use for the computer's hand
    call the function get_hand to get the string representation of the user's hand
    call the function get_hand to get the string representation of the computer's hand
    call the function determine_winner to figure out who won
    print out the player hand and computer hand
    print out the winner
"""
import random

computer_choice = random.randint(0,2)
user_choice = int(input(f"Please enter:\n0 for scissor\n1 for rock\n2 for paper\nYour choice: "))

def get_hand(hand):
    hand_choices = {0:"scissor", 1:"rock", 2:"paper"}
    return hand_choices.get(hand)

computer_hand = get_hand(computer_choice)
user_hand = get_hand(user_choice)

if computer_hand == "scissor" and user_hand == "scissor":
    escenario = 1
elif computer_hand == "scissor" and user_hand == "rock":
    escenario = 2
elif computer_hand == "scissor" and user_hand == "paper":
    escenario = 3
elif computer_hand == "rock" and user_hand == "scissor":
    escenario = 4
elif computer_hand == "rock" and user_hand == "rock":
    escenario = 5
elif computer_hand == "rock" and user_hand == "paper":
    escenario = 6
elif computer_hand == "paper" and user_hand == "scissor":
    escenario = 7
elif computer_hand == "paper" and user_hand == "rock":
    escenario = 8
elif computer_hand == "paper" and user_hand == "paper":
    escenario = 9

def determine_winner(winner):
    escenario_final = {1:"Tie",2:"User wins!",3:"Computer wins!",4:"Computer wins!",5:"Tie",6:"User wins!",7:"User wins!",8:"Computer wins!",9:"Tie"}
    return escenario_final.get(winner)

result = determine_winner(escenario)

print("Computer choice:",computer_hand)
print("User choice:",user_hand)
print("Result:",result)

