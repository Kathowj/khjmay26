from unittest.mock import patch
from guess import pick_secret, play_game


def test_pick_secret_in_range():
    for _ in range(100):
        n = pick_secret()
        assert 1 <= n <= 100


def test_pick_secret_custom_range():
    n = pick_secret(low=5, high=5)
    assert n == 5


def test_play_game_single_correct_guess():
    with patch("builtins.input", return_value="42"):
        attempts = play_game(secret=42)
    assert attempts == 1


def test_play_game_multiple_guesses():
    guesses = iter(["10", "80", "42"])
    with patch("builtins.input", side_effect=guesses):
        attempts = play_game(secret=42)
    assert attempts == 3


def test_play_game_invalid_then_correct():
    guesses = iter(["abc", "42"])
    with patch("builtins.input", side_effect=guesses):
        attempts = play_game(secret=42)
    assert attempts == 1  # invalid input doesn't count
