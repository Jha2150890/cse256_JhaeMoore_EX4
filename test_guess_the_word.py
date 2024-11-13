# Jhae Moore
# CIS256 Fall 2024
# EX 4(EX 4)

# NOTE: When using pytest both correct_func and wrong_func have to be used in order the test case to pass

from guess_the_word import random_func, correct_func, wrong_func

def test_random_func(): # Test if the program selects a word from the list correctly
    assert random_func(3) == "golf"
    assert random_func(1) == "football"
    assert random_func(5) == "baseball"

def test_correct_func(): # Test if the program process the correct guesses
    assert correct_func() == True
    
def test_wrong_func(): # Test if the program process the incorrect guesses
    assert wrong_func() == False


