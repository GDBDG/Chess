"""
Game implementation.
Manage the game and store the current state
"""
import copy
from itertools import product

from app.src.exceptions.invalid_move_error import InvalidMoveError
from app.src.logger import LOGGER
from app.src.model.available_move_getter._available_squares_getter import (
    _available_squares_bishop,
    _available_squares_knight,
    _available_squares_queen,
    _available_squares_rook,
    _available_squares_king,
)
from app.src.model.available_move_getter.available_moves import (
    _get_pawn_first_movement,
    _get_pawn_forward_moves,
    _get_pawn_capture_moves,
)
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.game_state import GameState
from app.src.model.miscenaleous.utils import get_king
from app.src.model.move.bishop_move import BishopMove
from app.src.model.move.king_move import KingMove
from app.src.model.move.knight_move import KnightMove
from app.src.model.move.move import Move
from app.src.model.move.queen_move import QueenMove
from app.src.model.move.rook_move import RookMove
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.king import King
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


class Game:
    """
    Class that represent a chess board.
    Also contains the history of the game
    """

    def __init__(self):
        """
        Build a board instance
        """
        LOGGER.info("Build a game instance")
        self.piece_dict: dict[Square, Piece] = {}
        self.set_initial_config()
        self.player = Color.WHITE
        self.move_historic: [Move] = []
        self.config_history = {}
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
        LOGGER.info("Initial game config creation")
        self.piece_dict = {
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

    def available_moves_list(self) -> [Move]:
        """
        Return the list of the available moves for the player that plays.
        @return: List of Moves
        """
        LOGGER.info("Call of available_moves")
        available_moves = []
        for square, piece in self.piece_dict.items():
            if piece.color == self.player:
                available_moves.extend(
                    self.square_available_moves(
                        square,
                        legal_verification=True,
                    )
                )
        return available_moves

    def apply_move(self, move: Move):
        """
        Apply a move
        Changes the player
        Assert that the move is valid
        Assert historic has been updated
        Update the game state
        @param move:
        @return:
        """
        LOGGER.info("Call of apply_move")
        if move not in self.available_moves_list():
            LOGGER.error("Invalid move")
            raise InvalidMoveError(move)
        # Play the move
        move.apply_move(self.piece_dict)
        # Update the player who has to play
        self.player = Color.BLACK if self.player == Color.WHITE else Color.WHITE
        # Update the historic
        self.move_historic.append(move)
        self.update_config_history()
        # Update the game state
        # TODO

    def update_config_history(self):
        """
        Update the configuration history
        Use a custom hash from the piece_dict
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
        # Calcul the config bit value
        config_value = 0b0
        for (column, row) in product(Column, range(1, 9)):
            if Square(column, row) not in self.piece_dict:
                config_value = config_value << 4
            else:
                config_value = (config_value << 4) + self.piece_dict[
                    Square(column, row)
                ].bit_value()
        # Update the history
        if config_value in self.config_history:
            self.config_history[config_value] += 1
            if self.config_history[config_value] == 3:
                self.state = GameState.DRAW
                LOGGER.info("Draw with threefold rule")
        else:
            self.config_history[config_value] = 1

    def square_available_moves(
        self,
        origin: Square,
        legal_verification=False,
    ) -> [Move]:
        """
        Return a list with all the available moves from origin
        @param legal_verification: if a legal verification on the moves must be done
        @param origin: Square origin for the move
        @return: a list with the available moves from origin
        """
        # pylint: disable=R0916
        LOGGER.info("Get available moves called for bishop")
        origin_piece = self.piece_dict[origin]
        available_moves = []
        if type(origin_piece) == Bishop:
            available_moves.extend(
                [
                    BishopMove(origin, destination)
                    for destination in _available_squares_bishop(
                    origin, self.piece_dict
                )
                ]
            )
        elif type(origin_piece) == Knight:
            available_moves.extend(
                [
                    KnightMove(origin, destination)
                    for destination in _available_squares_knight(
                    origin, self.piece_dict
                )
                ]
            )
        elif type(origin_piece) == Queen:
            available_moves.extend(
                [
                    QueenMove(origin, destination)
                    for destination in _available_squares_queen(origin, self.piece_dict)
                ]
            )
        elif type(origin_piece) == Rook:
            available_moves.extend(
                [
                    RookMove(origin, destination)
                    for destination in _available_squares_rook(origin, self.piece_dict)
                ]
            )
        # king
        elif type(origin_piece) == King:
            available_moves.extend(
                [
                    KingMove(origin, destination)
                    for destination in _available_squares_king(origin, self.piece_dict)
                ]
            )
        # pawn
        elif type(origin_piece) == Pawn:
            # First movement
            available_moves = _get_pawn_first_movement(origin, self.piece_dict)
            # Forward move
            available_moves.extend(_get_pawn_forward_moves(origin, self.piece_dict))
            # Capture on the right
            available_moves.extend(_get_pawn_capture_moves(origin, self.piece_dict))
            return available_moves
        else:
            raise ValueError("Unknown pieces in origin")
        # Remove moves if they are illegal
        if legal_verification:
            return [move for move in available_moves if self.is_move_legal(move)]
        return available_moves

    def is_square_in_check(self, color: Color, square: Square) -> bool:
        """
        Return a boolean indicating if a piece in a different color can move
        to square (indicates if a piece of color *color* is in check)
        @param color: color of the piece that we check if it can be taken
        @param square: the square where we check if it can be taken
        @return: boolean
        """
        return any(
            piece.color != color
            and square
            in list(map(lambda x: x.destination, self.square_available_moves(origin)))
            for origin, piece in self.piece_dict.items()
        )

    def is_move_legal(
        self,
        move: Move,
    ) -> bool:
        """
        Return a boolean value indicating whether the move is legal or not.
        Applies the move in a copy, and check if the king is in the destination of opposite moves
        @return:
        """
        game_copy = copy.deepcopy(self)
        current_color = game_copy.piece_dict[move.origin].color
        king_square = get_king(game_copy.piece_dict, current_color)
        move.apply_move(game_copy.piece_dict)
        return not game_copy.is_square_in_check(current_color, king_square)
