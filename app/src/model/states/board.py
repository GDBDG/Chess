"""
Contains the game state (the pieces, and the associated methods)
"""
from itertools import product

from app.src.exceptions.missing_king_error import MissingKingError
from app.src.logger import LOGGER
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.pieces.bishop import Bishop
from app.src.model.classes.pieces.king import King
from app.src.model.classes.pieces.knight import Knight
from app.src.model.classes.pieces.pawn import Pawn
from app.src.model.classes.pieces.queen import Queen
from app.src.model.classes.pieces.rook import Rook
from app.src.model.classes.square import Square


class Board:
    """
    Contains the pieces, and the associated methods
    """

    def __init__(self):
        """
        Constructor
        """
        self.piece_dict = Board.initial_config()

    def get_piece_type_counter(self):
        """
        Return a dict with the number of each piece in the game.
        One counter for both players
        @return:
        """
        piece_counter = {Bishop: 0, King: 0, Knight: 0, Pawn: 0, Queen: 0, Rook: 0}
        for piece in self.piece_dict.values():
            piece_counter[piece.__class__] += 1
        return piece_counter

    def are_bishop_in_dead_position(self) -> bool:
        """
        Must be called if there are 2 bishops and 2 kings in the game.
        (Only purpose: to detect a draw in game)
        Return if the bishops are in a dead position
        (king and bishop against king and bishop, with both bishops on squares of the same color)
        @return:
        """
        if self.get_piece_type_counter() != {
            Bishop: 2,
            King: 2,
            Knight: 0,
            Pawn: 0,
            Queen: 0,
            Rook: 0,
        }:
            return False
        square_color = []
        bishop_color = []
        for square, piece in self.piece_dict.items():
            print(piece)
            if isinstance(piece, Bishop):
                square_color.append(square.square_color())
                bishop_color.append(piece.color)
        return square_color[0] == square_color[1] and bishop_color[0] != bishop_color[1]

    def dict_to_bit(self) -> int:
        """
        Return the bit value of a board
        a square state is encoded on 4 bits abcd
        a: 1 if white, 0 other
        bcd: 001 : bishop 9 | 1
        bcd: 010 : king  a | 2
        bcd: 011 : knight b | 3
        bcd: 100 : pawn c | 4
        bcd: 101 : queen d | 5
        bcd: 110 : rook e | 6
        bcd: 111 : piece (only useful for tests)
        abcd: 0000 : empty square
        config history bit value : A1A2...H8
        @return:
        """
        config_value = 0b0
        for (column, row) in product(Column, range(1, 9)):
            if Square(column, row) not in self.piece_dict:
                config_value = config_value << 4
            else:
                config_value = (config_value << 4) + self.piece_dict[
                    Square(column, row)
                ].bit_value()
        return config_value

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
        king = next(
            (
                square
                for square in self.piece_dict
                if type(self.piece_dict[square]) == King
                   and self.piece_dict[square].color == color
            ),
            None,
        )
        if king is None:
            raise MissingKingError
        return king

    @staticmethod
    def initial_config():
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
