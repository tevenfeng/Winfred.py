from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QMargins, QPointF
from PyQt6.QtGui import QShortcut, QKeySequence, QGuiApplication
from pynput import keyboard

from .MainText import MainText


class WinfredMainWindow(QMainWindow):
    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.mainEdit = None
        self.oldPos = self.pos()
        self.initUI(conf)

        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)
        self.mainHotKeyListener = keyboard.GlobalHotKeys({"<ctrl>+y": self.show})
        self.mainHotKeyListener.start()

    def initUI(self, conf):
        self.setWindowTitle("Winfred")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(700, 64)
        self.centerOnScreen()
        self.setStyleSheet("background-color: black;")

        self.mainEdit = MainText(conf.mainTextFontSize)
        self.setContentsMargins(QMargins(6, 0, 6, 0))
        self.setCentralWidget(self.mainEdit)

    def centerOnScreen(self):
        resolution = QGuiApplication.primaryScreen().availableGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 3) - (self.frameSize().height() / 2))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.oldPos)
        self.oldPos = event.globalPosition()
        self.move(self.x() + delta.x(), self.y() + delta.y())

