"""
Getter for the moves from origin
"""

from app.src.logger import LOGGER
from app.src.model.available_move_getter._available_squares_getter import (
    _available_squares_bishop,
    _available_squares_knight,
    _available_squares_queen,
    _available_squares_rook,
    _step_next_move,
    _available_squares_king,
)
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import _get_current_color
from app.src.model.move.bishop_move import BishopMove
from app.src.model.move.king_move import KingMove
from app.src.model.move.knight_move import KnightMove
from app.src.model.move.knight_promotion import KnightPromotion
from app.src.model.move.knight_promotion_capture import KnightPromotionCapture
from app.src.model.move.move import Move
from app.src.model.move.pawn_capture import CaptureMove
from app.src.model.move.pawn_move import PawnMove
from app.src.model.move.queen_move import QueenMove
from app.src.model.move.queen_promotion import QueenPromotion
from app.src.model.move.queen_promotion_capture import QueenPromotionCapture
from app.src.model.move.rook_move import RookMove
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.king import King
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


def get_available_moves(
    origin: Square,
    piece_dict: dict[Square, Piece],
    legal_verification=False,
) -> [Move]:
    """
    Return a list with all the available moves from origin
    @param legal_verification: if a legal verification on the moves must be done
    @param origin: Square origin for the move
    @param piece_dict: dict with the pieces in the game
    @return: a list with the available moves from origin
    """
    # pylint: disable=R0916
    LOGGER.info("Get available moves called for bishop")
    origin_piece = piece_dict[origin]
    available_moves = []
    if type(origin_piece) == Bishop:
        available_moves.extend(
            [
                BishopMove(origin, destination)
                for destination in _available_squares_bishop(origin, piece_dict)
            ]
        )
    elif type(origin_piece) == Knight:
        available_moves.extend(
            [
                KnightMove(origin, destination)
                for destination in _available_squares_knight(origin, piece_dict)
            ]
        )
    elif type(origin_piece) == Queen:
        available_moves.extend(
            [
                QueenMove(origin, destination)
                for destination in _available_squares_queen(origin, piece_dict)
            ]
        )
    elif type(origin_piece) == Rook:
        available_moves.extend(
            [
                RookMove(origin, destination)
                for destination in _available_squares_rook(origin, piece_dict)
            ]
        )
    # king
    elif type(origin_piece) == King:
        available_moves.extend(
            [
                KingMove(origin, destination)
                for destination in _available_squares_king(origin, piece_dict)
            ]
        )
    # pawn
    elif type(origin_piece) == Pawn:
        # First movement
        available_moves = _get_pawn_first_movement(origin, piece_dict)
        # Forward move
        available_moves.extend(_get_pawn_forward_moves(origin, piece_dict))
        # Capture on the right
        available_moves.extend(_get_pawn_capture_moves(origin, piece_dict))
        return available_moves
    else:
        raise ValueError("Unknown pieces in origin")
    # Remove moves if they are illegal
    if legal_verification:
        return [move for move in available_moves if move.is_legal(piece_dict)]
    else:
        return available_moves


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
            PawnMove(
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
        _add_capture_move(origin, destination, piece_dict, available_moves)
    # capture on the left
    if origin.column != Column.A:
        destination = Square(
            Column(origin.column.value - 1),
            origin.row + _step_next_move(origin, piece_dict),
        )
        # Promotion
        _add_capture_move(origin, destination, piece_dict, available_moves)
    return available_moves


def _add_capture_move(
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


def is_square_in_check(
    color: Color, square: Square, piece_dict: dict[Square, Piece]
) -> bool:
    """
    Return a boolean indicating if a piece in a different color can move
    to square (indicates if a piece of color *color* is in check)
    @param color: color of the piece that we check if it can be taken
    @param square: the square where we check if it can be taken
    @param piece_dict:  dict of the pieces in the game
    @return: boolean
    """
    return any(
        piece.color != color
        and square
        in list(map(lambda x: x.destination, get_available_moves(origin, piece_dict)))
        for origin, piece in piece_dict.items()
    )
