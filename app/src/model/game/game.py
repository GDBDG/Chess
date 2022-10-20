"""
Game implementation.
Manage the game and store the current state
"""

from app.src.exceptions.invalid_move_error import InvalidMoveError
from app.src.logger import LOGGER
from app.src.model.game.board import Board
from app.src.model.game.castling_state import CastlingState
from app.src.model.game.game_historic import GameHistoric
from app.src.model.game.game_state import GameState
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.utils import square_available_moves_no_castling, is_square_in_check
from app.src.model.move.move import Move
from app.src.model.pieces.king import King
from app.src.model.pieces.piece import Piece


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
        self.board = Board()
        self.game_historic = GameHistoric()
        self.game_state = GameState()
        self.white_castling_state = CastlingState(Color.WHITE)
        self.black_castling_state = CastlingState(Color.BLACK)

    @property
    def piece_dict(self) -> dict[Square, Piece]:
        """
        Board getter
        @return:
        """
        return self.board.piece_dict

    @property
    def player(self) -> Color:
        """
        Player getter (from game_state
        @return:
        """
        return self.game_state.player

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
        capture = move.apply_move(self.board)
        # Update the historic
        self.game_historic.update_historic(move, self.board)
        # Update the game state
        self.update_castling_state()
        self.game_state.update_state(self.game_historic, capture)
        # Draw with no moves
        king_square = self.board.get_king(self.game_state.player)
        if not is_square_in_check(self.game_state.player, king_square, self.board, self.game_historic) \
            and self.available_moves_list() == []:
            self.game_state.state = GameState.DRAW

    def update_castling_state(self):
        """
        After a move is played, update the game state (the castling variables)
        Use the last move in history.
        @return: None.
        """
        # Castling state update
        if self.player == Color.WHITE:
            self.white_castling_state.update_castling_state(self.game_historic.move_historic[-1])
        else:
            self.black_castling_state.update_castling_state(self.game_historic.move_historic[-1])

    def square_available_moves(self, origin, legal_verification=False) -> [Move]:
        """
        Return a list with all the available moves from origin
        @param legal_verification:
        @param origin:
        @return:
        """
        available_moves = square_available_moves_no_castling(
            origin, self.board, self.game_historic, legal_verification
        )
        if type(self.piece_dict[origin]) == King:
            if self.player == Color.WHITE:
                available_moves.extend(self.white_castling_state.available_castling(self.board, self.game_historic))
            else:
                available_moves.extend(self.black_castling_state.available_castling(self.board, self.game_historic))
        return available_moves
