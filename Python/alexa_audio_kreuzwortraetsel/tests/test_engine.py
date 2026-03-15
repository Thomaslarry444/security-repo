from engine import CrosswordGame


def test_sample_puzzle_initial_state() -> None:
    game = CrosswordGame.with_sample_puzzle()
    assert game.total_count() == 3
    assert game.solved_count() == 0
    assert game.is_finished() is False


def test_correct_answer_updates_progress() -> None:
    game = CrosswordGame.with_sample_puzzle()
    first_clue = game.next_open_clue()
    assert first_clue is not None

    assert game.check_answer(first_clue.clue_id, "Alexa") is True
    assert game.solved_count() == 1


def test_wrong_answer_does_not_update_progress() -> None:
    game = CrosswordGame.with_sample_puzzle()
    first_clue = game.next_open_clue()
    assert first_clue is not None

    assert game.check_answer(first_clue.clue_id, "falsch") is False
    assert game.solved_count() == 0


def test_hint_format_contains_length_and_first_letter() -> None:
    game = CrosswordGame.with_sample_puzzle()
    hint = game.hint_for("S1")
    assert "4 Buchstaben" in hint
    assert "H" in hint
