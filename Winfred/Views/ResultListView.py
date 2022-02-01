from PySide6.QtGui import QFont
from PySide6.QtWidgets import QListWidget

from Winfred.ViewModels.ResultItemModel import BaseResultItemModel, IconResultItemModel, SplitResultItemModel
from Winfred.Views.ResultItemView import ResultItemView


class ResultListView(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("border: none; color: white;")
        font = QFont()
        font.setPointSize(24)
        self.setFont(font)

        temp_model = SplitResultItemModel("test_main_title", "test_sub_title", "", "test_main_title")

        self.addItem(ResultItemView(temp_model))
