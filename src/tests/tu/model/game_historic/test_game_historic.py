"""
Tests for GameHistoric
"""
from src.domain.classes.const.color import Color
from src.domain.classes.const.column import Column
from src.domain.classes.pieces.bishop import Bishop
from src.domain.classes.pieces.king import King
from src.domain.classes.pieces.knight import Knight
from src.domain.classes.pieces.pawn import Pawn
from src.domain.classes.pieces.queen import Queen
from src.domain.classes.pieces.rook import Rook
from src.domain.classes.square import Square
from src.domain.states.board import Board
from src.domain.states.game_historic import GameHistoric


def test_update_config_history():
    """
    Test the method update_config_history
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | |R| | | |
    5 | |P| | | |k| | |
    4 | | | |N| | | | |
    3 | | | | | | | | |
    2 | |Q| | |b| | | |
    1 | | | | | | | | |
       A B C D  E F G H
    @return: None
    """
    piece_dict = {
        Square(Column.D, 4): Knight(Color.WHITE),
        Square(Column.E, 6): Rook(Color.WHITE),
        Square(Column.F, 5): King(Color.BLACK),
        Square(Column.E, 2): Bishop(Color.BLACK),
        Square(Column.B, 5): Pawn(Color.WHITE),
        Square(Column.B, 2): Queen(Color.WHITE),
    }
    move = Rook.move(Square(Column.E, 5), Square(Column.E, 6))
    board = Board()
    board.piece_dict = piece_dict
    game_historic = GameHistoric()
    game_historic.update_historic(move, board)
    expected_bit_value = 0xD00C00000000000000B000001000E0000002000 << 64
    assert game_historic.config_historic[expected_bit_value] == 1
