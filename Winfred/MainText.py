from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont, QColor


class MainText(QTextEdit):
    def __init__(self, font_size):
        super(MainText, self).__init__()
        self.textContent = ""

        font = QFont()
        font.setPointSize(font_size)
        self.setFont(font)
        self.setText(self.textContent)
        self.setTextColor(QColor.fromRgb(255, 255, 255))
        self.setStyleSheet("border: 0;")
