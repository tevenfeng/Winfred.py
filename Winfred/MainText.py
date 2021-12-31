from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTextEdit, QLineEdit
from PyQt6.QtGui import QFont, QColor


class MainText(QLineEdit):
    def __init__(self, font_size):
        super(MainText, self).__init__()
        self.textContent = None

        self.setFontSize(font_size)

        self.setStyleSheet("border: 0;")
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter)

    def setFontSize(self, font_size):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)
        self.setText(self.textContent)
