"""
Test the feature available Moves
"""
from itertools import product

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move, ShortCastling, LongCastling
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.king import King
from app.src.model.pieces.rook import Rook


class TestKing:
    """
    Test class
    """

    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }

    def test_available_moves(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 |B| | |x|x|x| | |
        1 |R| | | |K| | |R|
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        Test that a king can't go on a square if it is checked
        :return:
        """
        piece = King(Column.E, 1)
        rook1 = Rook(Column.A, 1)
        rook2 = Rook(Column.H, 1)
        other = Rook(Column.A, 2, Color.BLACK)

        piece_list = {
            (Column.E, 1): piece,
            (Column.A, 1): rook1,
            (Column.H, 1): rook2,
            (Column.A, 2): other,
        }
        expected_moves = [
            Move(
                self.square_list[Column.E, 1],
                self.square_list[Column.D, 1],
                PieceType.KING,
            ),
            Move(
                self.square_list[Column.E, 1],
                self.square_list[Column.F, 1],
                PieceType.KING,
            ),
            ShortCastling(
                self.square_list[Column.E, 1],
                self.square_list[Column.H, 1],
            ),
            LongCastling(
                self.square_list[Column.E, 1],
                self.square_list[Column.C, 1],
            ),
        ]
        assert piece.available_moves(self.square_list, piece_list) == expected_moves
