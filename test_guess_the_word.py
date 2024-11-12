import pytest
from guess_the_word import random_func, correct_func, wrong_func

def test_random_func():
    assert random_func(3) == "golf"
    assert random_func(1) == "football"
    assert random_func(5) == "baseball"

def test_correct_func():
    assert correct_func() == True
    
def test_wrong_func():
    assert wrong_func() == False
