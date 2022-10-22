"""
Short castling
"""
from app.src.model.events.moves.move import Move
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column
from app.src.model.pieces.piece import Piece


class ShortCastling(Move):
    """
    Short castling class.
    origin: the king
    """

    def __init__(self, origin: Square):
        """
        No need to give the destination
        """
        super().__init__(origin, Square(Column.G, origin.row))

    def apply_move(self, piece_dict: dict[Square, Piece]) -> bool:
        """
        Apply the long castling.
        Does no verification.
        @param piece_dict:
        @return:
        """
        # Moves the king
        piece_dict[Square(Column.G, self.origin.row)] = piece_dict.pop(self.origin)
        # Moves the Rook
        piece_dict[Square(Column.F, self.origin.row)] = piece_dict.pop(
            Square(Column.H, self.origin.row)
        )
        return False
