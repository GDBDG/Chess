"""
Getter for the moves from origin
"""

from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.const.column import Column
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.events.event_getter.square_getter.utils_available_squares_getter import (
    step_next_move,
)
from src.CHESS.domain.events.moves.en_passant import EnPassant
from src.CHESS.domain.events.moves.knight_promotion import KnightPromotion
from src.CHESS.domain.events.moves.knight_promotion_capture import (
    KnightPromotionCapture,
)
from src.CHESS.domain.events.moves.move import Move
from src.CHESS.domain.events.moves.pawn_2_square_move import Pawn2SquareMove
from src.CHESS.domain.events.moves.pawn_capture import CaptureMove
from src.CHESS.domain.events.moves.pawn_move import PawnMove
from src.CHESS.domain.events.moves.queen_promotion import QueenPromotion
from src.CHESS.domain.events.moves.queen_promotion_capture import QueenPromotionCapture
from src.CHESS.domain.states.board import Board
from src.CHESS.domain.states.game_historic import GameHistoric


def get_pawn_forward_moves(
    origin: Square,
    board: Board,
) -> [Move]:
    """
    Return the available forward moves for a pawn
    @param board:
    @param origin:
    @return:
    """
    available_moves = []
    if (
        Square(origin.column, origin.row + step_next_move(origin, board.piece_dict))
        not in board.piece_dict
    ):
        # Promotion:
        if origin.row + step_next_move(origin, board.piece_dict) in [1, 8]:
            available_moves.extend(
                (
                    QueenPromotion(
                        origin,
                        Square(
                            origin.column,
                            origin.row + step_next_move(origin, board.piece_dict),
                        ),
                    ),
                    KnightPromotion(
                        origin,
                        Square(
                            origin.column,
                            origin.row + step_next_move(origin, board.piece_dict),
                        ),
                    ),
                )
            )
        # classic moves
        else:
            available_moves.append(
                PawnMove(
                    origin,
                    Square(
                        origin.column,
                        origin.row + step_next_move(origin, board.piece_dict),
                    ),
                )
            )
    return available_moves


def get_pawn_first_movement(
    origin: Square,
    board: Board,
) -> [Move]:
    """
    Return the 2 squares moves (if available)
    @param board:
    @param origin:
    @return:
    """
    # pylint: disable=R0916
    available_moves = []
    color = board.get_current_color(origin)
    if (
        (
            (color == Color.WHITE and origin.row == 2)
            or (color == Color.BLACK and origin.row == 7)
        )
        and Square(origin.column, origin.row + step_next_move(origin, board.piece_dict))
        not in board.piece_dict
        and Square(
        origin.column, origin.row + 2 * step_next_move(origin, board.piece_dict)
    )
        not in board.piece_dict
    ):
        available_moves.append(
            Pawn2SquareMove(
                origin,
                Square(
                    origin.column,
                    origin.row + 2 * step_next_move(origin, board.piece_dict),
                ),
            )
        )
    return available_moves


def get_pawn_capture_moves(
    origin: Square,
    board: Board,
) -> [Move]:
    """
    Return the capture moves for a pawn in origin
    @param origin:
    @param board.piece_dict:
    @return:
    """
    available_moves = []
    if origin.column != Column.H:
        destination = Square(
            Column(origin.column.value + 1),
            origin.row + step_next_move(origin, board.piece_dict),
        )
        _add_pawn_capture_move(origin, destination, board, available_moves)
    # capture on the left
    if origin.column != Column.A:
        destination = Square(
            Column(origin.column.value - 1),
            origin.row + step_next_move(origin, board.piece_dict),
        )
        # Promotion
        _add_pawn_capture_move(origin, destination, board, available_moves)
    return available_moves


def get_pawn_enpassant_moves(origin, board: Board, historic: GameHistoric) -> [Move]:
    """
    Get the en passant moves if available
    @param origin:
    @return:
    """
    available_moves = []
    last_move = historic.move_historic[-1]
    if (
        type(historic.move_historic[-1]) == Pawn2SquareMove
        and last_move.destination.row == origin.row
        and abs(origin.column.value - last_move.destination.column.value) == 1
    ):
        available_moves.append(
            EnPassant(
                origin,
                Square(
                    last_move.destination.column,
                    origin.row + step_next_move(origin, board.piece_dict),
                ),
            )
        )
    return available_moves


def _add_pawn_capture_move(
    origin: Square,
    destination: Square,
    board: Board,
    available_moves: [Move],
) -> None:
    """
    Add the available captures to available_moves for the pawn at a given destination
    Modify available_moves to add the available moves
    (Makes no verification on destination)
    @param board.piece_dict:
    @param origin: origin square
    @param destination: destination square
    @param available_moves: list of available moves (modified by the function)
    @return:
    """
    # Promotion
    if (
        destination in board.piece_dict
        and board.piece_dict[destination].color != board.get_current_color(origin)
        and destination.row in [1, 8]
    ):
        available_moves.extend(
            (
                QueenPromotionCapture(origin, destination),
                KnightPromotionCapture(origin, destination),
            )
        )
    # Classic moves
    if (
        destination in board.piece_dict
        and board.piece_dict[destination].color != board.get_current_color(origin)
        and destination.row not in [1, 8]
    ):
        available_moves.append(CaptureMove(origin, destination))
