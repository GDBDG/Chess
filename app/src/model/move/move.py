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

    def apply_move(self, piece_dict: dict[Square, Piece]) -> bool:
        """
        Apply a move
        Moves the piece.
        (Does no legal verification
        @return: True if the move is a capture
        """
        capture = self.destination in piece_dict
        piece_dict[self.destination] = piece_dict[self.origin]
        piece_dict.pop(self.origin)
        return capture

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
