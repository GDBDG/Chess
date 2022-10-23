"""
Unit tests for the Square classes
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.square import Square


def test_hash():
    """
    Test that 2 squares with the same coordinates are the same key in a dict
    @return:
    """
    square1 = Square(Column.A, 1)
    square2 = Square(Column.A, 1)
    useless_dict = {square1: 1}
    assert hash(square1) == hash(square2)
    assert useless_dict[square1] == useless_dict[square2]


def test_square_color():
    """
    Test that it is possible to get a square color
    from its coordinates
    @return:
    """
    assert Square(Column.A, 1).square_color() == Color.BLACK
    assert Square(Column.A, 2).square_color() == Color.WHITE
    assert Square(Column.B, 3).square_color() == Color.WHITE
    assert Square(Column.D, 6).square_color() == Color.BLACK
