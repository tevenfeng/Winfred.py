import logging

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu


class SystemTray(QSystemTrayIcon):
    def __init__(self, main_app, icon, parent=None):
        super(SystemTray, self).__init__(icon, parent)
        self.setVisible(True)

        # Creating the options
        menu = QMenu(parent)

        option1 = QAction("Geeks for Geeks")
        option2 = QAction("GFG")
        menu.addAction(option1)
        menu.addAction(option2)

        quit_action = QAction("Quit")
        quit_action.triggered.connect(main_app.quit)
        menu.addAction(quit_action)

        # Adding options to the System Tray
        self.setContextMenu(menu)
