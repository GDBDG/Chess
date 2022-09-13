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
    _get_current_color,
)
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column
from app.src.model.move.bishop_move import BishopMove
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
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


def get_available_moves(
    origin: Square,
    piece_dict: dict[Square, Piece],
) -> [Move]:
    """
    Return a list with all the available moves from origin
    @param origin: Square origin for the move
    @param piece_dict: dict with the pieces in the game
    @return: a list with the available moves from origin
    """
    LOGGER.info("Get available moves called for bishop")
    origin_piece = piece_dict[origin]
    if type(origin_piece) == Bishop:
        return [
            BishopMove(origin, destination)
            for destination in _available_squares_bishop(origin, piece_dict)
        ]
    if type(origin_piece) == Knight:
        return [
            KnightMove(origin, destination)
            for destination in _available_squares_knight(origin, piece_dict)
        ]
    if type(origin_piece) == Queen:
        return [
            QueenMove(origin, destination)
            for destination in _available_squares_queen(origin, piece_dict)
        ]
    if type(origin_piece) == Rook:
        return [
            RookMove(origin, destination)
            for destination in _available_squares_rook(origin, piece_dict)
        ]
    # pawn
    if type(origin_piece) == Pawn:
        available_moves = []
        # Forward move
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
        # Capture move
        # Capture on right
        if origin.column != Column.H:
            destination = Square(
                Column(origin.column.value + 1),
                origin.row + _step_next_move(origin, piece_dict),
            )
            add_capture_move(origin, destination, piece_dict, available_moves)
        # capture on left
        if origin.column != Column.A:
            destination = Square(
                Column(origin.column.value - 1),
                origin.row + _step_next_move(origin, piece_dict),
            )
            # Promotion
            add_capture_move(origin, destination, piece_dict, available_moves)
        return available_moves
    raise ValueError("Unknown pieces in origin")


def add_capture_move(
    origin: Square,
    destination: Square,
    piece_dict: dict[Square, Piece],
    available_moves: [Move],
) -> None:
    """
    Add the available captures for the pawn at a given destination
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
