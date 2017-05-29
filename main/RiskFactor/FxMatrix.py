__author__ = 'Ivelin'

from main.RiskFactor.Currency import Currency
from collections import OrderedDict
import numpy as np
import copy

class FxMatrix(object):

    def __init__(self, currencies, rates):
        self.currencies = currencies # OrderedDict() # currency integer
        self.rates = rates # list(list()) # matrix of fx rates

    def getRate(self, ccy1, ccy2):
        if ccy1==ccy2:
            return 1.0
        index1 = self.currencies.get(ccy1, 'Null')
        index2 = self.currencies.get(ccy2, 'Null')
        if index1!='Null' and index2!='Null':
            return self.rates[index1][index2]
        else:
            raise TypeError('no rate found for'+ccy1+'/'+ccy2 +
                            ' FX matrix only contains rates for'+ self.currencies.keys())


class FxMatrixBuilder(object):

    MINIMAL_MATRIX_SIZE = 2

    def __init__(self):
        self.currencies=OrderedDict() # currency integer
        self.rates=np.zeros([self.MINIMAL_MATRIX_SIZE, self.MINIMAL_MATRIX_SIZE]) # matrix of fx rates

    def build(self):
        return FxMatrix(self.currencies, self.rates)

    def merge(self, other):
        #find common ccies
        common = [x for x in self.currencies.keys() if x in other.currencies.keys()]
        if not common:
            raise ValueError('There are no currencies in common betweeen'+
                             self.currencies.keys()+' and '+other.currencies.keys())
        #add in all other currencies

    def __getRate(self, ccy1, ccy2):
        i = self.currencies.get(ccy1)
        j = self.currencies.get(ccy2)
        return self.rates[i][j]

    def addRate(self, ccy1, ccy2, rate):
        pass

    def addInitialCurrenyPair(self, ccy1, ccy2, rate):
        self.currencies[ccy1]=0
        self.currencies[ccy2]=1
        self.rates[0][0]=1.0
        self.rates[0][1]=rate
        self.rates[1][1]=1.0
        self.rates[1][0]=1.0/rate

    def addExistingCurrencyPair(self, ccy1, ccy2, rate):
        #ensure capacity
        self.ensureCapacity([ccy1, ccy2])
        #devide exisit/other ccy
        existingCcy = ccy1 if ccy1 in self.currencies.keys() else ccy2
        otherCcy = ccy1 if ccy2==existingCcy else ccy2
        #get the correct format of the rate
        updatedRate = rate if existingCcy==ccy2 else 1.0/rate
        #get the Matrix index
        indexExist = self.currencies.get(existingCcy)
        indexOther = len(self.currencies)
        #add new ccy to dict and Matrix
        self.currencies[otherCcy]=indexOther
        self.rates[indexOther][indexOther]=1.0
        #update all cells of matrix
        for i in range(indexOther):
            convertedRate = updatedRate * self.rates[indexExist][i]
            self.rates[indexOther][i] = convertedRate
            self.rates[i][indexOther] = 1.0/convertedRate



    def addNewCurrencyPair(self, ccy1, ccy2, rate):
        #ensure capacity
        self.ensureCapacity([ccy1, ccy2])
        #index of ccy1 ccy2
        ccy1Index = len(self.currencies)+1
        ccy2Index = len(self.currencies)+2
        self.rates[ccy1Index][ccy2Index]=1.0
        self.rates[ccy1Index][ccy2Index]=rate
        self.rates[ccy2Index][ccy2Index]=1.0
        self.rates[ccy2Index][ccy1Index]=1.0/rate



    def updateExistingPair(self, ccy1, ccy2, rate):
        ccy1Index = self.currencies.get(ccy1)
        ccy2Index = self.currencies.get(ccy2)
        self.rates[ccy1Index][ccy2Index]=rate
        self.rates[ccy2Index][ccy1Index]=1.0/rate


    def addCurrencyPair(self, ccy1, ccy2, rate):
        if ccy1 in self.currencies.keys() and ccy2 in self.currencies.keys():
            self.updateExistingPair(ccy1, ccy2, rate)
        elif ccy1 in self.currencies.keys() or ccy2 in self.currencies.keys():
            self.addExistingCurrencyPair(ccy1, ccy2, rate)
        else:
            self.addNewCurrencyPair(ccy1, ccy2, rate)


    def ensureCapacity(self, newCurrencies):
        newCurrencies.extend(self.currencies.keys())
        distinctCcy=set(newCurrencies)
        size=len(distinctCcy)
        if size > len(self.rates):
            self.addCapacity(size)

    def addCapacity(self, requiredOrder):
        sizeToAdd=requiredOrder-len(self.rates)
        '''
        extList=[None]*sizeToAdd
        newMatrix=[x.extend(extList) for x in self.rates]
        newArrays=[[None]*requiredOrder]*sizeToAdd
        newMatrix.extend(newArrays)
        #assign to self.rates
        '''
        newMatrix = np.zeros([requiredOrder, requiredOrder])
        newMatrix[:len(self.rates),:len(self.rates)]=self.rates
        self.rates=newMatrix


def Main():
    eur = Currency.of("EUR")
    usd = Currency.of("USD")
    gbp = Currency.of("GBP")

    builder = FxMatrixBuilder()
    print(builder.currencies)
    print(builder.rates)
    builder.addInitialCurrenyPair(usd, eur, 1.2)
    print(builder.currencies)
    print(builder.rates)
    builder.addCurrencyPair(eur, gbp, 1.1)
    print(builder.currencies)
    print(builder.rates)



'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()