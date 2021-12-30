import os
import platform
import logging
from enum import Enum, unique


@unique
class OsPlatform(Enum):
    Windows = 1
    Linux = 2
    macOS = 3
    Unknown = 4


def detect_os():
    platform_str = platform.system()
    if platform_str == 'Windows':
        return OsPlatform.Windows
    elif platform_str == 'Linux':
        return OsPlatform.Linux
    elif platform_str == 'Darwin':
        return OsPlatform.macOS
    else:
        return OsPlatform.Unknown


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
