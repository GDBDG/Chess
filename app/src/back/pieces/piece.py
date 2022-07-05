"""
Piece classes
"""
from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.exceptions.row_error import RowError
from app.src.exceptions.unavailable_square_error import UnavailableSquareError


class Piece:
    """
    Generic class of a chess piece.
    Has no gaming meaning, but contains methods for all pieces
    """

    def __init__(self, column: Column, row: int, color: Color = Color.WHITE):
        """
        Constructor of piece
        :param row: between 1 and 8, column coordinate
        :param column: between A and H (Column enum), row
        :param color:
        """
        if not 1 <= row <= 8:
            raise RowError(row)
        self.column = column
        self.row = row
        self.color = color

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        Return all squares empty or with a piece in the opposite team
        Update the piece_list (it must be the piece_list of the board, and not a copy
        :return: list of Square
        """
        return [square for square in square_list.values() if ((square.column, square.row) not in piece_list.keys()) or
                piece_list[(square.column, square.row)].color != self.color]

    def move_to(self, destination: Square, square_list, piece_list):
        """
        Move the piece to a new square
        * Checks if the square is available
        :param piece_list:
        :param square_list: dict containing squares
        :param destination: instance of Square where self is moved
        :return: None
        """
        # Raises an exception if the asked destination is not available
        if destination not in self.available_squares(square_list, piece_list):
            raise UnavailableSquareError(destination)
        # Set new coordinates
        self.row = destination.row
        self.column = destination.column
