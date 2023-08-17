from main import Chess
import unittest
import pytest
import chess
from chess import IllegalMoveError


@pytest.fixture
def chess_sim():
    return Chess()


def test_apply_moves_applies_legal_moves(chess_sim):
    moves = ["e2e4", "b8c6"]
    expected_board_final_state = chess.Board(
        "r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2"
    )

    chess_sim.apply_moves(moves)

    assert chess_sim.board == expected_board_final_state


def test_apply_moves_throws_IllegalMoveError_when_move_is_illegal(chess_sim):
    invalid_moves = ["e2e4", "b8c5"]  # Second move is an illegal knight move
    with pytest.raises(IllegalMoveError) as exeption:
        chess_sim.apply_moves(invalid_moves)
        assert type(exception) == IllegalMoveError
