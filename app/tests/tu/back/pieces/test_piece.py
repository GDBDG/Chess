"""
Tests for Piece class
"""
from itertools import product

import pytest

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.piece import Piece
from app.src.back.pieces.rook import Rook
from app.src.exceptions.row_error import RowError
from app.src.exceptions.unavailable_square_error import UnavailableSquareError


class TestPiece:
    """
    test class
    """

    piece_list = {
        (Column.A, 1): Piece(Column.A, 1),
        (Column.A, 2): Piece(Column.A, 2),
        (Column.A, 3): Piece(Column.A, 3, Color.BLACK),
    }
    square_list = {(Column.A, i): Square(Column.A, i) for i in range(1, 9)}

    def test_valid_init(self):
        """
        Test all valid instantiation
        :return: None
        """
        for row, column, color in product(range(1, 9), Column, Color):
            piece = Piece(column, row, color)
            assert piece.column == column
            assert piece.row == row
            assert piece.color == color

    def test_invalid_instantiation(self):
        """
        Test if an incorrect row is given
        assert RowError is raised
        :return: None
        """
        with pytest.raises(RowError):
            Piece(Column.B, 9)

    def test_available_squares(self):
        """
        test that available squares return correct square_list
        :return: None
        """
        expected_list = [self.square_list[Column.A, i] for i in range(3, 9)]
        assert (
            self.piece_list[Column.A, 1].available_squares(
                self.square_list, self.piece_list
            )
            == expected_list
        )

    def test_move_to_valid_destination(self):
        """
        Test move_to_destination, when a correct destination is provided
        :return: None
        """
        piece = self.piece_list[Column.A, 1]
        piece.move_to(self.square_list[Column.A, 3], self.square_list, self.piece_list)
        assert piece.row == 3 and piece.column == Column.A
        assert piece.has_moved

    def test_move_to_invalid_destination(self):
        """
        test move_to_destination with incorrect destination (square not in square list,
        or friendly piece in destination)
        :return: None
        """
        piece = self.piece_list[Column.A, 1]
        with pytest.raises(UnavailableSquareError):
            piece.move_to(Square(Column.B, 1), self.square_list, self.piece_list)
        with pytest.raises(UnavailableSquareError):
            piece.move_to(Square(Column.A, 2), self.square_list, self.piece_list)

    def test_add_square_valid_coordinates(self):
        """
        test _add_square with valid coordinates
        :return: None
        """
        available_squares = []
        Piece._add_square(1, 7, self.square_list, available_squares)
        assert available_squares == [self.square_list[Column.A, 7]]

    def test_add_square_invalid_column(self):
        """
        test _add_square with invalid column
        :return: None
        """
        available_squares = []
        Piece._add_square(9, 7, self.square_list, available_squares)
        assert not available_squares

    def test_add_square_invalid_row(self):
        """
        test _add_square with invalid column
        :return: None
        """
        available_squares = []
        Piece._add_square(1, 9, self.square_list, available_squares)
        assert not available_squares

    def test_is_square_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |W| | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return:
        """
        other = Piece(Column.F, 6, Color.BLACK)
        other2 = Piece(Column.C, 6)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.F, 6): other,
            (Column.C, 6): other2,
        }
        assert Piece.is_square_in_check(
            Color.WHITE, square_list[Column.D, 4], square_list, piece_list
        )

    def test_is_square_not_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return:
        """
        other = Rook(Column.F, 6, Color.BLACK)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.F, 6): other,
        }
        assert not Piece.is_square_in_check(
            Color.WHITE, square_list[Column.D, 4], square_list, piece_list
        )

    def test_is_square_not_in_check2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |B| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return:
        """
        other = Rook(Column.D, 4, Color.BLACK)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): other,
        }
        assert not Piece.is_square_in_check(
            Color.WHITE, square_list[Column.D, 4], square_list, piece_list
        )

    def test_is_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |W| | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return:
        """
        piece = Piece(Column.D, 4)
        other = Piece(Column.F, 6, Color.BLACK)
        other2 = Piece(Column.C, 6)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other,
            (Column.C, 6): other2,
        }
        assert piece.is_in_check(
            square_list, piece_list
        )

    def test_is_not_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return:
        """
        piece = Piece(Column.D, 4)
        other = Rook(Column.F, 6, Color.BLACK)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other,
        }
        assert not piece.is_in_check(
            square_list, piece_list
        )
