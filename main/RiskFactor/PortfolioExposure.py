__author__ = 'Ivelin'

from main.RiskFactor.RiskFactor import RiskFactor
from main.RiskFactor.Currency import Currency
from main.Utils import typeassert

class PortfolioExposure(object):

    def __init__(self, riskFactor, amount, currency):
        self.riskFactor=riskFactor
        self.amount=amount
        self.currency=currency

    @classmethod
    def of(cls, riskFactor, amount, currency):
        return cls(riskFactor, amount, currency)

