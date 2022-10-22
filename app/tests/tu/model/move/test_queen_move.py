"""
Tests for the queen moves
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.pieces.piece import Piece
from app.src.model.classes.pieces.queen import Queen
from app.src.model.classes.square import Square
from app.src.model.events.moves.queen_move import QueenMove
from app.src.model.miscenaleous.utils import square_available_moves_no_castling
from app.src.model.states.board import Board


def test_queen_move():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | |W| |B| | |
    5 | | | | | | | | |
    4 | | | |Q| | |B| |
    3 | | |W| | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The queen moves uses _available_square_on_side_line, already completely
    tested)
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): Queen(Color.WHITE),
        Square(Column.D, 6): Piece(Color.WHITE),
        Square(Column.G, 4): Piece(Color.BLACK),
        Square(Column.F, 6): Piece(Color.BLACK),
        Square(Column.C, 3): Piece(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    expected_moves = [
        QueenMove(Square(Column.D, 4), Square(Column.E, 4)),
        QueenMove(Square(Column.D, 4), Square(Column.F, 4)),
        QueenMove(Square(Column.D, 4), Square(Column.G, 4)),
        QueenMove(Square(Column.D, 4), Square(Column.C, 4)),
        QueenMove(Square(Column.D, 4), Square(Column.B, 4)),
        QueenMove(Square(Column.D, 4), Square(Column.A, 4)),
        QueenMove(Square(Column.D, 4), Square(Column.D, 5)),
        QueenMove(Square(Column.D, 4), Square(Column.D, 3)),
        QueenMove(Square(Column.D, 4), Square(Column.D, 2)),
        QueenMove(Square(Column.D, 4), Square(Column.D, 1)),
        QueenMove(Square(Column.D, 4), Square(Column.E, 5)),
        QueenMove(Square(Column.D, 4), Square(Column.F, 6)),
        QueenMove(Square(Column.D, 4), Square(Column.E, 3)),
        QueenMove(Square(Column.D, 4), Square(Column.F, 2)),
        QueenMove(Square(Column.D, 4), Square(Column.G, 1)),
        QueenMove(Square(Column.D, 4), Square(Column.C, 5)),
        QueenMove(Square(Column.D, 4), Square(Column.B, 6)),
        QueenMove(Square(Column.D, 4), Square(Column.A, 7)),
    ]
    assert (
        square_available_moves_no_castling(Square(Column.D, 4), board) == expected_moves
    )
