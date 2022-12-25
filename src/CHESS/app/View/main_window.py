"""
View of the main window
Contains a chess board, an opponent selector
"""

import itertools
from PySide6.QtWidgets import QMainWindow
from src.CHESS.app.View.chess_square import ChessSquare
from src.CHESS.app.View.constants import BoardColor
from src.ihm.main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.board.setVerticalHeaderLabels(["8", "7", "6", "5", "4", "3", "2", "1"])
        self.board.setHorizontalHeaderLabels(["A", "B", "C", "D", "E", "F", "G", "H"])
        for row, column in itertools.product(range(8), range(8)):
            color = BoardColor.BLACK if (row + column) % 2 else BoardColor.WHITE
            self.board.setItem(row, column, ChessSquare(color))
