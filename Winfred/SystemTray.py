import logging

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu


class SystemTray(QSystemTrayIcon):
    def __init__(self):
        super(SystemTray, self).__init__()

        icon = QIcon("../assets/Winfred64.ico")
        self.setIcon(icon)

        # Creating the options
        menu = QMenu()
        option1 = QAction("Geeks for Geeks")
        option2 = QAction("GFG")
        menu.addAction(option1)
        menu.addAction(option2)

        # Adding options to the System Tray
        self.setContextMenu(menu)
