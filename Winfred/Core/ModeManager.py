from enum import Enum, unique

from PySide6.QtCore import Signal, QObject


@unique
class WinfredMode(Enum):
    NormalMode = 1              # only search bar
    ListMode = 2                # search bar and list
    DisplayMode = 3             # search bar, list and preview


class ModeManager(QObject):
    winfredModeChangeSignal = Signal(WinfredMode)

    def __init__(self):
        super(ModeManager, self).__init__()
        self.__current_mode = WinfredMode.NormalMode

    def getCurrentMode(self):
        return self.__current_mode

    def setCurrentMode(self, new_mode: WinfredMode):
        if new_mode == self.__current_mode:
            return
        self.winfredModeChangeSignal.emit(new_mode)
        self.__current_mode = new_mode
