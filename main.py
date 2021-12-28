import sys
from PyQt6.QtWidgets import QApplication

from Winfred.mainwindow import WinfredMainWindow


def main():
    app = QApplication(sys.argv)
    winfred = WinfredMainWindow()
    winfred.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
