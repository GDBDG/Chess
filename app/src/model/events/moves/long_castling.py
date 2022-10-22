"""
Long castling
"""
from app.src.model.classes.pieces.piece import Piece
from app.src.model.events.moves.move import Move
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column


class LongCastling(Move):
    """
    Long castling classes.
    origin: the king
    """

    def __init__(self, origin: Square):
        """
        No needto give the destination
        @param origin:
        """
        super().__init__(origin, Square(Column.C, origin.row))

    def apply_move(self, piece_dict: dict[Square, Piece]) -> bool:
        """
        Apply the long castling.
        Does no verification.
        @param piece_dict:
        @return:
        """
        # Moves the king
        piece_dict[Square(Column.C, self.origin.row)] = piece_dict.pop(self.origin)
        # Moves the Rook
        piece_dict[Square(Column.D, self.origin.row)] = piece_dict.pop(
            Square(Column.A, self.origin.row)
        )
        return False
