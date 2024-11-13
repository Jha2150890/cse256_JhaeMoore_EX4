# Jhae Moore
# CIS256 Fall 2024
# EX 4(EX 4)

import random

def random_func(num):

    list_sports = ["basketball", "football", "hockey", "golf", "bmx", 'baseball']

    random_choice = list_sports[num] # Picks a word by the index number
    
    return random_choice

random_num = random.randint(0,5) # Store a number between 0 - 5

random_choice = random_func(random_num)

print("Guess the letters!")

letter = ''

turns_left = 15

while turns_left != 0:

    failed = 0

    for x in random_choice:
        if x in letter: # Print a letter(s) if the word contains it 
            print(x, end=" \n")
            def correct_func():
                return True # return True for the test case

        else:
            print("_") 
            failed += 1 # Increase failed variable by 1 until the word is fully spelled out.

    if failed == 0: # If the failed variable didn't increase, you win the game

        print("Congratulations, you got it right!")
        print(f"The word is: {random_choice}")
        break

    print()

    letter_guess = input("Guess a letter! ")

    if len(letter_guess) > 1: # You can only guess one letter and cannot be more
        print("Must only spell out one letter at a time, please try again!")
        letter_guess = ''

    letter += letter_guess.lower()

    if letter_guess not in random_choice: 

        turns_left -= 1 # Decrease the turns by 1
        def wrong_func():
            return False # return False for the test case
        print("That is wrong.")
        print(f"You have {turns_left} turns left")
        

        if turns_left == 0: # If turns reaches 0, it is game over
            print("Too bad! You lose...")
            
