#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Strategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def return_column(self, board):
        """This method must be overridden"""
        pass
