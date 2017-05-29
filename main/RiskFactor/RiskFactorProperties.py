__author__ = 'Ivelin'

from main.RiskFactor.AssetClass import AssetClass
from main.RiskFactor.RiskType import RiskType
from main.RiskFactor.ShockType import ShockType, RelativeShock, AbsoluteShock
from main.Utils import typeassert

@typeassert(assetClass=AssetClass,
            riskType=RiskType,
            shockType=ShockType)
class RiskFactorProperties(object):

    def __init__(self, assetClass, riskType, shockType):
        self.assetClass=assetClass
        self.riskType=riskType
        self.shockType=shockType

    @classmethod
    def relativeShock(cls, assetClass, riskType, shift):
        return cls(assetClass, riskType, RelativeShock.of(shift))

    @classmethod
    def absoluteShock(cls, assetClass, riskType, shift):
        return cls(assetClass, riskType, AbsoluteShock.of(shift))
