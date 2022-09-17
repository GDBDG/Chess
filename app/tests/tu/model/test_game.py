"""
Tests for the game class
"""
from app.src.model.game.game import Game
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.knight_move import KnightMove
from app.src.model.move.pawn_move import PawnMove
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.king import King
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


def test_available_moves_list():
    """
    Test that an initial config returns all the 20 moves
    No need to do more tests, They are done in the piece test
    with the get_available_moves
    @return:
    """
    game = Game()
    expected_moves = [
        KnightMove(
            Square(Column.B, 1),
            Square(Column.A, 3),
        ),
        KnightMove(
            Square(Column.B, 1),
            Square(Column.C, 3),
        ),
        KnightMove(
            Square(Column.G, 1),
            Square(Column.F, 3),
        ),
        KnightMove(
            Square(Column.G, 1),
            Square(Column.H, 3),
        ),
        PawnMove(
            Square(Column.A, 2),
            Square(Column.A, 4),
        ),
        PawnMove(
            Square(Column.A, 2),
            Square(Column.A, 3),
        ),
        PawnMove(
            Square(Column.B, 2),
            Square(Column.B, 4),
        ),
        PawnMove(
            Square(Column.B, 2),
            Square(Column.B, 3),
        ),
        PawnMove(
            Square(Column.C, 2),
            Square(Column.C, 4),
        ),
        PawnMove(
            Square(Column.C, 2),
            Square(Column.C, 3),
        ),
        PawnMove(
            Square(Column.D, 2),
            Square(Column.D, 4),
        ),
        PawnMove(
            Square(Column.D, 2),
            Square(Column.D, 3),
        ),
        PawnMove(
            Square(Column.E, 2),
            Square(Column.E, 4),
        ),
        PawnMove(
            Square(Column.E, 2),
            Square(Column.E, 3),
        ),
        PawnMove(
            Square(Column.F, 2),
            Square(Column.F, 4),
        ),
        PawnMove(
            Square(Column.F, 2),
            Square(Column.F, 3),
        ),
        PawnMove(
            Square(Column.G, 2),
            Square(Column.G, 4),
        ),
        PawnMove(
            Square(Column.G, 2),
            Square(Column.G, 3),
        ),
        PawnMove(
            Square(Column.H, 2),
            Square(Column.H, 4),
        ),
        PawnMove(
            Square(Column.H, 2),
            Square(Column.H, 3),
        ),
    ]
    assert game.available_moves_list() == expected_moves


def test_update_config_history():
    """
    Test the method update_config_history
    8 | | | |  | | | | |
    7 | | | |  | | | | |
    6 | | | |  |R| | | |
    5 | |P| |  | |k| | |
    4 | | | |KN| | | | |
    3 | | | |  | | | | |
    2 | |Q| |  |b| | | |
    1 | | | |  | | | | |
       A B C D  E F G H
    @return: None
    """
    piece_dict = {
        Square(Column.D, 4): Knight(Color.WHITE),
        Square(Column.E, 6): Rook(Color.WHITE),
        Square(Column.F, 5): King(Color.BLACK),
        Square(Column.E, 2): Bishop(Color.BLACK),
        Square(Column.B, 5): Pawn(Color.WHITE),
        Square(Column.B, 2): Queen(Color.WHITE)
    }
    game = Game()
    game.piece_dict = piece_dict
    game.update_config_history()
    expected_bit_value = 0xd00c00000000000000b000001000e0000002000 << 64
    assert game.config_history[expected_bit_value] == 1
