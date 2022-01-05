import sys

from PyQt6.QtWidgets import QApplication

from Winfred.MainWindow import WinfredMainWindow
from Winfred.Infrastructure import ConfManager, OsPlatform
from Winfred.SystemTray import SystemTray


def main():
    conf = ConfManager()

    app = QApplication(sys.argv)
    winfred = WinfredMainWindow(conf)
    if conf.getOSPlatform() == OsPlatform.Linux:
        if conf.getConfByName("hide_on_start") != "yes":
            winfred.show()
    elif conf.getOSPlatform() == OsPlatform.Windows:
        winfred.show()
        winfred.hide()  # resolve lagging on Windows because of hiding on start
        if conf.getConfByName("hide_on_start") != "yes":
            winfred.show()

    systemTray = SystemTray()
    systemTray.setVisible(True)
    systemTray.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
