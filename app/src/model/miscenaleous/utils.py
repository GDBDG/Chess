"""
Some useful functions
"""
from app.src.logger import LOGGER
from app.src.model.available_move_getter.available_moves import get_pawn_first_movement, get_pawn_forward_moves, \
    get_pawn_capture_moves, _get_pawn_enpassant_moves
from app.src.model.classes.pieces.bishop import Bishop
from app.src.model.classes.pieces.king import King
from app.src.model.classes.pieces.knight import Knight
from app.src.model.classes.pieces.pawn import Pawn
from app.src.model.classes.pieces.queen import Queen
from app.src.model.classes.pieces.rook import Rook
from app.src.model.classes.square import Square
from app.src.model.events.moves.move import Move
from app.src.model.game.board import Board
from app.src.model.game.game_historic import GameHistoric
from app.src.model.miscenaleous.color import Color


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
    LOGGER.info("Get available moves called for bishop")
    origin_piece = board.piece_dict[origin]
    available_moves = []
    if type(origin_piece) in [Bishop, King, Knight, Queen, Rook]:
        available_moves.extend(
            origin_piece.move(origin, destination)
            for destination in origin_piece.available_squares(
                origin, board
            )
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
        available_moves.extend(_get_pawn_enpassant_moves(origin, board, historic))
    else:
        raise ValueError("Unknown pieces in origin")
    # Remove moves if they are illegal
    if legal_verification:
        return [move for move in available_moves if move.is_move_legal(board, historic)]
    return available_moves


def is_square_in_check(color: Color, square: Square, board: Board, historic: GameHistoric = None) -> bool:
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
