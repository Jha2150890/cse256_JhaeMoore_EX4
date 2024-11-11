import pytest
from guess_the_word import random_func

def test_random_func():
    assert random_func(1) == "football"
