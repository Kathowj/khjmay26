# Python Number Guessing Game

A command-line number guessing game built with Python. The program selects a
random number, accepts guesses from the player, and provides feedback until
the player guesses correctly or reaches the attempt limit.

## Features

- Random number generation
- Configurable guessing range
- Input validation and error handling
- High/low feedback
- Optional maximum number of attempts
- Automated tests for core game behavior

## Requirements

- Python 3.11 or later
- pytest (for running the test suite)

## Run the game

Clone the repository and run:

```bash
python guess.py
```

The game chooses a number from 1 to 100 and allows up to 10 valid guesses.

## Run the tests

Install pytest:

```bash
python -m pip install pytest
```

Run the test suite:

```bash
python -m pytest -v
```

## Project structure

```text
.
├── guess.py
├── test_guess.py
└── README.md
```

## Concepts demonstrated

This project demonstrates Python functions, loops, conditionals, exception
handling, random number generation, input validation, and automated testing
with mocked user input.

## Future improvements

- Add difficulty levels
- Track and display a high score
- Add a replay option
- Package the game for installation
