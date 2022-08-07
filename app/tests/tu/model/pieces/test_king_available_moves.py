"""
Test the feature available Moves
"""
from itertools import product
from unittest.mock import MagicMock

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move, ShortCastling, LongCastling, EmptyMove
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
        @return:
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
        assert (
            piece._available_moves_no_legal_verification(
                self.square_list, piece_list, EmptyMove()
            )
            == expected_moves
        )

    def test_apply_castling(self):
        """
        Test that castling are applied
        @return:
        """
        piece = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        rook2 = Rook(Column.A, 1)
        piece.short_castle = MagicMock()
        piece.long_castle = MagicMock()
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.E, 1): piece,
            (Column.H, 1): rook,
            (Column.A, 1): rook2,
        }
        move = ShortCastling(
            square_list[Column.E, 1],
            square_list[Column.H, 1],
        )
        piece._apply_move_no_legal_verification(
            move, square_list, piece_list, EmptyMove()
        )
        piece.short_castle.assert_called_once_with(square_list, piece_list)
        move = LongCastling(
            square_list[Column.E, 1],
            square_list[Column.A, 1],
        )
        piece._apply_move_no_legal_verification(
            move, square_list, piece_list, EmptyMove()
        )
        piece.long_castle.assert_called_once_with(square_list, piece_list)
