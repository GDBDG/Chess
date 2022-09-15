"""
Abstract class for movements
"""
import copy
from abc import ABC

from app.src.model.game.square import Square
from app.src.model.miscenaleous.utils import get_king
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
        Applies the move in a copy, and check if the king is in the destination of opposite moves
        @return:
        """
        from app.src.model.available_move_getter.available_moves import is_square_in_check
        piece_dict_copy = copy.deepcopy(piece_dict)
        current_color = piece_dict_copy[self.origin].color
        king_square = get_king(piece_dict_copy, current_color)
        self.apply_move(piece_dict_copy)
        return not is_square_in_check(current_color, king_square, piece_dict_copy)

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
