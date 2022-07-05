"""
Tests for Piece class
"""
from itertools import product

import pytest

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.piece import Piece
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
