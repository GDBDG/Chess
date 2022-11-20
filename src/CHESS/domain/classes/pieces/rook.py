"""
Rook
"""
from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.pieces.piece import Piece
from src.CHESS.domain.events.moves.rook_move import RookMove


class Rook(Piece):
    """
    Rook classes
    """

    move = RookMove

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1110 or 0100
        """
        return 0b1110 if self.color == Color.WHITE else 0b0110

    def __repr__(self):
        return "R" if self.color == Color.WHITE else "r"
