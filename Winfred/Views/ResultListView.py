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

        temp_model1 = SplitResultItemModel("test_main_title1", "test_sub_title", "", "test_main_title")
        temp_model2 = SplitResultItemModel("test_main_title2", "test_sub_title", "", "test_main_title")
        temp_model3 = SplitResultItemModel("test_main_title3", "test_sub_title", "", "test_main_title")
        item_list = [temp_model1, temp_model2, temp_model3]

        self.addItems(item_list)

        self.itemClicked.connect(self.OnSelectedClicked)

    def addItems(self, item_list: list[BaseResultItemModel]):
        for item in item_list:
            if isinstance(item, BaseResultItemModel):
                new_item = ResultItemView(item)
                self.addItem(new_item)

    def OnSelectedClicked(self, current):
        print(current.text())
        print(self.currentRow())
        target_item = self.takeItem(self.currentRow())
        self.insertItem(0, target_item)

        # Todo: need to hide and reset mainwindow
        if self.count() > 0:
            self.setCurrentRow(0)
