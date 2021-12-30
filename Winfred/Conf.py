import os
import logging

from .Infrastructure import detect_os, OsPlatform


class Conf(object):
    def __init__(self):
        self.winfredHomeDir = os.path.expandvars("$HOME/.winfred")
        if not os.path.exists(self.winfredHomeDir):
            os.mkdir(self.winfredHomeDir)

        self.confFilePath = os.path.join(self.winfredHomeDir, "winfred.conf")

        self.logFilePath = os.path.join(self.winfredHomeDir, "winfred.log")
        logging.basicConfig(filename=self.logFilePath, level=logging.DEBUG,
                            format='%(levelname)s %(asctime)s [%(filename)s:%(lineno)d]%(message)s')

        self.os = detect_os()
        logging.info("Conf init, platform detected: %s", self.os)

        if self.os == OsPlatform.Linux:
            self.mainTextFontSize = 24
        elif self.os == OsPlatform.Windows:
            self.mainTextFontSize = 28
        elif self.os == OsPlatform.macOS:
            self.mainTextFontSize = 42

