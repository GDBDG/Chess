"""
Tests for GameHistoric
"""
from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.const.column import Column
from src.CHESS.domain.classes.pieces.bishop import Bishop
from src.CHESS.domain.classes.pieces.king import King
from src.CHESS.domain.classes.pieces.knight import Knight
from src.CHESS.domain.classes.pieces.pawn import Pawn
from src.CHESS.domain.classes.pieces.queen import Queen
from src.CHESS.domain.classes.pieces.rook import Rook
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.states.board import Board
from src.CHESS.domain.states.game_historic import GameHistoric


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
