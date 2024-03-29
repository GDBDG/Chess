"""
Bishop
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.pieces.piece import Piece
from app.src.model.events.moves.bishop_move import BishopMove


class Bishop(Piece):
    """
    Bishop classes
    """

    move = BishopMove

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1001 or 0001
        """
        return 0b1001 if self.color == Color.WHITE else 0b0001

    def __repr__(self):
        return "B" if self.color == Color.WHITE else "b"
