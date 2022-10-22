"""
Queen
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.pieces.piece import Piece
from app.src.model.events.moves.queen_move import QueenMove


class Queen(Piece):
    """
    Queen classes
    """

    move = QueenMove

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1101 or 0101
        """
        return 0b1101 if self.color == Color.WHITE else 0b0101

    def __repr__(self):
        return "Q" if self.color == Color.WHITE else "q"
