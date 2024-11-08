import random

random_num = random.randint(0,5)

list_sports = ["basketball", "football", "hockey", "golf", "bmx", 'baseball']

random_choice = list_sports[random_num]

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

    letter += letter_guess.lower()

    if letter_guess not in random_choice:

        turns_left -= 1
        print("That is wrong.")
        print(f"You have {turns_left} turns left")

        if turns_left == 0:
            print("Too bad! You lose...")
            
