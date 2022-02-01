from PySide6.QtWidgets import QListWidgetItem

from Winfred.ViewModels.ResultItemModel import BaseResultItemModel


class ResultItemView(QListWidgetItem):
    def __init__(self, item_model: BaseResultItemModel):
        super(ResultItemView, self).__init__()
        self.__item_model = item_model

        self.setText(self.__item_model.getMainTitle())
