"""
Test for the king
"""
from itertools import product

import pytest

from app.src.exceptions.invalid_movement_error import InvalidMovementError
from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.castling_errors import CastlingErrors
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.pieces.king import King
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.rook import Rook


class TestKing:
    """
    Test class
    """

    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }

    def test_available_squares(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W|W| | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        (The rook moves uses _available_square_on_side_line, already completely
        tested)
        :return:
        """
        piece = King(Column.D, 4)
        other = Piece(Column.E, 4)

        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 4): other,
        }
        expected_squares = [
            self.square_list[Column.C, 3],
            self.square_list[Column.C, 4],
            self.square_list[Column.C, 5],
            self.square_list[Column.D, 3],
            self.square_list[Column.D, 5],
            self.square_list[Column.E, 3],
            self.square_list[Column.E, 5],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_available_squares2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W|B| | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        (The rook moves uses _available_square_on_side_line, already completely
        tested)
        :return:
        """
        piece = King(Column.D, 4)
        other = Piece(Column.E, 4, Color.BLACK)

        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 4): other,
        }
        expected_squares = [
            self.square_list[Column.E, 4],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_available_squares3(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 |W| | | |B| | | |
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        Test that a king can't go on a square if it is checked
        :return:
        """
        piece = King(Column.A, 1)
        other = Rook(Column.E, 1, Color.BLACK)

        piece_list = {
            (Column.A, 1): piece,
            (Column.E, 1): other,
        }
        expected_squares = [
            self.square_list[Column.A, 2],
            self.square_list[Column.B, 2],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_is_short_castling_available(self):
        """
        | | | | |K|x|x|R|
         A B C D E F G H
        Check that a valid set up return the square
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.VALID
        )

    def test_is_short_castling_not_available1(self):
        """
        | | | | | | | |R|
        | | | | |K|x|x| |
         A B C D E F G H
        Check that if the rook has moved, castling unavailable
        Check that if there is no rook, castling is unavailable
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.H, 2)
        # no rook
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 2): rook,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.ROOK_HAS_MOVED
        )
        # rook has moved
        rook.move_to(self.square_list[Column.H, 1], self.square_list, piece_list)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.ROOK_HAS_MOVED
        )

    def test_is_short_castling_not_available12(self):
        """
        Check that if the king has moved, castling unavailable
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        king.has_moved = True
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.KING_HAS_MOVED
        )

    def test_is_short_castling_not_available13(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 |B| | | |K| | |R|
           A B C D E F G H
        Check that if the king is in check, castling unavailable
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        other = Piece(Column.A, 1, Color.BLACK)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
            (Column.A, 1): other,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.KING_IN_CHECK
        )

    def test_is_short_castling_not_available14(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | |K|W|W|R|
           A B C D E F G H
        Check that if the F column is not empty, castling unavailable
        Check that if the G column is not empty, castling unavailable
        :return:
        """
        # F not empty
        king = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        other = Piece(Column.F, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
            (Column.F, 1): other,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.NOT_EMPTY_PATH
        )
        # G not empty
        other = Piece(Column.G, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
            (Column.G, 1): other,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.NOT_EMPTY_PATH
        )

    def test_is_short_castling_not_available15(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | |b|b| |
        1 | | | | |K| | |R|
           A B C D E F G H
        Check that if the F column is in check, castling unavailable
        Check that if the G column is in check, castling unavailable
        :return:
        """
        # Column F in check
        king = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        other = Rook(Column.F, 2, Color.BLACK)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
            (Column.F, 2): other,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.PATH_IN_CHECK
        )
        # Column G in check
        other = Rook(Column.G, 2, Color.BLACK)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
            (Column.G, 2): other,
        }
        assert (
            king.is_short_castling_valid(self.square_list, piece_list)
            == CastlingErrors.PATH_IN_CHECK
        )

    def test_is_long_castling_available(self):
        """
        |R| | | |K| | | |
         A B C D E F G H
        Check that a valid set-up return the square
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.A, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.VALID
        )

    def test_is_long_castling_not_available1(self):
        """
        |R| | | | | | | |
        | | | | |K|x|x| |
         A B C D E F G H
        Check that if the rook has moved, castling unavailable
        Check that if there is no rook, castling is unavailable
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.A, 2)
        # no rook
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 2): rook,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.ROOK_HAS_MOVED
        )
        # rook has moved
        rook.move_to(self.square_list[Column.A, 1], self.square_list, piece_list)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.ROOK_HAS_MOVED
        )

    def test_is_long_castling_not_available12(self):
        """
        Check that if the king has moved, castling unavailable
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.A, 1)
        king.has_moved = True
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.KING_HAS_MOVED
        )

    def test_is_long_castling_not_available13(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 |R| | | |K| | |B|
           A B C D E F G H
        Check that if the king is in check, castling unavailable
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.A, 1)
        other = Piece(Column.H, 1, Color.BLACK)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
            (Column.H, 1): other,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.KING_IN_CHECK
        )

    def test_is_long_castling_not_available14(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 |R|W|W|W|K| | | |
           A B C D E F G H
        Check that if the B column is not empty, castling unavailable
        Check that if the C column is not empty, castling unavailable
        Check that if the D column is not empty, castling unavailable
        :return:
        """
        # B not empty
        king = King(Column.E, 1)
        rook = Rook(Column.A, 1)
        other = Piece(Column.B, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
            (Column.B, 1): other,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.NOT_EMPTY_PATH
        )
        # C not empty
        other = Piece(Column.C, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
            (Column.C, 1): other,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.NOT_EMPTY_PATH
        )
        # D not empty
        other = Piece(Column.D, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
            (Column.D, 1): other,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.NOT_EMPTY_PATH
        )

    def test_is_long_castling_not_available15(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | |b|b| | | | |
        1 |R| | | |K| | | |
           A B C D E F G H
        Check that if the C column is in check, castling unavailable
        Check that if the D column is in check, castling unavailable
        :return:
        """
        # Column C in check
        king = King(Column.E, 1)
        rook = Rook(Column.A, 1)
        other = Rook(Column.C, 2, Color.BLACK)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
            (Column.C, 2): other,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.PATH_IN_CHECK
        )
        # Column D in check
        other = Rook(Column.D, 2, Color.BLACK)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
            (Column.D, 2): other,
        }
        assert (
            king.is_long_castling_valid(self.square_list, piece_list)
            == CastlingErrors.PATH_IN_CHECK
        )

    def test_short_castle(self):
        """
        1 | | | | |K| | |R|
           A B C D E F G H
        1 | | | | | |R|K| |
           A B C D E F G H
        Test that a valid castle does all the modifications
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.H, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.H, 1): rook,
        }
        king.short_castle(self.square_list, piece_list)
        assert (Column.H, 1) not in piece_list
        assert (Column.E, 1) not in piece_list
        assert king.column == Column.G
        assert king.row == 1
        assert king.has_moved
        assert rook.column == Column.F
        assert rook.row == 1
        assert rook.has_moved

    def test_invalid_short_castle(self):
        """
        Test that an invalid castle raises a InvalidMovementError
        :return:
        """
        king = King(Column.E, 1)
        piece_list = {
            (Column.E, 1): king,
        }
        with pytest.raises(InvalidMovementError):
            king.short_castle(self.square_list, piece_list)

    def test_long_castle(self):
        """
        1 |R| | | |K| | | |
           A B C D E F G H
        1 | | |K|R| | | | |
           A B C D E F G H
        Test that a valid castle does all the modifications
        :return:
        """
        king = King(Column.E, 1)
        rook = Rook(Column.A, 1)
        piece_list = {
            (Column.E, 1): king,
            (Column.A, 1): rook,
        }
        king.long_castle(self.square_list, piece_list)
        assert (Column.A, 1) not in piece_list
        assert (Column.E, 1) not in piece_list
        assert king.column == Column.C
        assert king.row == 1
        assert king.has_moved
        assert rook.column == Column.D
        assert rook.row == 1
        assert rook.has_moved

    def test_invalid_long_castle(self):
        """
        Test that an invalid castle raises a InvalidMovementError
        :return:
        """
        king = King(Column.E, 1)
        piece_list = {
            (Column.E, 1): king,
        }
        with pytest.raises(InvalidMovementError):
            king.long_castle(self.square_list, piece_list)
