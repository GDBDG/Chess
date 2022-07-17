"""
Custom error : invalid move
"""
from app.src.model.miscenaleous.move import Move


class InvalidMoveError(ValueError):
    """
    Custom Error class
    """
    def __init__(self, move: Move):
        """
        Constructor
        :param move: move that is invalid,
        """
        self.message = f"{move} is invalid:"

    def __repr__(self):
        return self.message