"""
Abstract classes for movements
"""
from abc import ABC

from src.domain.classes.square import Square


class Move(ABC):
    """
    Abstract classes
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
