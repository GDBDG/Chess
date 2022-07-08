"""
Piece classes
"""
from itertools import product

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
        return [
            square
            for square in square_list.values()
            if ((square.column, square.row) not in piece_list.keys())
            or piece_list[(square.column, square.row)].color != self.color
        ]

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

    def _available_square_on_side_line(
        self,
        columns: [Column],
        rows: [int],
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on only one side line (for ex on the right)
        For that : takes a lists of columns, that must correspond to the columns in the right
        or left of the piece, and its row
        Or, take a list of rows, that correspond to the rows on itertools or underneath self,
        and its column
        To make it generic, both are list
        In practice, make the product of columns and rows, so one must have only one element to
        have a meaning with a rook.
        :param columns: list of column to iterate on,
        :param rows: list of rows to iterate on
        :param square_list: list of squares available
        :param piece_list: list of pieces (represents the pieces in the game)
        :return: square_list of available squares designated by th product of columns and rows
        """
        available_squares = []
        for column, row in product(columns, rows):
            # if there is a piece on the square
            if (column, row) in piece_list:
                # if the piece can take the other piece
                if piece_list[column, row].color != self.color:
                    available_squares.append(square_list[column, row])
                break
            # if there is no piece on the square
            available_squares.append(square_list[column, row])
        return available_squares

    def _available_squares_on_right(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: square_list of available squares
        :param piece_list: list of pieces (represent the pieces in the game)
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value + 1, 9)),
            [self.row],
            square_list,
            piece_list,
        )

    def _available_squares_on_left(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: square_list of available squares
        :param piece_list: list of pieces (represent the pieces in the game)
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value - 1, 0, -1)),
            [self.row],
            square_list,
            piece_list,
        )

    def _available_squares_upper(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: square_list of available squares
        :param piece_list: list of pieces (represent the pieces in the game)
        :return:
        """
        return self._available_square_on_side_line(
            [self.column],
            range(self.row + 1, 9),
            square_list,
            piece_list,
        )

    def _available_squares_below(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: square_list of available squares
        :param piece_list: list of pieces (represent the pieces in the game)
        :return:
        """
        return self._available_square_on_side_line(
            [self.column],
            range(self.row - 1, 0, -1),
            square_list,
            piece_list,
        )
