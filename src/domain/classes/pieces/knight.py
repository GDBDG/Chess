"""
Knight
"""

from src.domain.classes.const.color import Color
from src.domain.classes.pieces.piece import Piece
from src.domain.events.moves.knight_move import KnightMove


class Knight(Piece):
    """
    Knight classes
    """

    move = KnightMove

    def bit_value(self) -> int:
        """
        Return the bit value, used for the piece_dict hash
        @return: 1011 or 0011
        """
        return 0b1011 if self.color == Color.WHITE else 0b0011

    def __repr__(self) -> str:
        return "KN" if self.color == Color.WHITE else "kn"
