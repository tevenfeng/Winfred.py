from enum import Enum, unique

from PySide6.QtCore import Signal, QObject


@unique
class WinfredMode(Enum):
    NormalMode = 1              # only search bar
    ListMode = 2                # search bar and list
    DisplayMode = 3             # search bar, list and preview


class StatusManager(QObject):
    winfredModeChangeSignal = Signal(WinfredMode)

    def __init__(self):
        super(StatusManager, self).__init__()
        self.__is_activated = True
        self.__current_mode = WinfredMode.NormalMode

    def getWinfredMode(self):
        return self.__current_mode

    def setWinfredMode(self, new_mode: WinfredMode):
        if new_mode == self.__current_mode:
            return
        self.winfredModeChangeSignal.emit(new_mode)
        self.__current_mode = new_mode

    def isWinfredActivated(self):
        return self.__is_activated

    def setWinfredActivated(self, is_activated: bool):
        self.__is_activated = is_activated
