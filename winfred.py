import sys

from PySide6.QtWidgets import QApplication

from Winfred.Views.MainWindow import WinfredMainWindow
from Winfred.Infrastructure.PlatformManager import OsPlatform
from Winfred.Core.ConfManager import ConfManager


def main():
    conf = ConfManager()

    app = QApplication(sys.argv)
    winfred = WinfredMainWindow(conf)
    winfred.winfredQuitSignal.connect(app.quit)
    if conf.getOSPlatform() == OsPlatform.Linux or conf.getOSPlatform() == OsPlatform.macOS:
        if conf.getConfByName("hide_on_start") != "yes":
            winfred.show()
    elif conf.getOSPlatform() == OsPlatform.Windows:
        winfred.show()
        winfred.hide()  # resolve lagging on Windows because of hiding on start
        if conf.getConfByName("hide_on_start") != "yes":
            winfred.show()

    if conf.getConfByName("hide_on_lose_focus") == "yes":
        app.focusChanged.connect(winfred.handleWinfredFocusChangedSignal)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
