import logging

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QMargins, QPointF
from PyQt6.QtGui import QShortcut, QKeySequence, QGuiApplication
from pynput import keyboard

from .MainText import MainText
from .Snippet import SnippetManager


class WinfredMainWindow(QMainWindow):
    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.__conf = conf
        self.__mainEdit = None
        self.__oldPos = self.pos()
        self.initUI(conf)

        self.__snippetManager = SnippetManager(conf)
        self.__snippetManager.snippetReplaceSignal.connect(self.handleSnippetReplaceSignal)

        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)
        QShortcut(QKeySequence(Qt.Key.Key_Alt + Qt.Key.Key_F4), self, self.hide)
        self.__mainHotKeyListener = keyboard.GlobalHotKeys({"<ctrl>+<space>": self.show})
        self.__mainHotKeyListener.start()

        self.__clipboardHotKeyListener = keyboard.GlobalHotKeys({"<cmd_l>+c": self.showClipboard})
        self.__clipboardHotKeyListener.start()

        self.__keyboardController = keyboard.Controller()

    def initUI(self, conf):
        self.setWindowTitle("Winfred")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint
                           | Qt.WindowType.WindowStaysOnTopHint
                           | Qt.WindowType.Tool)
        self.setFixedSize(700, 64)
        self.centerOnScreen()
        self.setStyleSheet("background-color: black;")

        self.__mainEdit = MainText(conf.mainTextFontSize)
        self.__mainEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setContentsMargins(QMargins(6, 0, 6, 0))
        self.setCentralWidget(self.__mainEdit)
        self.setFocusProxy(self.__mainEdit)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def show(self):
        self.setVisible(True)
        self.setFocus()
        self.__mainEdit.setFocus()
        self.activateWindow()
        self.backspaceNTimes(1)     # use input event to force focus on the __mainEdit(Windows need this)

    def hide(self):
        self.clearFocus()
        self.setVisible(False)

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

    def backspaceNTimes(self, backspace_count):
        while backspace_count > 0:
            self.__keyboardController.press(keyboard.Key.backspace)
            self.__keyboardController.release(keyboard.Key.backspace)
            backspace_count -= 1

    def typeSomething(self, target_content):
        self.__keyboardController.type(target_content)

    def handleSnippetReplaceSignal(self, backspace_num, target_snippet_str):
        logging.info("len:%d, target snippet:%s" % (backspace_num, target_snippet_str))
        self.backspaceNTimes(backspace_num)
        self.typeSomething(target_snippet_str)

    def showClipboard(self):
        self.show()

