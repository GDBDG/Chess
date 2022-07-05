"""
square class
"""
from app.src.back.miscenaleous.column import Column
from app.src.exceptions.row_error import RowError


class Square:
    """
    Class tha represent a square in a chass game
    Contains coordinates, and the piece on it if there is one
    """

    def __init__(self, column: Column, row: int):
        """
        Build the instance
        :param column: column value (between 1 and 8)
        :param row: row Value
        """
        if not 1 <= row <= 8:
            raise RowError(row)
        self.column = column
        self.row = row
