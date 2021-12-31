from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QMargins, QPointF
from PyQt6.QtGui import QShortcut, QKeySequence, QGuiApplication
from pynput import keyboard

from .MainText import MainText
from .Snippet import SnippetManager


class WinfredMainWindow(QMainWindow):
    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self._mainEdit = None
        self.__oldPos = self.pos()
        self.initUI(conf)

        self._snippetManager = SnippetManager(conf)

        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hideMainWindow)
        self._mainHotKeyListener = keyboard.GlobalHotKeys({"<ctrl>+y": self.showMainWindow})
        self._mainHotKeyListener.start()

    def initUI(self, conf):
        self.setWindowTitle("Winfred")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(700, 64)
        self.centerOnScreen()
        self.setStyleSheet("background-color: black;")

        self._mainEdit = MainText(conf.mainTextFontSize)
        self.setContentsMargins(QMargins(6, 0, 6, 0))
        self.setCentralWidget(self._mainEdit)

    def showMainWindow(self):
        self.show()

    def hideMainWindow(self):
        self.hide()

    def centerOnScreen(self):
        resolution = QGuiApplication.primaryScreen().availableGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 3) - (self.frameSize().height() / 2))

    def mousePressEvent(self, event):
        self.__oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.__oldPos)
        self.__oldPos = event.globalPosition()
        self.move(self.x() + delta.x(), self.y() + delta.y())

