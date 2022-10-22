"""
Test that it is possible to get the bishop moves
"""
from app.src.model.events.moves.bishop_move import BishopMove
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import square_available_moves_no_castling
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.piece import Piece


def test_bishop_move():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | |W| | |
    5 | | | | | | | | |
    4 | | | |W| | | | |
    3 | | | | | | | | |
    2 | |B| | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The bishop moves uses _available_square_on_side_line, already completely
    tested)
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): Bishop(Color.WHITE),
        Square(Column.F, 6): Piece(Color.WHITE),
        Square(Column.B, 2): Piece(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    expected_moves = [
        BishopMove(Square(Column.D, 4), Square(Column.E, 5)),
        BishopMove(Square(Column.D, 4), Square(Column.E, 3)),
        BishopMove(Square(Column.D, 4), Square(Column.F, 2)),
        BishopMove(Square(Column.D, 4), Square(Column.G, 1)),
        BishopMove(Square(Column.D, 4), Square(Column.C, 5)),
        BishopMove(Square(Column.D, 4), Square(Column.B, 6)),
        BishopMove(Square(Column.D, 4), Square(Column.A, 7)),
        BishopMove(Square(Column.D, 4), Square(Column.C, 3)),
        BishopMove(Square(Column.D, 4), Square(Column.B, 2)),
    ]
    assert (
        square_available_moves_no_castling(Square(Column.D, 4), board) == expected_moves
    )
