__author__ = 'Ivelin'

from enum import Enum

class RiskType(Enum):

    Sensitivity=1
    Exposure=2

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        if name in [x.name for x in RiskType]:
            return cls[name]
        else:
            raise RuntimeError('Asset class'+name+' is not defined')

