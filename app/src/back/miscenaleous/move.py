"""
Movement (for historic)
Store square destination, piece, and origin square
Method to know if a movement allow an en passant capture
"""
from app.src.back.miscenaleous.piece_type import PieceType


class Move:
    """
    Class Move
    """

    def __init__(self, origin, destination, piece_type: PieceType):
        """
        Constructor
        :param origin: origin square (Square)
        :param destination: destination square (Square)
        :param piece_type: type of the piece that has moved
        """
        self.origin = origin
        self.destination = destination
        self.piece_type = piece_type

    def allow_en_passant(self) -> bool:
        """
        Return if the move correspond to a pawn first move
        :return:
        """

        return (
            self.piece_type == PieceType.PAWN
            and abs(self.origin.row - self.destination.row) == 2
        )
