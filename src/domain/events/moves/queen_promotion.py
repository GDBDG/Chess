"""
Queen Promotion.
Promotion: when a pawn reaches the last line: can turn into another piece.
Simplification: only queen and knight (bishop and rook are useless)
"""
from src.domain.classes.pieces.piece import Piece
from src.domain.classes.pieces.queen import Queen
from src.domain.classes.square import Square
from src.domain.events.moves.pawn_move import PawnMove


class QueenPromotion(PawnMove):
    """
    Queen promotion classes.
    """

    def __repr__(self):
        return (
            f"{self.origin.column.name}{self.origin.row}"
            f"{self.destination.column.name}{self.destination.row}"
            f"=Q"
        )

    def apply_move(self, piece_dict: dict[Square, Piece]) -> bool:
        """
        Replace the pawn by a queen
        @param piece_dict: pieces in the game
        @return: false : no capture
        """
        piece_dict[self.destination] = Queen(piece_dict[self.origin].color)
        piece_dict.pop(self.origin)
        return False
