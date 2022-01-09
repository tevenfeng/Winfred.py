import logging
import os.path

from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget
from PySide6.QtCore import Qt, QMargins, QPointF, Signal
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication, QIcon
from pynput import keyboard

from .MainText import MainText
from .Snippet import SnippetManager
from .SystemTray import SystemTray


class WinfredMainWindow(QMainWindow):
    winfredQuitSignal = Signal()

    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.__centralWidget = None
        self.__mainLayout = None
        self.__conf = conf
        self.__mainEdit = None
        self.__systemTray = None
        self.__oldPos = self.pos()
        self.initUI(conf)

        self.__snippetManager = SnippetManager(conf)
        self.__snippetManager.snippetReplaceSignal.connect(self.handleSnippetReplaceSignal)

        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)
        self.__mainHotKeyListener = keyboard.GlobalHotKeys({"<ctrl>+<space>": self.show})
        self.__mainHotKeyListener.start()

        self.__clipboardHotKeyListener = keyboard.GlobalHotKeys({"<cmd_l>+c": self.showClipboard})
        self.__clipboardHotKeyListener.start()

        self.__keyboardController = keyboard.Controller()

    def initUI(self, conf):
        self.setWindowTitle("Winfred")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setFixedSize(700, 64)
        self.centerOnScreen()
        self.setStyleSheet("background-color: black;")
        self.setContentsMargins(QMargins(6, 0, 6, 0))
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.__centralWidget = QWidget(self)
        self.setCentralWidget(self.__centralWidget)

        self.__mainLayout = QGridLayout(self.__centralWidget)
        self.__centralWidget.setLayout(self.__mainLayout)

        self.__mainEdit = MainText(conf.mainTextFontSize, self.__centralWidget)
        self.__mainEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.__mainLayout.addWidget(self.__mainEdit, 0, 0, 1, 2)

        self.initSystemTrayIcon(conf)

    def initSystemTrayIcon(self, conf):
        icon_path = os.path.join(conf.getAssetsPath(), "winfred.png")
        icon = QIcon(icon_path)
        self.__systemTray = SystemTray(icon, self)
        self.__systemTray.show()
        self.__systemTray.systemTrayDisplaySignal.connect(self.show)
        self.__systemTray.systemTrayQuitSignal.connect(self.winfredQuit)

    def winfredQuit(self):
        self.winfredQuitSignal.emit()

    def show(self):
        self.setVisible(True)
        self.setFocus()
        self.__mainEdit.setFocus()
        self.activateWindow()
        if self.__conf.isOnWindows():
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

