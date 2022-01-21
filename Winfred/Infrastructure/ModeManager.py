from enum import Enum, unique


@unique
class WinfredMode(Enum):
    NormalMode = 1              # only search bar
    ListMode = 2                # search bar and list
    DisplayMode = 3             # search bar, list and preview
