"""
Movement (for historic)
Store square destination, piece, and origin square
Method to know if a movement allow an en passant capture
"""
from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.piece_type import PieceType


class Move:
    """
    Class Move : standard move
    """

    def __init__(self, origin: Square, destination: Square, piece_type: PieceType):
        """
        Constructor
        :param origin: origin square (Square)
        :param destination: destination square (Square)
        :param piece_type: type of the piece that has moved
        """
        self.origin = origin
        self.destination = destination
        self.piece_type = piece_type

    def __hash__(self):
        return hash(repr(self))

    def allow_en_passant(self) -> bool:
        """
        Return if the move correspond to a pawn first move
        :return:
        """

        return (
            self.piece_type == PieceType.PAWN
            and abs(self.origin.row - self.destination.row) == 2
        )

    def __eq__(self, other):
        return (
            type(self) == type(other)
            and self.origin == other.origin
            and self.destination == other.destination
            and self.piece_type == other.piece_type
        )

    def __repr__(self):
        return (
            f"Origin : {self.origin}, \nDestination : {self.destination}\n"
            f"PieceType : {self.piece_type}"
        )


class EmptyMove(Move):
    """
    Used only to initialize a game.
    """

    def __init__(self):
        super().__init__(Square(Column.A, 1), Square(Column.A, 1), PieceType.PIECE)

    def allow_en_passant(self) -> bool:
        return False


class ShortCastling(Move):
    """
    Short Castling Move
    """

    def __init__(self, origin: Square, destination: Square):
        """
        Constructor
        :param origin: origin square (Square)
        :param destination: destination square (Square)
        :param piece_type: type of the piece that has moved
        """
        super().__init__(origin, destination, PieceType.KING)

    def allow_en_passant(self) -> bool:
        return False


class LongCastling(Move):
    """
    Short Castling Move
    """

    def __init__(self, origin: Square, destination: Square):
        """
        Constructor
        :param origin: origin square (Square)
        :param destination: destination square (Square)
        :param piece_type: type of the piece that has moved
        """
        super().__init__(origin, destination, PieceType.KING)

    def allow_en_passant(self) -> bool:
        return False


class EnPassant(Move):
    """
    En Passant Capture
    """

    def __init__(self, origin: Square, destination: Square):
        """
        Constructor
        :param origin: origin square (Square)
        :param destination: destination square (Square)
        :param piece_type: type of the piece that has moved
        """
        super().__init__(origin, destination, PieceType.PAWN)

    def allow_en_passant(self) -> bool:
        return False


class Promotion(Move):
    """
    Promotion Move, the piece_type store the new type of the pawn
    """

    def allow_en_passant(self) -> bool:
        return False
