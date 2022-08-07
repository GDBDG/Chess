"""
square class
"""
from app.src.exceptions.row_error import RowError
from app.src.logger import LOGGER
from app.src.model.miscenaleous.column import Column

logger = LOGGER


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
            logger.error("Row must be between 1 and 8 to initiate square")
            raise RowError(row)
        self.column: Column = column
        self.row = row

    def __repr__(self):
        return f"({self.column.name},{self.row})"
