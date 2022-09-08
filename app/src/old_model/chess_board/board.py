"""
Board class
"""
from itertools import product

from app.src.exceptions.invalid_move_error import InvalidMoveError
from app.src.exceptions.missing_king_error import MissingKingError
from app.src.logger import LOGGER
from app.src.old_model.chess_board.square import Square
from app.src.old_model.miscenaleous.color import Color
from app.src.old_model.miscenaleous.column import Column
from app.src.old_model.miscenaleous.game_state import GameState
from app.src.old_model.miscenaleous.move import Move, EmptyMove
from app.src.old_model.miscenaleous.utils import get_king
from app.src.old_model.pieces.bishop import Bishop
from app.src.old_model.pieces.king import King
from app.src.old_model.pieces.knight import Knight
from app.src.old_model.pieces.pawn import Pawn
from app.src.old_model.pieces.queen import Queen
from app.src.old_model.pieces.rook import Rook

logger = LOGGER


class Board:
    """
    Class that represent a chess board.
    Also contains the history of the game
    """

    def __init__(self):
        """
        Build a board instance
        """
        logger.info("Building board")
        self.squares = {}
        for (column, row) in product(Column, range(1, 9)):
            self.squares[(column, row)] = Square(column, row)
        self.piece_list = {}
        self.set_initial_config()
        self.player = Color.WHITE
        self.historic: [Move] = [EmptyMove()]
        self.state = GameState.RUNNING

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
        @return:
        """
        logger.info("Initial game config creation")
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
        Return the list of the available moves for the player that plays.
        Set the game state (win or draw)
        @return: List of Moves
        """
        logger.info("Call of available_moves")
        available_moves = []
        for piece in self.piece_list.values():
            if piece.color == self.player:
                available_moves.extend(
                    piece.available_moves(
                        self.squares,
                        self.piece_list,
                        self.historic[-1],
                    )
                )
        if not available_moves:
            logger.info("No available moves, end of the game")
            try:
                king = get_king(self.piece_list, self.player)
            except MissingKingError as error:
                logger.error("The king is missing")
                raise error
            if not king.is_in_check(self.squares, self.piece_list):
                logger.info("Stalemate")
                self.state = GameState.DRAW
            elif self.player == Color.WHITE:
                logger.info("Black win")
                self.state = GameState.BLACK_WIN
            else:
                logger.info("White win")
                self.state = GameState.WHITE_WIN
        return available_moves

    def apply_move(self, move: Move):
        """
        Apply a move
        Changes the player
        Assert that the move is valid
        Assert historic has been updated
        @param move:
        @return:
        """
        logger.info("Call of apply_move")
        if move not in self.available_moves_list():
            logger.error("Invalid move")
            raise InvalidMoveError(move)
        # Play the move
        self.piece_list[move.origin.column, move.origin.row].apply_move(
            move, self.squares, self.piece_list, self.historic[-1]
        )
        # Update the player who has to play
        self.player = Color.BLACK if self.player == Color.WHITE else Color.WHITE
        # Update the historic
        self.historic.append(move)
