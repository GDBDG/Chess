"""
Tests for class Board
"""
from app.src.model.chess_board.board import Board
from app.src.model.constantes import SQUARE_NUMBER


class TestBoard:
    """
    Testing class
    """

    board = Board()

    def test_number_squares(self):
        """
        Assert tha there is the right number of squares in the board
        :return: None
        """
        assert len(self.board.squares.items()) == SQUARE_NUMBER
