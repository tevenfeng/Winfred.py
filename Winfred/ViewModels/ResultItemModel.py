from PySide6.QtCore import QObject


class BaseResultItemModel(QObject):
    def __init__(self, main_title: str, sub_title: str):
        super(BaseResultItemModel, self).__init__()
        self.__main_title = main_title
        self.__sub_title = sub_title

    def getMainTitle(self):
        return self.__main_title

    def setMainTitle(self, main_title: str):
        self.__main_title = main_title

    def getSubTitle(self):
        return self.__sub_title

    def setSubTitle(self, sub_title: str):
        self.__sub_title = sub_title


class IconResultItemModel(BaseResultItemModel):
    def __init__(self, main_title, sub_title, icon_path):
        super(IconResultItemModel, self).__init__(main_title, sub_title)
        self.__icon_path = icon_path

    def getIconPath(self):
        return self.__icon_path

    def setIconPath(self, icon_path: str):
        self.__icon_path = icon_path


class SplitResultItemModel(IconResultItemModel):
    def __init__(self, main_title, sub_title, icon_path, main_content):
        super(SplitResultItemModel, self).__init__(main_title, sub_title, icon_path)
        self.__main_content = main_content

    def getMainContent(self):
        return self.__main_content

    def setMainContent(self, main_content: str):
        self.__main_content = main_content
