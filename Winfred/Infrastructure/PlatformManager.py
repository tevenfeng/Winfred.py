import platform
from enum import Enum, unique


@unique
class OsPlatform(Enum):
    Windows = 1
    Linux = 2
    macOS = 3
    Unknown = 4


class PlatformManager(object):
    @staticmethod
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
