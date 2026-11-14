import random


def pick_secret(low=1, high=100):
    """Return a random integer between low and high, inclusive."""
    if low > high:
        raise ValueError("low must be less than or equal to high")
    return random.randint(low, high)


def play_game(secret, low=1, high=100, max_attempts=None):
    """Run the guessing game and return the number of valid guesses used.

    Invalid or out-of-range input does not count as an attempt.
    If max_attempts is reached, the game ends and returns the attempts used.
    """
    if low > high:
        raise ValueError("low must be less than or equal to high")
    if not low <= secret <= high:
        raise ValueError("secret must be within the guessing range")
    if max_attempts is not None and max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    attempts = 0

    while True:
        raw = input(f"Guess a number ({low}-{high}): ")

        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not low <= guess <= high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            return attempts

        if max_attempts is not None and attempts >= max_attempts:
            print(f"Out of attempts! The secret number was {secret}.")
            return attempts


def main():
    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    secret = pick_secret()
    play_game(secret, max_attempts=10)


if __name__ == "__main__":
    main()
