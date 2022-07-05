"""
Tests square class
"""
from itertools import product

import pytest

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.column import Column
from app.src.exceptions.row_error import RowError


class TestSquare:
    """
    Testing class
    """
    def test_init_valid_square(self):
        """
        Check tha it is to instantiate all the valid squares
        :return: None
        """
        for row, column in product(range(1, 9), Column):
            square = Square(column, row)
            assert square.column == column
            assert square.row == row

    def test_invalid_row(self):
        """
        Check that a RowError is raised if invalid row is given for init
        :return: None
        """
        with pytest.raises(RowError):
            Square(Column.A, 9)
