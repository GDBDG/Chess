"""
QWidget for chess Square
"""
from PySide6.QtWidgets import QTableWidgetItem
from src.CHESS.app.View.constants import BoardColor


class ChessSquare(QTableWidgetItem):
    def __init__(self, color: BoardColor):
        """
        Display a chess square
        """
        super().__init__()
        self.color = color
        self.setBackground(color.value)
