#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._color = None

    def set_color(self, color):
        self._color = color

    @abstractmethod
    def return_column(self, board):
        """This method must be overridden"""
        pass
