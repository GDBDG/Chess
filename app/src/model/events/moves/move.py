"""
Abstract class for movements
"""
import copy
from abc import ABC

from app.src.model.game.board import Board
from app.src.model.game.square import Square


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

    def is_move_legal(
        self,
        board: Board,
        historic=None
    ) -> bool:
        """
        Return a boolean value indicating whether the moves is legal or not.
        Applies the moves in a copy, and check if the king is in the destination of opposite moves
        @return:
        """
        board_copy = copy.deepcopy(board)
        current_color = board_copy.piece_dict[self.origin].color
        self.apply_move(board_copy)
        king_square = board_copy.get_king(current_color)
        from app.src.model.miscenaleous.utils import is_square_in_check
        return not is_square_in_check(current_color, king_square, board_copy, historic)

    def apply_move(self, board: Board) -> bool:
        """
        Apply a moves
        Moves the piece.
        (Does no legal verification
        @return: True if the moves is a capture
        """
        capture = self.destination in board.piece_dict
        board.piece_dict[self.destination] = board.piece_dict[self.origin]
        board.piece_dict.pop(self.origin)
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
