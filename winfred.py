import sys
from PyQt6.QtWidgets import QApplication

from Winfred.MainWindow import WinfredMainWindow
from Winfred.Infrastructure import ConfManager


def main():
    conf = ConfManager()

    app = QApplication(sys.argv)
    winfred = WinfredMainWindow(conf)
    winfred.show()
    winfred.hide()  # resolve lagging because of hiding on start
    if conf.getConfByName("hide_on_start") != "yes":
        winfred.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
