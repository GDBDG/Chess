"""
Getter for the moves from origin
"""

from app.src.model.available_move_getter._available_squares_getter import (
    _step_next_move,
)
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import _get_current_color
from app.src.model.move.knight_promotion import KnightPromotion
from app.src.model.move.knight_promotion_capture import KnightPromotionCapture
from app.src.model.move.move import Move
from app.src.model.move.pawn_2_square_move import Pawn2SquareMove
from app.src.model.move.pawn_capture import CaptureMove
from app.src.model.move.pawn_move import PawnMove
from app.src.model.move.queen_promotion import QueenPromotion
from app.src.model.move.queen_promotion_capture import QueenPromotionCapture
from app.src.model.pieces.piece import Piece


def _get_pawn_forward_moves(
    origin: Square,
    piece_dict: dict[Square, Piece],
) -> [Move]:
    """
    Return the available forward moves for a pawn
    @param origin:
    @param piece_dict:
    @return:
    """
    available_moves = []
    if (
        Square(origin.column, origin.row + _step_next_move(origin, piece_dict))
        not in piece_dict
    ):
        # Promotion:
        if origin.row + _step_next_move(origin, piece_dict) in [1, 8]:
            available_moves.extend(
                (
                    QueenPromotion(
                        origin,
                        Square(
                            origin.column,
                            origin.row + _step_next_move(origin, piece_dict),
                        ),
                    ),
                    KnightPromotion(
                        origin,
                        Square(
                            origin.column,
                            origin.row + _step_next_move(origin, piece_dict),
                        ),
                    ),
                )
            )
        # classic move
        else:
            available_moves.append(
                PawnMove(
                    origin,
                    Square(
                        origin.column,
                        origin.row + _step_next_move(origin, piece_dict),
                    ),
                )
            )
    return available_moves


def _get_pawn_first_movement(
    origin: Square,
    piece_dict: dict[Square, Piece],
) -> [Move]:
    """
    Return the 2 squares move (if available)
    @param origin:
    @param piece_dict:
    @return:
    """
    # pylint: disable=R0916
    available_moves = []
    color = _get_current_color(origin, piece_dict)
    if (
        (
            (color == Color.WHITE and origin.row == 2)
            or (color == Color.BLACK and origin.row == 7)
        )
        and Square(origin.column, origin.row + _step_next_move(origin, piece_dict))
        not in piece_dict
        and Square(origin.column, origin.row + 2 * _step_next_move(origin, piece_dict))
        not in piece_dict
    ):
        available_moves.append(
            Pawn2SquareMove(
                origin,
                Square(
                    origin.column,
                    origin.row + 2 * _step_next_move(origin, piece_dict),
                ),
            )
        )
    return available_moves


def _get_pawn_capture_moves(
    origin: Square,
    piece_dict: dict[Square, Piece],
) -> [Move]:
    """
    Return the capture moves for a pawn in origin
    @param origin:
    @param piece_dict:
    @return:
    """
    available_moves = []
    if origin.column != Column.H:
        destination = Square(
            Column(origin.column.value + 1),
            origin.row + _step_next_move(origin, piece_dict),
        )
        _add_pawn_capture_move(origin, destination, piece_dict, available_moves)
    # capture on the left
    if origin.column != Column.A:
        destination = Square(
            Column(origin.column.value - 1),
            origin.row + _step_next_move(origin, piece_dict),
        )
        # Promotion
        _add_pawn_capture_move(origin, destination, piece_dict, available_moves)
    return available_moves


def _add_pawn_capture_move(
    origin: Square,
    destination: Square,
    piece_dict: dict[Square, Piece],
    available_moves: [Move],
) -> None:
    """
    Add the available captures to available_moves for the pawn at a given destination
    Modify available_moves to add the available moves
    (Makes no verification on destination)
    @param piece_dict:
    @param origin: origin square
    @param destination: destination square
    @param available_moves: list of available moves (modified by the function)
    @return:
    """
    # Promotion
    if (
        destination in piece_dict
        and piece_dict[destination].color != _get_current_color(origin, piece_dict)
        and destination.row in [1, 8]
    ):
        available_moves.extend(
            (
                QueenPromotionCapture(origin, destination),
                KnightPromotionCapture(origin, destination),
            )
        )
    # Classic move
    if (
        destination in piece_dict
        and piece_dict[destination].color != _get_current_color(origin, piece_dict)
        and destination.row not in [1, 8]
    ):
        available_moves.append(CaptureMove(origin, destination))
