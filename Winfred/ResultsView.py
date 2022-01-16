from PySide6.QtGui import QFont
from PySide6.QtWidgets import QListWidget, QListWidgetItem


class ResultsView(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("border: none; color: white;")
        font = QFont()
        font.setPointSize(24)
        self.setFont(font)
        self.addItem(QListWidgetItem("test"))