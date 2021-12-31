from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QMargins, QPointF
from PyQt6.QtGui import QShortcut, QKeySequence, QGuiApplication
from pynput import keyboard

from .MainText import MainText


class WinfredMainWindow(QMainWindow):
    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.setWindowTitle("Winfred")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(700, 64)
        self.centerOnScreen()
        self.setStyleSheet("background-color: black;")
        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)

        self.oldPos = self.pos()

        edit = MainText(conf.mainTextFontSize)
        self.setContentsMargins(QMargins(6, 0, 6, 0))
        self.setCentralWidget(edit)

        self.mainHotKeyListener = keyboard.GlobalHotKeys({"<ctrl>+y": self.show})
        self.mainHotKeyListener.start()

    def centerOnScreen(self):
        resolution = QGuiApplication.primaryScreen().availableGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.oldPos)
        self.oldPos = event.globalPosition()
        self.move(self.x() + delta.x(), self.y() + delta.y())

