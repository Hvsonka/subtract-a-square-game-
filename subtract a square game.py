# File: CS112_A1_T2_3_20230795.py
# Welcome to Subtract-a-square game
# Author: Hussein Ahmed Hussein
# Id: 20230795

RULES = """This is the Subtract-a-square game.
The rules are as follows:
 - A number is selected
 - You enter a number
 - The square of that number is deducted from the selected number
 - The computer selects and deducts a square from the number
 - The process is repeated
 - Whoever completes the last move wins
"""

import math

# Function to check if a number is a perfect square
def is_square(num):
    root = int(math.sqrt(num))
    return root * root == num

# Function to get valid moves (squares) for the current coins
def get_valid_moves(coins):
    return [x * x for x in range(1, int(math.sqrt(coins)) + 1) if x * x <= coins]

# Function to play the Subtract-a-square game
def subtract_square_game(coins):
    while coins > 0:
        print(f"Current coins: {coins}")
        
        # Player 1's move
        player_move = int(input("Player 1, enter your move: "))
        while player_move not in get_valid_moves(coins):
            print("Invalid move. Please choose a valid square number.")
            player_move = int(input("Player 1, enter your move: "))
        
        coins -= player_move

        # Check if Player 1 wins
        if coins == 0:
            print("Player 1 wins!")
            break

        print(f"Remaining coins: {coins}\n")

        # Player 2's move
        player_move = int(input("Player 2, enter your move: "))
        while player_move not in get_valid_moves(coins):
            print("Invalid move. Please choose a valid square number.")
            player_move = int(input("Player 2, enter your move: "))
        
        coins -= player_move

        # Check if Player 2 wins
        if coins == 0:
            print("Player 2 wins!")
            break

        print(f"Remaining coins: {coins}\n")

if __name__ == "__main__":
    # Get the initial number of coins from the user
    initial_coins = int(input("Enter the initial number of coins: "))
    
    # Start the Subtract-a-square game
    subtract_square_game(initial_coins)