__author__ = 'Ivelin'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      13/11/2016
# Last Updated: 13/11/2016

# Filename:     Currency.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for Currency type
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------
from main.Utils.ArgChecker import typeassert

@typeassert(name = str)

class Currency(object):

    def __init__(self, name):
        self.name=name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @classmethod
    def of(cls, name):
        return cls(name)

    def __eq__(self, other):
        return self.name==other.name

    def __hash__(self):
        return hash(self.name)

def Main():
    curr=Currency.of('EUR')
    print(curr)

    newC=Currency.of(3)

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
