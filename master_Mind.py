#!/bin/python3
import random

# Mapping tussen nummers en kleuren
COLOR_MAP = {
    "1": "red", "red": "red",
    "2": "blue", "blue": "blue",
    "3": "green", "green": "green",
    "4": "yellow", "yellow": "yellow",
    "5": "purple", "purple": "purple",
    "6": "orange", "orange": "orange"
}

ALLOWED_COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

def generate_Code(length=4):
    return [random.choice(ALLOWED_COLORS) for _ in range(length)]


def get_Feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))

    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(color, 0), 
    guess_counts.get(color, 0)) for color in guess_counts)

    return black_pegs, white_pegs


def show_Secret(code):
    print("Secret code:", ' '.join(code))


def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-color code. Use color **names** or **numbers 1–6**.")
    print("Choices:")
    for num, color in sorted((k, v) for k,
     v in COLOR_MAP.items() if k.isdigit()):
        print(f"  {num}: {color}")


    secret_code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = []
        valid_guess = False

        while not valid_guess:
            user_input = input(f"\nAttempt {attempt}: ").strip().lower()

            if user_input == "cheat":
                password = input("Enter cheat password: ").strip()
                if password == "admin":
                    show_Secret(secret_code)
                else:
                    print("Incorrect password. Cheat mode denied.")
                continue

            raw_guess = user_input.split()
            if len(raw_guess) != 4:
                print("Please enter exactly 4 values (colors or numbers).")
                continue

            try:
                guess = [COLOR_MAP[word] for word in raw_guess]
                valid_guess = True
            except KeyError:
                print("Invalid entry. Use colors or numbers from 1–6.")
                continue

        black, white = get_Feedback(secret_code, guess)
        print(f"Black pegs (correct color & position): {black}")
        print(f"White pegs (correct color, wrong position): {white}")

        if black == 4:
            print(f"\nCongratulations! You guessed the code: 
            {' '.join(secret_code)}")
            return

    print(f"\nGame Over! The correct code was: {' '.join(secret_code)}")

if __name__ == "__main__":
    again = "Y"
    while again == "Y":
        play_Mastermind()
        again = input("\nPlay again? (Y/N): ").strip().upper()

