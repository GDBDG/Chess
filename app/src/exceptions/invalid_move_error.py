"""
Custom error : invalid move
"""
from app.src.model.miscenaleous.move import Move


class InvalidMoveError(ValueError):
    """
    Custom Error class
    """

    def __init__(self, move: Move, reason: str = ""):
        """
        Constructor
        @param move: move that is invalid,
        """
        super().__init__()
        self.message = f"{move} is invalid:\n{reason}"

    def __repr__(self):
        return self.message
