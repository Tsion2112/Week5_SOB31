"""

Corrections made:
1. Removed debug print statement that revealed the secret number.
2. Added single-line comments to explain each part of the code.
3. Ensured input validation checks if the user enters exactly a 4-digit number.
4. Used f-strings for better string formatting.



Explanation of Changes:
1. compare_numbers function:

This function now checks each digit in the guessed number (user_guess) against the actual number (number).
It counts "bulls" when the guessed digit is in the correct position and "cows" when the guessed digit is in the number but in the wrong position.
It returns a tuple with the count of cows and bulls.
2. Game Instructions:

The instructions are printed at the beginning to explain how the game works.
3. Input Handling:

raw_input() was replaced with input(), which is used in Python 3.
There’s a check to ensure the user inputs a valid 4-digit number (len(user_guess) != 4 or not user_guess.isdigit()).
4. Exit Option:

The user can type "exit" at any prompt to end the game.
5. Padding the Number:


How the Game Works:
The player guesses a 4-digit number.
The program compares the guess to the hidden number and provides feedback:
Bulls: Digits in the correct position.
Cows: Digits in the wrong position.
The game continues until the player guesses all four digits correctly (4 bulls), and then the game ends.
"""

import random

# Tsion added: Compare the user's guess to the number and count cows and bulls
def compare_numbers(number, user_guess):
    cows = 0  # Tsion added: Initialize cows count
    bulls = 0  # Tsion added: Initialize bulls count

    # Tsion fixed: Loop through the number and guess to compare digits
    for i in range(len(number)):  
        if user_guess[i] == number[i]:  # Tsion fixed: Check if digit is in the correct position
            bulls += 1  # Tsion added: Increment bulls if the digit is correct in the correct position
        elif user_guess[i] in number:  # Tsion fixed: Check if the digit exists elsewhere in the number
            cows += 1  # Tsion added: Increment cows if the digit exists but in the wrong position

    return (cows, bulls)  # Tsion added: Return cows and bulls as a tuple

# Game setup
playing = True  # Tsion added: Start the game loop
number = str(random.randint(0, 9999)).zfill(4)  # Tsion fixed: Ensure the number is always 4 digits
guesses = 0  # Tsion added: Initialize guesses count

# Tsion added: Game instructions
print("Let's play a game of Cowbull!")
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow.")
print("For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

# Main game loop
while playing:
    user_guess = input("Give me your best guess! (4 digits)")  # Tsion fixed: Used input() to capture user guess
    if user_guess == "exit":  # Tsion added: Option to exit the game
        print("Thanks for playing!")
        break  # Exit the game loop

    # Tsion fixed: Check if the guess is a valid 4-digit number
    if len(user_guess) != 4 or not user_guess.isdigit():
        print("Invalid input. Please enter a 4-digit number.")  # Tsion added: Print an error message for invalid input
        continue  # Tsion added: Ask for input again if it's invalid

    cowbullcount = compare_numbers(number, user_guess)  # Tsion fixed: Get the cows and bulls count
    guesses += 1  # Tsion added: Increment the guess count

    print(f"You have {cowbullcount[0]} cows, and {cowbullcount[1]} bulls.")  # Tsion fixed: Display cows and bulls correctly

    # Tsion fixed: End the game if the user gets 4 bulls
    if cowbullcount[1] == 4:
        playing = False  # Tsion added: Stop playing when 4 bulls are achieved
        print(f"You win the game after {guesses} guesses! The number was {number}.")
        break  # Tsion added: Exit the game loop

    else:
        print("Your guess isn't quite right, try again.")  # Tsion added: Prompt the user to try again if not correct

