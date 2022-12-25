# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1341, 861))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.board = QTableWidget(self.horizontalLayoutWidget)
        if (self.board.columnCount() < 8):
            self.board.setColumnCount(8)
        if (self.board.rowCount() < 8):
            self.board.setRowCount(8)
        self.board.setObjectName(u"board")
        self.board.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.board.sizePolicy().hasHeightForWidth())
        self.board.setSizePolicy(sizePolicy)
        self.board.setMinimumSize(QSize(819, 0))
        self.board.setRowCount(8)
        self.board.setColumnCount(8)
        self.board.horizontalHeader().setVisible(True)
        self.board.horizontalHeader().setDefaultSectionSize(100)
        self.board.horizontalHeader().setHighlightSections(False)
        self.board.verticalHeader().setVisible(True)
        self.board.verticalHeader().setCascadingSectionResizes(False)
        self.board.verticalHeader().setDefaultSectionSize(100)

        self.verticalLayout.addWidget(self.board)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.start_game_button = QPushButton(self.horizontalLayoutWidget)
        self.start_game_button.setObjectName(u"start_game_button")

        self.verticalLayout_3.addWidget(self.start_game_button)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_game_button.setText(QCoreApplication.translate("MainWindow", u"New game", None))
    # retranslateUi

