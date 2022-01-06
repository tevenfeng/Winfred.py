import os
import json
import logging

from PyQt6.QtCore import pyqtSignal, QObject

from pynput import keyboard


class SnippetManager(QObject):
    snippetReplaceSignal = pyqtSignal(int, str)

    def __init__(self, conf):
        super(SnippetManager, self).__init__()

        self.__snippetDir = conf.getConfByName("snippet_dir")
        if self.__snippetDir is None:
            self.__snippetDir = os.path.join(conf.getWinfredHomePath(), "snippets")

        self.__snippetsDict = {}
        self.loadSnippets(self.__snippetDir)

        self.__curStr = ""

        self.__snippetKeyboardListener = None

        self.initKeyboardListeners()

    def initKeyboardListeners(self):
        self.__snippetKeyboardListener = keyboard.Listener(on_press=self.listenKeyboard)
        self.__snippetKeyboardListener.start()

    def loadSnippets(self, snippet_dir):
        if os.path.exists(snippet_dir) and os.path.isdir(snippet_dir):
            for temp_name in os.listdir(snippet_dir):
                temp_name_full = os.path.join(snippet_dir, temp_name)
                if os.path.isdir(temp_name_full):
                    self.loadSnippets(temp_name_full)
                elif os.path.isfile(temp_name_full):
                    if not temp_name_full.endswith("json"):
                        continue
                    logging.info("SnippetManager loading: %s", temp_name_full)
                    with open(temp_name_full, encoding='utf-8') as input_file:
                        snippet_data = json.load(input_file)['alfredsnippet']
                        self.__snippetsDict[snippet_data["keyword"]] = snippet_data["snippet"]

    def listenKeyboard(self, key):
        try:
            if key.char == '$':
                self.__curStr = '$'
            else:
                self.__curStr += key.char
                if self.__curStr in self.__snippetsDict:
                    target_str = self.__snippetsDict[self.__curStr]
                    backspace_num = len(self.__curStr)
                    self.snippetReplaceSignal.emit(backspace_num, target_str)
                    self.__curStr = ""
                elif len(self.__curStr) > 15:
                    self.__curStr = ""
        except AttributeError:
            if key == keyboard.Key.backspace:
                self.__curStr = self.__curStr[:-1]
