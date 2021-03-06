import logging
import os.path

from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget
from PySide6.QtCore import Qt, QMargins, QPointF, Signal
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication, QIcon
from pynput import keyboard

from Winfred.Core.StatusManager import WinfredMode, StatusManager
from Winfred.Core.SnippetManager import SnippetManager
from Winfred.Views.MainText import MainText
from Winfred.Views.SystemTray import SystemTray
from Winfred.Views.ResultListView import ResultListView


class WinfredMainWindow(QMainWindow):
    winfredQuitSignal = Signal()
    __winfredMainSearchShowSignal = Signal()
    __winfredClipboardShowSignal = Signal()

    def __init__(self, conf):
        super(WinfredMainWindow, self).__init__()
        self.__centralWidget = None
        self.__mainLayout = None
        self.__conf = conf
        self.__mainEdit = None
        self.__resultsList = None
        self.__systemTray = None
        self.__oldPos = self.pos()
        self.initUI(conf)

        self.__winfredStatusManager = StatusManager()
        self.__winfredStatusManager.winfredModeChangeSignal.connect(self.handleWinfredModeChangeSignal)

        self.__snippetManager = SnippetManager(conf)
        self.__snippetManager.snippetReplaceSignal.connect(self.handleSnippetReplaceSignal)

        QShortcut(QKeySequence(Qt.Key.Key_Escape), self, self.hide)
        self.__mainHotKeyListener = keyboard.GlobalHotKeys({
            "<ctrl>+<alt>": self.__winfredMainSearchShowSignal.emit,
            # "<cmd_l>+c": self.__winfredClipboardShowSignal.emit,
        })
        self.__mainHotKeyListener.start()

        self.__winfredMainSearchShowSignal.connect(self.showMainSearch)
        self.__winfredClipboardShowSignal.connect(self.showClipboard)

        self.__keyboardController = keyboard.Controller()

    def __del__(self):
        self.__mainHotKeyListener.stop()

    def initUI(self, conf):
        self.setWindowTitle("Winfred")
        icon_path = os.path.join(conf.getAssetsPath(), "winfred.ico")
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
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
        self.__mainLayout.addWidget(self.__mainEdit, 0, 0)

        self.__resultsList = ResultListView(self)
        self.__mainLayout.addWidget(self.__resultsList, 1, 0)
        self.__resultsList.hide()

        self.initSystemTrayIcon(conf)

    def getCurrentMode(self):
        return self.__winfredStatusManager.getWinfredMode()

    def setCurrentMode(self, mode: WinfredMode):
        self.__winfredStatusManager.setWinfredMode(mode)

    def shrinkSize(self):
        self.setFixedSize(700, 64)
        self.__resultsList.hide()

    def enlargeSize(self):
        self.setFixedSize(700, 640)
        self.__resultsList.show()

    def initSystemTrayIcon(self, conf):
        icon_path = os.path.join(conf.getAssetsPath(), "winfred.png")
        icon = QIcon(icon_path)
        self.__systemTray = SystemTray(icon, self)
        self.__systemTray.show()
        self.__systemTray.systemTrayDisplaySignal.connect(self.showMainSearch)
        self.__systemTray.systemTrayQuitSignal.connect(self.winfredQuit)

    def winfredQuit(self):
        self.winfredQuitSignal.emit()

    def show(self):
        self.setVisible(True)
        self.setFocus()
        self.__mainEdit.setFocus()
        self.__winfredStatusManager.setWinfredActivated(True)
        self.activateWindow()
        self.raise_()
        if self.__conf.isOnWindows():
            self.backspaceNTimes(1)     # use input event to force focus on the __mainEdit(Windows need this)

    def hide(self):
        self.setCurrentMode(WinfredMode.HideMode)
        self.__winfredStatusManager.setWinfredActivated(False)
        self.setVisible(False)
        self.clearFocus()

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

    def handleWinfredModeChangeSignal(self, new_mode: WinfredMode):
        if new_mode == WinfredMode.NormalMode:
            self.shrinkSize()
        elif new_mode == WinfredMode.ListMode:
            self.enlargeSize()
        elif new_mode == WinfredMode.DisplayMode:
            self.enlargeSize()

    def handleWinfredFocusChangedSignal(self):
        # self.hide function will not make isActiveWindow return False, so we have to manually do it
        if not self.__winfredStatusManager.isWinfredActivated() or not self.isActiveWindow():
            self.hide()

    def showMainSearch(self):
        current_mode = self.getCurrentMode()
        if current_mode == WinfredMode.HideMode:
            self.setCurrentMode(WinfredMode.NormalMode)
            self.show()
        elif current_mode == WinfredMode.NormalMode:
            self.hide()

    def showClipboard(self):
        self.setCurrentMode(WinfredMode.DisplayMode)
        self.show()
