"""
Contains the game state (the pieces, and the associated methods)
"""
from app.src.exceptions.missing_king_error import MissingKingError
from app.src.logger import LOGGER
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color


class Board:
    """
    Contains the pieces, and the associated methods
    """

    def __init__(self):
        """
        Constructor
        """
        self.piece_dict = Board.set_initial_config()

    def get_current_color(
        self,
        origin: Square,
    ) -> Color:
        """
        Get the color of the piece origin, with the piece list and the coordinates
        @param origin: square with a piece
        @return:
        """
        try:
            return self.piece_dict[origin].color
        except KeyError as error:
            LOGGER.error("Tried to get the color of an empty square")
            raise error

    def get_king(self, color: Color) -> Square:
        """
        Return the King with the color <color> in the piece_list
        Raises an error if there is no King
        @param color: color of the king
        @return: the origin of the king
        """
        from app.src.model.pieces.king import King

        king = next(
            (
                square
                for square in self.piece_dict
                if type(self.piece_dict[square]) == King and self.piece_dict[square].color == color
            ),
            None,
        )
        if king is None:
            raise MissingKingError
        return king

    @staticmethod
    def set_initial_config():
        """
        Create an initial game config
        8 |R|k|B|Q|K|B|k|R|
        7 |p|p|p|p|p|p|p|p|
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 |p|p|p|p|p|p|p|p|
        1 |R|k|B|Q|K|B|k|R|
           A B C D E F G H
        @return:
        """
        from app.src.logger import LOGGER
        from app.src.model.game.square import Square
        from app.src.model.miscenaleous.color import Color
        from app.src.model.miscenaleous.column import Column
        from app.src.model.pieces.bishop import Bishop
        from app.src.model.pieces.king import King
        from app.src.model.pieces.knight import Knight
        from app.src.model.pieces.pawn import Pawn
        from app.src.model.pieces.queen import Queen
        from app.src.model.pieces.rook import Rook
        LOGGER.info("Initial game config creation")
        return {
            # White pieces
            Square(Column.A, 1): Rook(Color.WHITE),
            Square(Column.B, 1): Knight(Color.WHITE),
            Square(Column.C, 1): Bishop(Color.WHITE),
            Square(Column.D, 1): Queen(Color.WHITE),
            Square(Column.E, 1): King(Color.WHITE),
            Square(Column.F, 1): Bishop(Color.WHITE),
            Square(Column.G, 1): Knight(Color.WHITE),
            Square(Column.H, 1): Rook(Color.WHITE),
            Square(Column.A, 2): Pawn(Color.WHITE),
            Square(Column.B, 2): Pawn(Color.WHITE),
            Square(Column.C, 2): Pawn(Color.WHITE),
            Square(Column.D, 2): Pawn(Color.WHITE),
            Square(Column.E, 2): Pawn(Color.WHITE),
            Square(Column.F, 2): Pawn(Color.WHITE),
            Square(Column.G, 2): Pawn(Color.WHITE),
            Square(Column.H, 2): Pawn(Color.WHITE),
            # Black pieces
            Square(Column.A, 8): Rook(Color.BLACK),
            Square(Column.B, 8): Knight(Color.BLACK),
            Square(Column.C, 8): Bishop(Color.BLACK),
            Square(Column.D, 8): Queen(Color.BLACK),
            Square(Column.E, 8): King(Color.BLACK),
            Square(Column.F, 8): Bishop(Color.BLACK),
            Square(Column.G, 8): Knight(Color.BLACK),
            Square(Column.H, 8): Rook(Color.BLACK),
            Square(Column.A, 7): Pawn(Color.BLACK),
            Square(Column.B, 7): Pawn(Color.BLACK),
            Square(Column.C, 7): Pawn(Color.BLACK),
            Square(Column.D, 7): Pawn(Color.BLACK),
            Square(Column.E, 7): Pawn(Color.BLACK),
            Square(Column.F, 7): Pawn(Color.BLACK),
            Square(Column.G, 7): Pawn(Color.BLACK),
            Square(Column.H, 7): Pawn(Color.BLACK),
        }
