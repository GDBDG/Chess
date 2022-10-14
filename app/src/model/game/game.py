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
    _step_next_move,
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
from app.src.model.move.empty_move import EmptyMove
from app.src.model.move.en_passant import EnPassant
from app.src.model.move.king_move import KingMove
from app.src.model.move.knight_move import KnightMove
from app.src.model.move.long_castling import LongCastling
from app.src.model.move.move import Move
from app.src.model.move.pawn_2_square_move import Pawn2SquareMove
from app.src.model.move.pawn_move import PawnMove
from app.src.model.move.queen_move import QueenMove
from app.src.model.move.rook_move import RookMove
from app.src.model.move.short_castling import ShortCastling
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
        self.move_historic: [Move] = [EmptyMove()]
        self.config_history = {}
        self.state = GameState.RUNNING
        self.fifty_counter = 0
        # Change to False when the king or the H rook has moved
        self.white_short_castle_available = True
        # Change to False when the king or the A rook has moved
        self.white_long_castle_available = True
        # Change to False when the king or the H rook has moved
        self.black_short_castle_available = True
        # Change to False when the king or the A rook has moved
        self.black_long_castle_available = True

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
        capture = move.apply_move(self.piece_dict)
        # Update the historic
        self.move_historic.append(move)
        self.update_config_history()
        # Update the game state
        self.update_castling_state()
        self.update_draw_state(capture)
        # Update the player who has to play
        self.player = Color.BLACK if self.player == Color.WHITE else Color.WHITE

    def update_draw_state(self, capture: bool):
        """
        Update the counter for the 50 move rule
        @param capture:boolean value if the last move was a capture
        @return:
        """
        if capture or isinstance(self.move_historic[-1], PawnMove):
            self.fifty_counter = 0
        else:
            self.fifty_counter += 1
            if self.fifty_counter == 100:
                self.state = GameState.DRAW
        # Dead position
        # TODO

    def update_castling_state(self):
        """
        After a move is played, update the game state (the castling variables, and detect a Draw)
        Use the last move in history.
        @return: None.
        """
        last_move = self.move_historic[-1]
        # Castling state update
        if self.player == Color.WHITE:
            if isinstance(last_move, KingMove):
                self.white_long_castle_available = False
                self.white_short_castle_available = False
            if isinstance(last_move, RookMove) and last_move.origin == Square(
                Column.A, 1
            ):
                self.white_long_castle_available = False
            if isinstance(last_move, RookMove) and last_move.origin == Square(
                Column.H, 1
            ):
                self.white_short_castle_available = False
        else:
            if isinstance(last_move, KingMove):
                self.black_long_castle_available = False
                self.black_short_castle_available = False
            if isinstance(last_move, RookMove) and last_move.origin == Square(
                Column.A, 8
            ):
                self.black_long_castle_available = False
            if isinstance(last_move, RookMove) and last_move.origin == Square(
                Column.H, 8
            ):
                self.black_short_castle_available = False

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

    def square_available_moves_no_castling(
        self,
        origin: Square,
        legal_verification=False,
    ) -> [Move]:
        """
        Return a list with all the available moves from origin
        The castling are in a separate function, to avoid recursion error
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
            # En passant
            available_moves.extend(self._get_pawn_enpassant_moves(origin))
            return available_moves
        else:
            raise ValueError("Unknown pieces in origin")
        # Remove moves if they are illegal
        if legal_verification:
            return [move for move in available_moves if self.is_move_legal(move)]
        return available_moves

    def square_available_moves(self, origin, legal_verification=False) -> [Move]:
        """
        Return a list with all the available moves from origin
        @param legal_verification:
        @param origin:
        @return:
        """
        available_moves = self.square_available_moves_no_castling(
            origin, legal_verification
        )
        if type(self.piece_dict[origin]) == King:
            available_moves.extend(self._available_castling(origin))
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
            in list(
                map(
                    lambda x: x.destination,
                    self.square_available_moves_no_castling(origin),
                )
            )
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

    def _get_pawn_enpassant_moves(self, origin) -> [Move]:
        """
        Get the en passant move if available
        @param origin:
        @return:
        """
        available_moves = []
        last_move = self.move_historic[-1]
        if (
            type(self.move_historic[-1]) == Pawn2SquareMove
            and last_move.destination.row == origin.row
            and abs(origin.column.value - last_move.destination.column.value) == 1
        ):
            available_moves.append(
                EnPassant(
                    origin,
                    Square(
                        last_move.destination.column,
                        origin.row + _step_next_move(origin, self.piece_dict),
                    ),
                )
            )
        return available_moves

    def _available_castling(self, origin: Square) -> [Move]:
        """
        |R|x|X|X|K| | | |
         A B C D E F G H
        neither the king nor the rook has moved
        the king is not in check
        x and X must be empty,
        X must not be in check
        (no need to check the position, since the king has not moved)

        Check if the king can make a short castling,
        and return the square destination
        Return the castling available
        @return:
        """
        long_castling_available = True
        short_castling_available = True
        available_moves = []
        # check if the king is not in check
        if self.is_square_in_check(self.player, origin):
            long_castling_available = False
            short_castling_available = False
        # Long castling
        # check if x are empty
        if (
            Square(Column.D, origin.row) in self.piece_dict
            or Square(Column.C, origin.row) in self.piece_dict
            or Square(Column.B, origin.row) in self.piece_dict
        ):
            long_castling_available = False
        # check if X are not in check
        if self.is_square_in_check(
            self.player,
            Square(Column.D, origin.row),
        ) or self.is_square_in_check(
            self.player,
            Square(Column.C, origin.row),
        ):
            long_castling_available = False
        # Short castling
        # check if x are empty
        if (
            Square(Column.F, origin.row) in self.piece_dict
            or Square(Column.G, origin.row) in self.piece_dict
        ):
            short_castling_available = False
        # check if x are not in check
        if self.is_square_in_check(
            self.player,
            Square(Column.F, origin.row),
        ) or self.is_square_in_check(
            self.player,
            Square(Column.G, origin.row),
        ):
            short_castling_available = False
        if (
            (self.player == Color.WHITE and self.white_long_castle_available)
            or (self.player == Color.BLACK and self.black_long_castle_available)
        ) and long_castling_available:
            available_moves.append(LongCastling(origin))
        if (
            (self.player == Color.WHITE and self.white_short_castle_available)
            or (self.player == Color.BLACK and self.black_short_castle_available)
        ) and short_castling_available:
            available_moves.append(ShortCastling(origin))
        return available_moves
