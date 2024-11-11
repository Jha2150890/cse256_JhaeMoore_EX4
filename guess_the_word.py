import random

def random_func(num):

    list_sports = ["basketball", "football", "hockey", "golf", "bmx", 'baseball']

    random_choice = list_sports[num]
    
    return random_choice

random_num = random.randint(0,5)

random_choice = random_func(random_num)

print("Guess the letters!")

letter = ''

turns_left = 15

while turns_left != 0:

    failed = 0

    for x in random_choice:
        if x in letter:
            print(x, end=" \n")

        else:
            print("_")
            failed += 1

    if failed == 0:

        print("Congratulations, you got it right!")
        print(f"The word is: {random_choice}")
        break

    print()

    letter_guess = input("Guess a letter! ")

    if len(letter_guess) > 1:
        print("Must only spell out one letter at a time, please try again!")
        letter_guess = ''

    letter += letter_guess.lower()

    if letter_guess not in random_choice:

        turns_left -= 1
        print("That is wrong.")
        print(f"You have {turns_left} turns left")

        if turns_left == 0:
            print("Too bad! You lose...")
            
