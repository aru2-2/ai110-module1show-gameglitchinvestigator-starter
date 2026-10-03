from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Regression tests for the high/low hint bug: the message must tell the player
# which direction to move, not the opposite.
def test_too_high_guess_tells_player_to_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_guess_tells_player_to_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_hint_direction_at_boundaries():
    # Off-by-one on either side of the secret
    assert check_guess(51, 50)[0] == "Too High"
    assert check_guess(49, 50)[0] == "Too Low"


# Regression tests for parse_guess whitespace handling.
def test_parse_guess_strips_surrounding_whitespace():
    assert parse_guess("  42  ") == (True, 42, None)

def test_parse_guess_whitespace_only_is_treated_as_empty():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_empty_and_none():
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")

def test_parse_guess_rejects_non_numeric():
    assert parse_guess("abc") == (False, None, "That is not a number.")
