import random


def pick_secret(low=1, high=100):
    return random.randint(low, high)


def play_game(secret):
    attempts = 0
    while True:
        raw = input("Guess a number (1-100): ")
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            return attempts


def main():
    print("=== Number Guessing Game ===")
    secret = pick_secret()
    play_game(secret)


if __name__ == "__main__":
    main()
