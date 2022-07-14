"""
Custom error, for invalid square
"""
from typing import Optional

from app.src.back.chess_board.square import Square

EN_PASSANT_UNAVAILABLE_MESSAGE = "En passant capture unavailable"


class InvalidMovementError(Exception):
    """
    Exception raised when square isn't valid. (Several rules)
    """

    def __init__(
        self, square: Optional[Square], detailedError: str = "Reason not specified"
    ):
        self.square = square
        self.message = f"Square ({self.square}) unavailable.\n{detailedError}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
