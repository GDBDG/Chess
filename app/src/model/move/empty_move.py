"""
Empty Move, to initialize the game history
"""
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column
from app.src.model.move.move import Move


class EmptyMove(Move):
    """
    Empty move class
    """

    def __init__(
        self,
    ):
        """
        Constructor
        """
        super().__init__(Square(Column.D, 4), Square(Column.D, 4))
