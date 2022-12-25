"""
Queen Promotion.
Promotion: when a pawn reaches the last line: can turn into another piece.
Simplification: only queen and knight (bishop and rook are useless)
"""
from src.CHESS.domain.classes.pieces.piece import Piece
from src.CHESS.domain.classes.pieces.queen import Queen
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.events.moves.pawn_move import PawnMove


class QueenPromotionCapture(PawnMove):
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
        @return: True: capture
        """
        piece_dict[self.destination] = Queen(piece_dict[self.origin].color)
        piece_dict.pop(self.origin)
        return True