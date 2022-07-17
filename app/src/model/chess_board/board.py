"""
Board class
"""
from itertools import product

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.king import King
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


class Board:
    """
    Class that represent a chess board.
    Also contains the history of the game
    """

    def __init__(self):
        """
        Build a board instance
        """
        self.piece_list = {}
        self.squares = {}
        for (column, row) in product(Column, range(1, 9)):
            self.squares[(row, column)] = Square(column, row)
        self.set_initial_config()
        self.player = Color.WHITE
        self.historic: [Move] = []

    def set_initial_config(self):
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
        :return:
        """
        self.piece_list = {
            # White pieces
            (Column.A, 1): Rook(Column.A, 1),
            (Column.B, 1): Knight(Column.B, 1),
            (Column.C, 1): Bishop(Column.C, 1),
            (Column.D, 1): Queen(Column.D, 1),
            (Column.E, 1): King(Column.E, 1),
            (Column.F, 1): Bishop(Column.F, 1),
            (Column.G, 1): Knight(Column.G, 1),
            (Column.H, 1): Rook(Column.H, 1),
            (Column.A, 2): Pawn(Column.A, 2),
            (Column.B, 2): Pawn(Column.B, 2),
            (Column.C, 2): Pawn(Column.C, 2),
            (Column.D, 2): Pawn(Column.D, 2),
            (Column.E, 2): Pawn(Column.E, 2),
            (Column.F, 2): Pawn(Column.F, 2),
            (Column.G, 2): Pawn(Column.G, 2),
            (Column.H, 2): Pawn(Column.H, 2),
            # Black pieces
            (Column.A, 8): Rook(Column.A, 8, Color.BLACK),
            (Column.B, 8): Knight(Column.B, 8, Color.BLACK),
            (Column.C, 8): Bishop(Column.C, 8, Color.BLACK),
            (Column.D, 8): Queen(Column.D, 8, Color.BLACK),
            (Column.E, 8): King(Column.E, 8, Color.BLACK),
            (Column.F, 8): Bishop(Column.F, 8, Color.BLACK),
            (Column.G, 8): Knight(Column.G, 8, Color.BLACK),
            (Column.H, 8): Rook(Column.H, 8, Color.BLACK),
            (Column.A, 7): Pawn(Column.A, 7, Color.BLACK),
            (Column.B, 7): Pawn(Column.B, 7, Color.BLACK),
            (Column.C, 7): Pawn(Column.C, 7, Color.BLACK),
            (Column.D, 7): Pawn(Column.D, 7, Color.BLACK),
            (Column.E, 7): Pawn(Column.E, 7, Color.BLACK),
            (Column.F, 7): Pawn(Column.F, 7, Color.BLACK),
            (Column.G, 7): Pawn(Column.G, 7, Color.BLACK),
            (Column.H, 7): Pawn(Column.H, 7, Color.BLACK),
        }

    def available_moves_list(self) -> [Move]:
        """
        Return the list of the available moves for the player that plays
        :return: List of Moves
        """
        available_moves = []
        for piece in self.piece_list.values():
            pass
