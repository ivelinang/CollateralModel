__author__ = 'Ivelin'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      13/11/2016
# Last Updated: 13/11/2016

# Filename:     ShockType.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for shock type
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

import abc
from abc import ABCMeta

class ShockType(metaclass=ABCMeta):

    def __init__(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def calcShiftedValue(initial, shock):
        pass

class AbsoluteShock(ShockType):

    def __init__(self):
        super(AbsoluteShock,self).__init__()

    @staticmethod
    def calcShiftedValue(initial, shock):
        return initial+shock

class RelativeShock(ShockType):

    def __init__(self):
        super(RelativeShock, self).__init__()

    @staticmethod
    def calcShiftedValue(initial, shock):
        return initial*(1.0+shock)