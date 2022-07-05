"""
Board class
"""
from itertools import product

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.column import Column


class Board:
    """
    Class that represent a chess board.
    Also contains the history of the game
    """
    def __init__(self):
        """
        Build a board instance
        """
        self.squares = {}
        for (column, row) in product(Column, range(1, 9)):
            self.squares[(row, column)] = Square(column, row)
        self.history = None
        self.piece_list = {}

