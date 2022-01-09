import logging

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtCore import Signal


class SystemTray(QSystemTrayIcon):
    systemTrayDisplaySignal = Signal()
    systemTrayQuitSignal = Signal()

    def __init__(self, icon, parent=None):
        super(SystemTray, self).__init__(icon, parent)
        self.setVisible(True)

        # Creating the options
        menu = QMenu(parent)
        menu.setStyleSheet("background-color: white; color: black;")

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.handleTrayIconQuit)
        menu.addAction(quit_action)

        # Adding options to the System Tray
        self.setContextMenu(menu)
        self.activated.connect(self.handleTrayIconClicked)

    def handleTrayIconClicked(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Context:
            self.contextMenu().show()
        elif reason == QSystemTrayIcon.ActivationReason.Trigger\
                or reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.systemTrayDisplaySignal.emit()

    def handleTrayIconQuit(self):
        self.systemTrayQuitSignal.emit()
