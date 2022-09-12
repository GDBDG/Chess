"""
Abstract class for movements
"""
from abc import ABC

from app.src.model.game.square import Square
from app.src.model.pieces.piece import Piece


class Move(ABC):
    """
    Abstract class
    """

    def __init__(
        self,
        origin: Square,
        destination: Square,
    ):
        """
        Constructor
        @param origin: origin square
        @param destination: destination square
        """
        self.origin = origin
        self.destination = destination

    def is_legal(
        self,
        piece_dict: dict[Square, Piece],
    ) -> bool:
        """
        Return a boolean value indicating whether the move is legal or not.
        @return:
        """

    def apply_move(self):
        """
        Apply a move
        Moves the piece.
        @return:
        """

    def __eq__(self, other):
        return (
            self.origin == other.origin
            and self.destination == other.destination
            and type(other) == type(self)
        )

    def __repr__(self):
        return (
            f"{self.origin.column.name}{self.origin.row}"
            f"{self.destination.column.name}{self.destination.row}"
        )
