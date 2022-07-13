"""
Movement (for historic)
Store square destination, piece, and origin square
Method to know if a movement allow an en passant capture
"""


class Move:
    """
    Class Move
    """

    def __init__(self, origin, destination, piece):
        """
        Constructor
        :param origin: origin square (Square)
        :param destination: destination square (Square)
        :param piece: Piece instance that has moved
        """
        self.origin = origin
        self.destination = destination
        self.piece = piece

    def allow_en_passant(self) -> bool:
        """
        Return if the move correspond to a pawn first move
        :return:
        """
        from app.src.back.pieces.pawn import Pawn

        return (
            isinstance(self.piece, Pawn)
            and abs(self.origin.row - self.destination.row) == 2
        )
