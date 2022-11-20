"""
Move processor.
Apply a move and update the global state
"""
import copy

from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.pieces.bishop import Bishop
from src.CHESS.domain.classes.pieces.king import King
from src.CHESS.domain.classes.pieces.knight import Knight
from src.CHESS.domain.classes.pieces.pawn import Pawn
from src.CHESS.domain.classes.pieces.queen import Queen
from src.CHESS.domain.classes.pieces.rook import Rook
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.events.event_getter.move_getter.pawn_available_moves import (
    get_pawn_first_movement,
    get_pawn_forward_moves,
    get_pawn_capture_moves,
    get_pawn_enpassant_moves,
)
from src.CHESS.domain.events.event_getter.square_getter.square_getter import (
    available_squares,
)
from src.CHESS.domain.events.moves.move import Move
from src.CHESS.domain.states.board import Board
from src.CHESS.domain.states.game_historic import GameHistoric
from src.CHESS.logger import LOGGER


def apply_move(move: Move, board: Board) -> bool:
    """
    Apply a move.
    Moves the piece.
    (Does no legal verification
    @return: True if the moves is a capture
    """
    capture = move.destination in board.piece_dict
    board.piece_dict[move.destination] = board.piece_dict[move.origin]
    board.piece_dict.pop(move.origin)
    return capture


def is_square_in_check(
    color: Color, square: Square, board: Board, historic: GameHistoric = None
) -> bool:
    """
    Return a boolean indicating if a piece in a different color can moves
    to square (indicates if a piece of color *color* is in check)
    @param historic:
    @param board:
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
                square_available_moves_no_castling(origin, board, historic),
            )
        )
        for origin, piece in board.piece_dict.items()
    )


def is_move_legal(move: Move, board: Board, historic=None) -> bool:
    """
    Return a boolean value indicating whether the moves is legal or not.
    Applies the moves in a copy, and check if the king is in the destination of opposite moves
    @return:
    """
    board_copy = copy.deepcopy(board)
    current_color = board_copy.piece_dict[move.origin].color
    apply_move(move, board_copy)
    king_square = board_copy.get_king(current_color)

    return not is_square_in_check(current_color, king_square, board_copy, historic)


def square_available_moves_no_castling(
    origin: Square,
    board: Board,
    historic: GameHistoric = None,
    legal_verification=False,
) -> [Move]:
    """
    Return a list with all the available moves from origin
    The castling are in a separate function, to avoid recursion error
    @param historic: useful only for pawn
    @param board:
    @param legal_verification: if a legal verification on the moves must be done
    @param origin: Square origin for the moves
    @return: a list with the available moves from origin
    """
    # pylint: disable=R0916
    LOGGER.info("Get available moves called")
    origin_piece = board.piece_dict[origin]
    available_moves = []
    if type(origin_piece) in [Bishop, King, Knight, Queen, Rook]:
        available_moves.extend(
            origin_piece.move(origin, destination)
            for destination in available_squares(origin, board)
        )
    # pawn
    elif type(origin_piece) == Pawn:
        # First movement
        available_moves = get_pawn_first_movement(origin, board)
        # Forward moves
        available_moves.extend(get_pawn_forward_moves(origin, board))
        # Capture on the right
        available_moves.extend(get_pawn_capture_moves(origin, board))
        # En passant
        available_moves.extend(get_pawn_enpassant_moves(origin, board, historic))
    else:
        raise ValueError("Unknown pieces in origin")
    # Remove moves if they are illegal
    if legal_verification:
        return [
            move for move in available_moves if is_move_legal(move, board, historic)
        ]
    return available_moves
