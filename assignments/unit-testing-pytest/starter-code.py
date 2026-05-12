"""
Starter Code for Unit Testing with pytest
Complete the TODO sections with your test functions.
Run your tests with: pytest starter-code.py
"""

import pytest


# ============ CALCULATOR MODULE ============
# These are the functions you'll test in Task 1 and Task 2

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raise ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ============ STRING UTILITIES MODULE ============
# These are functions you'll test in Task 3 (stretch goal)

def is_palindrome(s):
    """Check if a string is a palindrome (reads the same forwards and backwards)."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def reverse_words(sentence):
    """Reverse the order of words in a sentence."""
    return " ".join(sentence.split()[::-1])


def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


# ============ TASK 1: BASIC UNIT TESTS ============
# TODO: Write at least 3 test functions below
# Test the add(), subtract(), and multiply() functions

# Example test to get you started:
def test_add_basic():
    """Test basic addition."""
    assert add(2, 3) == 5


# TODO: Write your test_subtract function here
# Example: def test_subtract():
#              assert subtract(5, 3) == 2


# TODO: Write your test_multiply function here


# ============ TASK 2: EDGE CASES & ERROR HANDLING ============
# TODO: Write at least 2 additional test functions for edge cases

# Example edge case test:
def test_add_with_negatives():
    """Test addition with negative numbers."""
    assert add(-2, -3) == -5
    assert add(-5, 3) == -2


# TODO: Test division by zero using pytest.raises()
# Example: def test_divide_by_zero():
#              with pytest.raises(ValueError):
#                  divide(10, 0)


# ============ TASK 3: COMPREHENSIVE TESTING (STRETCH GOAL) ============
# TODO: Write tests for string_utils functions
# Test is_palindrome(), reverse_words(), and count_vowels()

# Example:
# def test_is_palindrome():
#     assert is_palindrome("racecar") == True
#     assert is_palindrome("hello") == False
