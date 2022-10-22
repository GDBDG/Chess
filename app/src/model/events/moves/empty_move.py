"""
Empty Move, to initialize the game history
"""
from app.src.model.classes.const.column import Column
from app.src.model.classes.square import Square
from app.src.model.events.moves.move import Move


class EmptyMove(Move):
    """
    Empty moves classes
    """

    def __init__(
        self,
    ):
        """
        Constructor
        """
        super().__init__(Square(Column.D, 4), Square(Column.D, 4))
