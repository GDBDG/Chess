"""
Unit tests for the Square class
"""
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column


def test_hash():
    """
    Test that 2 squares with the same coordinates are the same key in a dict
    @return:
    """
    square1 = Square(Column.A, 1)
    square2 = Square(Column.A, 1)
    toto = {square1: 1}
    assert hash(square1) == hash(square2)
    assert toto[square1] == toto[square2]
