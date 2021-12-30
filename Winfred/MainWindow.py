from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QMargins, QPointF
from PyQt6.QtGui import QShortcut, QKeySequence
from pynput import keyboard

from .MainText import MainText


class WinfredMainWindow(QMainWindow):
    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.setWindowTitle("Winfred")
        self.setFixedSize(700, 64)
        self.setStyleSheet("background-color: black;")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)

        self.oldPos = self.pos()

        edit = MainText(conf.mainTextFontSize)
        self.setContentsMargins(QMargins(6, 2, 6, 2))
        self.setCentralWidget(edit)

        self.mainHotKeyListener = keyboard.GlobalHotKeys({"<ctrl>+y": self.show})
        self.mainHotKeyListener.start()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.oldPos)
        self.oldPos = event.globalPosition()
        self.move(self.x() + delta.x(), self.y() + delta.y())

