import configparser
import logging
import os
import sys

from Winfred.Infrastructure.PlatformManager import OsPlatform, PlatformManager


class ConfManager(object):
    def __init__(self):
        self.__isDebugMode = False
        self.__configParser = configparser.ConfigParser()
        self.__os = PlatformManager.detectOS()
        self.__Confs = {}

        if getattr(sys, 'frozen', False):
            self.__assets_path = os.path.join(sys._MEIPASS, "assets")
        else:
            self.__assets_path = os.path.join(os.path.dirname(__file__), "../assets")

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

        self.__configFilePath = os.path.join(self.__winfredHomePath, "winfred.conf")
        self.loadAllConfig()

        self.__logFilePath = os.path.join(self.__winfredHomePath, "winfred.log")
        self.__loggingLevel = logging.WARNING
        if self.__isDebugMode:
            self.__loggingLevel = logging.DEBUG
        logging.basicConfig(filename=self.__logFilePath, level=self.__loggingLevel,
                            format='%(levelname)s %(asctime)s [%(filename)s:%(lineno)d]%(message)s')

        logging.info("Conf init, platform detected: %s", self.__os)
        logging.info("Conf init, winfred HOME: %s", self.__winfredHomePath)

    def getOSPlatform(self):
        return self.__os

    def isOnWindows(self):
        return self.__os == OsPlatform.Windows

    def isOnLinux(self):
        return self.__os == OsPlatform.Linux

    def isOnMacOS(self):
        return self.__os == OsPlatform.macOS

    def getUserProfilePath(self):
        return self.__userProfileDir

    def getWinfredHomePath(self):
        return self.__winfredHomePath

    def getConfigFilePath(self):
        return self.__configFilePath

    def getLogFilePath(self):
        return self.__logFilePath

    def loadAllConfig(self):
        if os.path.exists(self.__configFilePath) and os.path.isfile(self.__configFilePath):
            self.__configParser.read(self.__configFilePath, encoding='utf-8')
            for key in self.__configParser['DEFAULT']:
                self.__Confs[key] = self.__configParser['DEFAULT'][key]
                if key == 'debug_mode' and self.__configParser['DEFAULT'][key] == 'yes':
                    self.__isDebugMode = True

    def getAllConfs(self):
        return self.__Confs

    def getConfByName(self, key_name):
        if key_name in self.__Confs:
            return self.__Confs[key_name]
        return None

    def getAssetsPath(self):
        return self.__assets_path

    def isDebugMode(self):
        return self.__isDebugMode
