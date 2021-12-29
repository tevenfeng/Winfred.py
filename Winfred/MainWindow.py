from PyQt6.QtWidgets import QMainWindow, QTextEdit
from PyQt6.QtCore import Qt, QMargins
from PyQt6.QtGui import QShortcut, QKeySequence, QPalette

from .MainText import MainText


class WinfredMainWindow(QMainWindow):
    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.setWindowTitle("Winfred")
        self.setFixedSize(700, 64)
        self.setStyleSheet("background-color: black;")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)

        edit = MainText(conf.mainTextFontSize)
        self.setContentsMargins(QMargins(6, 2, 6, 2))
        self.setCentralWidget(edit)

