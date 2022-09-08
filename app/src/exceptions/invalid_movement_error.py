"""
Custom error, for invalid square
"""
from typing import Optional

from app.src.old_model.chess_board.square import Square

EN_PASSANT_UNAVAILABLE_MESSAGE = "En passant capture unavailable"


class InvalidMovementError(Exception):
    """
    Exception raised when square isn't valid. (Several rules)
    """

    def __init__(
        self, square: Optional[Square], detailed_error: str = "Reason not specified"
    ):
        self.square = square
        self.message = f"Square ({self.square}) unavailable.\n{detailed_error}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
