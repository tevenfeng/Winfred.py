import logging

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import QSystemTrayIcon, QMenu


class SystemTray(QSystemTrayIcon):
    def __init__(self, main_app, icon, parent=None):
        super(SystemTray, self).__init__(icon, parent)
        self.setVisible(True)

        # Creating the options
        menu = QMenu(parent)
        menu.setStyleSheet("background-color: white; color: black;")

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(main_app.quit)
        menu.addAction(quit_action)

        # Adding options to the System Tray
        self.setContextMenu(menu)
        self.activated.connect(self.showMenuOnTrigger)

    def showMenuOnTrigger(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Context:
            self.contextMenu().show()
