__author__ = 'Ivelin'

#-------------------------------------------------------------------------------
# Author:       Ivelin Angelov
# Written:      13/11/2016
# Last Updated: 13/11/2016

# Filename:     RiskFactor.py
# Python used:  3.4
#-------------------------------------------------------------------------------
# Description:  Serves as the main class for Asset Class types
#-------------------------------------------------------------------------------
# Log of changes:
# ...
#-------------------------------------------------------------------------------

import abc
from abc import ABCMeta

from main.Utils.ArgChecker import typeassert
from main.RiskFactor.Currency import Currency


class RiskFactor(metaclass=ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass

@typeassert(currency = Currency)
class FxRiskFactor(RiskFactor):

    def __init__(self, currency):
        super(FxRiskFactor, self).__init__()
        self.currency=currency

    def __str__(self):
        return self.currency.name

    @classmethod
    def of(cls, currency):
        if isinstance(currency, Currency):
            return cls(currency)
        elif isinstance(currency, str):
            return cls(Currency.of(currency))
        else:
            raise TypeError('FX risk factor cannot be defined with '+currency)

def Main():
    fx=FxRiskFactor.of('EUR')
    print(fx)
    curr=Currency.of('GBP')
    fx2=FxRiskFactor.of(curr)
    print(fx2)


'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
