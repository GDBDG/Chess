"""
King
"""

from src.domain.classes.const.color import Color
from src.domain.classes.pieces.piece import Piece
from src.domain.events.moves.king_move import KingMove


class King(Piece):
    """
    King classes
    """

    move = KingMove

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1010 or 0010
        """
        return 0b1010 if self.color == Color.WHITE else 0b0010

    def __repr__(self):
        return "K" if self.color == Color.WHITE else "k"
