"""
Tests for the game classes
"""
from app.src.model.classes.const.column import Column
from app.src.model.classes.square import Square
from app.src.model.events.moves.knight_move import KnightMove
from app.src.model.events.moves.pawn_2_square_move import Pawn2SquareMove
from app.src.model.events.moves.pawn_move import PawnMove
from app.src.model.game.game import Game


def test_available_moves_list():
    """
    Test that an initial config returns all the 20 moves
    No need to do more tests, They are done in the piece test
    with the get_available_moves
    @return:
    """
    game = Game()
    expected_moves = [
        KnightMove(
            Square(Column.B, 1),
            Square(Column.A, 3),
        ),
        KnightMove(
            Square(Column.B, 1),
            Square(Column.C, 3),
        ),
        KnightMove(
            Square(Column.G, 1),
            Square(Column.F, 3),
        ),
        KnightMove(
            Square(Column.G, 1),
            Square(Column.H, 3),
        ),
        Pawn2SquareMove(
            Square(Column.A, 2),
            Square(Column.A, 4),
        ),
        PawnMove(
            Square(Column.A, 2),
            Square(Column.A, 3),
        ),
        Pawn2SquareMove(
            Square(Column.B, 2),
            Square(Column.B, 4),
        ),
        PawnMove(
            Square(Column.B, 2),
            Square(Column.B, 3),
        ),
        Pawn2SquareMove(
            Square(Column.C, 2),
            Square(Column.C, 4),
        ),
        PawnMove(
            Square(Column.C, 2),
            Square(Column.C, 3),
        ),
        Pawn2SquareMove(
            Square(Column.D, 2),
            Square(Column.D, 4),
        ),
        PawnMove(
            Square(Column.D, 2),
            Square(Column.D, 3),
        ),
        Pawn2SquareMove(
            Square(Column.E, 2),
            Square(Column.E, 4),
        ),
        PawnMove(
            Square(Column.E, 2),
            Square(Column.E, 3),
        ),
        Pawn2SquareMove(
            Square(Column.F, 2),
            Square(Column.F, 4),
        ),
        PawnMove(
            Square(Column.F, 2),
            Square(Column.F, 3),
        ),
        Pawn2SquareMove(
            Square(Column.G, 2),
            Square(Column.G, 4),
        ),
        PawnMove(
            Square(Column.G, 2),
            Square(Column.G, 3),
        ),
        Pawn2SquareMove(
            Square(Column.H, 2),
            Square(Column.H, 4),
        ),
        PawnMove(
            Square(Column.H, 2),
            Square(Column.H, 3),
        ),
    ]
    assert game.available_moves_list() == expected_moves


