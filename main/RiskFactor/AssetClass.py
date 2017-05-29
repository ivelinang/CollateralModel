__author__ = 'Ivelin'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      13/11/2016
# Last Updated: 13/11/2016

# Filename:     AssetClass.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for Asset Class types
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

from enum import Enum

class AssetClass(Enum):

    #Equity
    Equity=1
    #Interest rates
    Interest_Rates=2
    #Credit
    Credit=3
    #Commodity
    Commodity=4

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        if name in [x.name for x in AssetClass]:
            return cls[name]
        else:
            raise RuntimeError('Asset class'+name+' is not defined')

def Main():
    print(AssetClass.Equity)
    asset = AssetClass.create('Credit')
    print(asset)
    asser2 = AssetClass.create('bou')

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
