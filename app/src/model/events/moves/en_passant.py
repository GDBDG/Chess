"""
En passant moves
"""
from app.src.model.events.moves.move import Move
from app.src.model.game.square import Square
from app.src.model.pieces.piece import Piece


class EnPassant(Move):
    """
    Class for EnPassant
    """

    def apply_move(self, piece_dict: dict[Square, Piece]) -> bool:
        """
        Apply an En Passant capture
        Does no legal verification, and does not check that the moves is possible
        @param piece_dict: pieces in the game
        @return:
        """
        piece_dict[self.destination] = piece_dict[self.origin]
        piece_dict.pop(Square(self.destination.column, self.origin.row))
        piece_dict.pop(self.origin)
        return True
