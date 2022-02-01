from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit


class MainText(QLineEdit):
    def __init__(self, font_size, parent=None):
        super(MainText, self).__init__(parent)

        self.setFontSize(font_size)

        self.setStyleSheet("border: 0; color: white;")
        self.setAlignment(Qt.AlignVCenter)

    def setFontSize(self, font_size):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def setContent(self, str_text):
        self.setText(str_text)

    def getContent(self):
        return self.text()

