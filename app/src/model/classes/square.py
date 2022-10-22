"""
Square:
Row and column
"""
from app.src.exceptions.row_error import RowError
from app.src.logger import LOGGER
from app.src.model.miscenaleous.column import Column


class Square:
    """
    Class tha represent a square in a chass game
    Contains coordinates, and the piece on it if there is one
    """

    def __init__(self, column: Column, row: int):
        """
        Build the instance
        @param column: column value (between 1 and 8)
        @param row: row Value
        """
        if not 1 <= row <= 8:
            LOGGER.error("Row must be between 1 and 8 to initiate square")
            raise RowError(row)
        self.column: Column = column
        self.row = row

    @staticmethod
    def add_square(column: int, row: int, available_squares):
        """
        Add the square with coordinate column and row in available_squares
        if it is in square_list
        @param row: row coordinate int value
        @param column: column coordinate (int value)
        @param available_squares: a list of square where the square will be added
        """
        if 1 <= column <= 8 and 1 <= row <= 8:
            available_squares.append(Square(Column(column), row))

    def __repr__(self):
        return f"({self.column.name},{self.row})"

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def __hash__(self):
        return hash((self.column, self.row))
