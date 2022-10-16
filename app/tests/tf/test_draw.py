"""
Tests for the draw rules:
- stalemate (no legal move available)
- dead position
"""
import pytest

from app.src.model.game.game import Game
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.game_state import GameState
from app.src.model.move.king_move import KingMove
from app.src.model.move.rook_move import RookMove
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.king import King
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.rook import Rook


def test_stalemate():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | |R| |
    2 | | | | | | |R| |
    1 | | | | | | | |K|
       A B C D E F G H
    Test that a draw config changes the game status
    @return:
    """
    game = Game()
    game.piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 2): Rook(Color.BLACK),
        Square(Column.G, 3): Rook(Color.BLACK),
    }
    game.color = Color.WHITE
    assert not game.available_moves_list()
    assert game.state == GameState.DRAW


@pytest.mark.skip(reason="not yet implemented")
def test_dead_position1():
    """
    Test that a dead position leads to a draw.
    1 king VS king
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | |k| |
    2 | | | | | | | | |
    1 | | | | | | | |K|
       A B C D E F G H
    @return:
    """
    game = Game()
    game.piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
    }
    assert game.state == GameState.DRAW


@pytest.mark.skip(reason="not yet implemented")
def test_dead_position2():
    """
    Test that a dead position leads to a draw.
    1 king VS king and bishop
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | |b| | |B| |
    2 | | | | | | | | |
    1 | | | | | | | |W|
       A B C D E F G H
    @return:
    """
    game = Game()
    game.piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.D, 3): Bishop(Color.WHITE),
    }
    assert game.state == GameState.DRAW


@pytest.mark.skip(reason="not yet implemented")
def test_dead_position3():
    """
    Test that a dead position leads to a draw.
    1 king VS king and knight
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | |b| | |B| |
    2 | | | | | | | | |
    1 | | | | | | | |W|
       A B C D E F G H
    @return:
    """
    game = Game()
    game.piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.D, 3): Knight(Color.WHITE),
    }
    assert game.state == GameState.DRAW


@pytest.mark.skip(reason="not yet implemented")
def test_dead_position4():
    """
    Test that a dead position leads to a draw.
    1 king and bishop VS king and bishop, both on same color
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | |b| | |B| |
    2 | | | | | | | | |
    1 | | | | | | | |W|
       A B C D E F G H
    @return:
    """
    game = Game()
    game.piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.D, 3): Knight(Color.WHITE),
        Square(Column.D, 5): Knight(Color.BLACK),
    }
    assert game.state == GameState.DRAW


def test_threefold_repetition_rule():
    """
    Test the threefold repetition rule
    8 |R| | | | | | | |
    7 | |r| | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | |k| |
    2 | | | | | | | | |
    1 | | | | | | | |K|
       A B C D E F G H
    @return:
    """
    game = Game()
    game.piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.A, 8): Rook(Color.WHITE),
        Square(Column.B, 7): Rook(Color.BLACK),
    }
    game.player = Color.BLACK
    move_list = [
        RookMove(Square(Column.B, 7), Square(Column.A, 7)),  # 1
        RookMove(
            Square(Column.A, 8), Square(Column.H, 8)
        ),
        RookMove(
            Square(Column.A, 7), Square(Column.G, 7)
        ),
        RookMove(
            Square(Column.H, 8), Square(Column.D, 8)
        ),
        RookMove(
            Square(Column.G, 7), Square(Column.A, 7)
        ),
        RookMove(
            Square(Column.D, 8), Square(Column.A, 8)
        ),  # 2
        KingMove(
            Square(Column.G, 3), Square(Column.G, 4)
        ),
        KingMove(
            Square(Column.H, 1), Square(Column.G, 1)
        ),
        KingMove(
            Square(Column.G, 4), Square(Column.G, 3)
        ),
        KingMove(
            Square(Column.G, 1), Square(Column.H, 1)
        ),  # 3
    ]
    list(map(game.apply_move, move_list))
    assert game.state == GameState.DRAW


@pytest.mark.skip(reason="not yet implemented")
def test_fifty_move():
    """
    Test the fifty move rule.
    @return:
    """
