"""
Tests for the draw rules:
- stalemate (no legal moves available)
- dead position
"""
import pytest

from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.pieces.bishop import Bishop
from app.src.model.classes.pieces.king import King
from app.src.model.classes.pieces.knight import Knight
from app.src.model.classes.pieces.rook import Rook
from app.src.model.classes.square import Square
from app.src.model.events.moves.king_move import KingMove
from app.src.model.events.moves.knight_move import KnightMove
from app.src.model.events.moves.pawn_2_square_move import Pawn2SquareMove
from app.src.model.events.moves.rook_move import RookMove
from app.src.model.game.board import Board
from app.src.model.game.game import Game
from app.src.model.game.game_state import GameState


def test_stalemate():
    """
    8 | | | | | | | | |
    7 | |k| | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | |r| |
    3 | | | | | | | | |
    2 | | | | | | |r| |
    1 | | | | | | | |K|
       A B C D E F G H
    Test that a draw config changes the game status
    @return:
    """
    game = Game()
    piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 2): Rook(Color.BLACK),
        Square(Column.G, 4): Rook(Color.BLACK),
        Square(Column.B, 7): King(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    game.game_state.player = Color.BLACK
    game.white_castling_state._CastlingState__long_castling_available = False
    game.apply_move(RookMove(Square(Column.G, 4), Square(Column.G, 3)))
    assert not game.available_moves_list()
    assert game.game_state.state == GameState.DRAW


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
    piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert game.game_state.state == GameState.DRAW


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
    piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.D, 3): Bishop(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert game.game_state.state == GameState.DRAW


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
    piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.D, 3): Knight(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert game.game_state.state == GameState.DRAW


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
    piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.D, 3): Knight(Color.WHITE),
        Square(Column.D, 5): Knight(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert game.game_state.state == GameState.DRAW


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
    piece_dict = {
        Square(Column.H, 1): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
        Square(Column.A, 8): Rook(Color.WHITE),
        Square(Column.B, 7): Rook(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    game.game_state.player = Color.BLACK
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
    assert game.game_state.state == GameState.DRAW


def test_fifty_move():
    """
    Test the fifty moves rule.
    @return:
    """
    game = Game()
    game.game_state.fifty_counter = 98
    game.apply_move(KnightMove(Square(Column.G, 1), Square(Column.F, 3)))
    assert game.game_state.fifty_counter == 99
    assert game.game_state.state == GameState.RUNNING
    game.apply_move(KnightMove(Square(Column.B, 8), Square(Column.C, 6)))
    assert game.game_state.fifty_counter == 100
    assert game.game_state.state == GameState.DRAW
    # Assert that a capture reset the counter
    game = Game()
    game.game_state.fifty_counter = 98
    piece_dict = {
        Square(Column.A, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.H, 2): Rook(Color.BLACK),
        Square(Column.B, 5): King(Color.BLACK),

    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board

    game.apply_move(RookMove(Square(Column.H, 1), Square(Column.H, 2)))
    assert game.game_state.fifty_counter == 0
    # Assert that a pawn moves reset the counter
    game = Game()
    game.game_state.fifty_counter = 98
    game.apply_move(Pawn2SquareMove(Square(Column.E, 2), Square(Column.E, 4)))
    assert game.game_state.fifty_counter == 0
