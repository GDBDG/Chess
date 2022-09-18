"""
Tests for the king basic moves
"""
from app.src.model.game.game import Game
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.king_move import KingMove
from app.src.model.pieces.king import King
from app.src.model.pieces.piece import Piece


def test_available_king_moves():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | |b|W|W| | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The rook moves uses _available_square_on_side_line, already completely
    tested)
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): King(Color.WHITE),
        Square(Column.E, 4): Piece(Color.WHITE),
        Square(Column.C, 4): Piece(Color.BLACK),
    }
    game = Game()
    game.piece_dict = piece_dict
    expected_moves = [
        KingMove(Square(Column.D, 4), Square(Column.C, 3)),
        KingMove(Square(Column.D, 4), Square(Column.C, 4)),
        KingMove(Square(Column.D, 4), Square(Column.C, 5)),
        KingMove(Square(Column.D, 4), Square(Column.D, 3)),
        KingMove(Square(Column.D, 4), Square(Column.D, 5)),
        KingMove(Square(Column.D, 4), Square(Column.E, 3)),
        KingMove(Square(Column.D, 4), Square(Column.E, 5)),
    ]
    assert game.square_available_moves(Square(Column.D, 4)) == expected_moves
