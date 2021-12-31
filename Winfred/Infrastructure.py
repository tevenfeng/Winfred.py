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


def detectOS():
    platform_str = platform.system()
    if platform_str == 'Windows':
        return OsPlatform.Windows
    elif platform_str == 'Linux':
        return OsPlatform.Linux
    elif platform_str == 'Darwin':
        return OsPlatform.macOS
    else:
        return OsPlatform.Unknown


class ConfManager(object):
    def __init__(self):
        self.__os = detectOS()

        if self.__os == OsPlatform.Linux:
            self.mainTextFontSize = 24
            self.__userProfileDir = os.path.expandvars("$HOME")
        elif self.__os == OsPlatform.Windows:
            self.mainTextFontSize = 28
            self.__userProfileDir = os.path.expandvars("%userprofile%")
        elif self.__os == OsPlatform.macOS:
            self.mainTextFontSize = 42
            self.__userProfileDir = os.path.expandvars("$HOME")

        self.__winfredHomePath = os.path.join(self.__userProfileDir, ".winfred")
        if not os.path.exists(self.__winfredHomePath):
            os.mkdir(self.__winfredHomePath)

        self.__confFilePath = os.path.join(self.__winfredHomePath, "winfred.conf")
        self.__logFilePath = os.path.join(self.__winfredHomePath, "winfred.log")
        logging.basicConfig(filename=self.__logFilePath, level=logging.DEBUG,
                            format='%(levelname)s %(asctime)s [%(filename)s:%(lineno)d]%(message)s')

        logging.info("Conf init, platform detected: %s", self.__os)
        logging.info("Conf init, winfred HOME: %s", self.__winfredHomePath)

    def getOSPlatform(self):
        return self.__os

    def getUserProfilePath(self):
        return self.__userProfileDir

    def getWinfredHomePath(self):
        return self.__winfredHomePath

    def getConfigFilePath(self):
        return self.__confFilePath

    def getLogFilePath(self):
        return self.__logFilePath
