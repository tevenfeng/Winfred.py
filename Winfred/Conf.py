from .Infrastructure import detect_os, OsPlatform
import logging


class Conf(object):
    def __init__(self):
        self.os = detect_os()
        logging.info("Conf init, platform detected: %s", self.os)

        if self.os == OsPlatform.Linux:
            self.mainTextFontSize = 24
        elif self.os == OsPlatform.Windows:
            self.mainTextFontSize == 24
        elif self.os == OsPlatform.macOS:
            self.mainTextFontSize == 42

