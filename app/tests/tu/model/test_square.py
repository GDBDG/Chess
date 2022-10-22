"""
Unit tests for the Square classes
"""
from app.src.model.classes.square import Square
from app.src.model.miscenaleous.column import Column


def test_hash():
    """
    Test that 2 squares with the same coordinates are the same key in a dict
    @return:
    """
    square1 = Square(Column.A, 1)
    square2 = Square(Column.A, 1)
    uselesse_dict = {square1: 1}
    assert hash(square1) == hash(square2)
    assert uselesse_dict[square1] == uselesse_dict[square2]
