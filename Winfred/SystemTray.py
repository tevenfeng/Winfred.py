import logging

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu, QStyle


class SystemTray(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTray, self).__init__(icon, parent)
        self.setVisible(True)

        # Creating the options
        menu = QMenu(parent)
        option1 = QAction("Geeks for Geeks")
        option2 = QAction("GFG")
        menu.addAction(option1)
        menu.addAction(option2)

        # Adding options to the System Tray
        self.setContextMenu(menu)
