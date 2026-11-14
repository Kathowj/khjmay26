import pytest
from unittest.mock import patch

from guess import pick_secret, play_game


def test_pick_secret_in_range():
    for _ in range(100):
        number = pick_secret()
        assert 1 <= number <= 100


def test_pick_secret_custom_range():
    assert pick_secret(low=5, high=5) == 5


def test_pick_secret_rejects_invalid_range():
    with pytest.raises(ValueError):
        pick_secret(low=10, high=1)


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
    assert attempts == 1


def test_play_game_out_of_range_does_not_count():
    guesses = iter(["101", "42"])
    with patch("builtins.input", side_effect=guesses):
        attempts = play_game(secret=42)
    assert attempts == 1


def test_play_game_stops_at_max_attempts():
    guesses = iter(["10", "80", "20"])
    with patch("builtins.input", side_effect=guesses):
        attempts = play_game(secret=42, max_attempts=2)
    assert attempts == 2


def test_play_game_rejects_secret_outside_range():
    with pytest.raises(ValueError):
        play_game(secret=101)


def test_play_game_rejects_zero_max_attempts():
    with pytest.raises(ValueError):
        play_game(secret=42, max_attempts=0)
