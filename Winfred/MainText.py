from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont


class MainText(QTextEdit):
    def __init__(self):
        super(MainText, self).__init__()
        self.textContent = ""

        font = QFont()
        font.setPointSize(42)
        self.setFont(font)
        self.setText(self.textContent)

