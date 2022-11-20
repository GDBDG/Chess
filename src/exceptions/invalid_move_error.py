"""
Custom error : invalid moves
"""
from src.domain.events.moves.move import Move


class InvalidMoveError(ValueError):
    """
    Custom Error classes
    """

    def __init__(self, move: Move, reason: str = ""):
        """
        Constructor
        @param move: moves that is invalid,
        """
        super().__init__()
        self.message = f"{move} is invalid:\n{reason}"

    def __repr__(self):
        return self.message
