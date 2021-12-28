from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QShortcut, QKeySequence


class WinfredMainWindow(QMainWindow):
    def __init__(self):
        super(WinfredMainWindow, self).__init__()
        self.setWindowTitle("Winfred")
        self.setFixedSize(700, 64)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)

