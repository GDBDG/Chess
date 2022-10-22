"""
Castling state (associated variables)
One instance for white, and one for black
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.square import Square
from app.src.model.events.event_processor.move_processor import is_square_in_check
from app.src.model.events.moves.king_move import KingMove
from app.src.model.events.moves.long_castling import LongCastling
from app.src.model.events.moves.move import Move
from app.src.model.events.moves.rook_move import RookMove
from app.src.model.events.moves.short_castling import ShortCastling
from app.src.model.states.board import Board
from app.src.model.states.game_historic import GameHistoric


class CastlingState:
    """
    Castling state
    __long_castling_available: false if the king or rook in A has moved
    __short_castling_available: false if the king or rook in H has moved
    """

    def __init__(self, color: Color):
        """
        Constructor
        """
        self.__short_castling_available = True
        self.__long_castling_available = True
        self.__row = 1 * (color == Color.WHITE) + 8 * (color == Color.BLACK)
        self.color = color

    def update_castling_state(self, last_move: Move) -> None:
        """
        Update the castling state with the last moves
        @param last_move:
        @return:
        """
        if isinstance(last_move, KingMove):
            self.__long_castling_available = False
            self.__short_castling_available = False
        if isinstance(last_move, RookMove) and last_move.origin == Square(
            Column.A, self.__row
        ):
            self.__long_castling_available = False
        if isinstance(last_move, RookMove) and last_move.origin == Square(Column.H, 1):
            self.__short_castling_available = False

    def __is_short_castling_available(self, board: Board, historic) -> bool:
        # sourcery skip: assign-if-exp, boolean-if-exp-identity,
        # sourcery skip: reintroduce-else, remove-unnecessary-cast
        """
        Return if a long castling is available for the current color.
        | | | | |K|x|x|R|
         A B C D E F G H
        neither the king nor the rook has moved
        the king is not in check
        x and X must be empty, and not in check
        (no need to check the position, since the king has not moved)

        @return:
        """
        # check if the king is not in check
        if is_square_in_check(
            self.color, Square(Column.E, self.__row), board, historic
        ):
            return False
        if (
            Square(Column.F, self.__row) in board.piece_dict
            or Square(Column.G, self.__row) in board.piece_dict
        ):
            return False
        # check if x are not in check
        if is_square_in_check(
            self.color, Square(Column.F, self.__row), board, historic
        ) or is_square_in_check(
            self.color, Square(Column.G, self.__row), board, historic
        ):
            return False
        return True

    def __is_long_castling_available(
        self, board: Board, historic: GameHistoric
    ) -> bool:
        # sourcery skip: assign-if-exp, boolean-if-exp-identity,
        # sourcery skip: reintroduce-else, remove-unnecessary-cast
        """
        Return if a long castling is available for the current color.
        |R|x|X|X|K| | | |
         A B C D E F G H
        neither the king nor the rook has moved
        the king is not in check
        x and X must be empty,
        X must not be in check
        (no need to check the position, since the king has not moved)

        @return:
        """
        # check if the king is not in check
        if is_square_in_check(
            self.color, Square(Column.E, self.__row), board, historic
        ):
            return False
        # check if x are empty
        if (
            Square(Column.D, self.__row) in board.piece_dict
            or Square(Column.C, self.__row) in board.piece_dict
            or Square(Column.B, self.__row) in board.piece_dict
        ):
            return False
        # check if X are not in check
        if is_square_in_check(
            self.color, Square(Column.D, self.__row), board, historic
        ) or is_square_in_check(
            self.color, Square(Column.C, self.__row), board, historic
        ):
            return False
        return True

    def available_castling(
        self, board: Board, historic: GameHistoric
    ) -> [LongCastling, ShortCastling]:
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
        long_castling_available = self.__is_long_castling_available(board, historic)
        short_castling_available = self.__is_short_castling_available(board, historic)
        available_moves = []
        if self.__long_castling_available and long_castling_available:
            available_moves.append(LongCastling(Square(Column.E, self.__row)))
        if self.__short_castling_available and short_castling_available:
            available_moves.append(ShortCastling(Square(Column.E, self.__row)))
        return available_moves
