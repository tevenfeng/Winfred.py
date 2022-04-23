import sqlite3

from PySide6.QtCore import QObject


class DatabaseManager(QObject):
    def __init__(self):
        super(DatabaseManager, self).__init__()

        self.__db_connection = sqlite3.connect('winfred.db')

