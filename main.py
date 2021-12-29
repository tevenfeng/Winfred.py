import sys
import logging
from PyQt6.QtWidgets import QApplication

from Winfred.MainWindow import WinfredMainWindow
from Winfred.Conf import Conf


def main():
    conf = Conf()

    app = QApplication(sys.argv)
    winfred = WinfredMainWindow(conf)
    winfred.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
