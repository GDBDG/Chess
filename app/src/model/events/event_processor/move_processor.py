"""
Move processor.
Apply a move and update the global state
"""
import copy

from app.src.model.events.moves.move import Move
from app.src.model.states.board import Board


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
    from app.src.model.miscenaleous.utils import is_square_in_check

    return not is_square_in_check(current_color, king_square, board_copy, historic)
