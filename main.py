"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tereza Petrova
email: tereza.petrova00@gmail.com
"""

import random

def greet_user():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    print("Enter a number:")
    print("-" * 47)

def generate_secret_number():
    digits = list("123456789")
    first_digit = random.choice(digits)
    digits = list("0123456789")
    digits.remove(first_digit)
    rest_digits = random.sample(digits, 3)
    return first_digit + ''.join(rest_digits)

def is_valid_guess(guess):
    if not guess.isdigit():
        print("Input must contain digits only.")
        return False
    if len(guess) != 4:
        print("Number must have exactly 4 digits.")
        return False
    if guess[0] == '0':
        print("Number must not start with zero.")
        return False
    if len(set(guess)) != 4:
        print("Digits must be unique.")
        return False
    return True

def evaluate_guess(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def format_result(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_word}, {cows} {cow_word}"

def play_game():
    greet_user()
    secret = generate_secret_number()
    attempts = 0

    while True:
        guess = input(">>> ").strip()
        if not is_valid_guess(guess):
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)

        if bulls == 4:
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guess{'es' if attempts != 1 else ''}!")
            print("-" * 47)
            print("That's amazing!")
            break
        else:
            print(f"{format_result(bulls, cows)}")

if __name__ == "__main__":
    play_game()