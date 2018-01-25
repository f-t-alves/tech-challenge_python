class currencyWallet:
    def __init__(self,currencyProperties):
        self.currencyBalance = 0
        self.__currencySymbol = currencyProperties['symbol']
        self.__currencyName = currencyProperties['name']
        self.__currencyDecimals = currencyProperties['decimals']
        self.__currencyISOCode = currencyProperties['numcode']

    @property
    def currencyBalance(self):
        return self.__currencyBalance
    @currencyBalance.setter
    def currencyBalance(self,value):
        if type(value) != type(10):
            print('Error: balance must be integer')
        else:
            self.__currencyBalance = value


    @property
    def currencyDecimals(self):
        return self.__currencyDecimals
    @currencyDecimals.setter
    def currencyDecimals(self,value):
        if type(value) != type(10):
            print('Error: decimals must be integer')
        else:
            self.__currencyDecimals = value


    @property
    def currencyName(self):
        return self.__currencyName
    @currencyName.setter
    def currencyName(self,value):
        if type(value) != type('bla'):
            print('Error: name must be string')
        else:
            self.__currencyName = value


    @property
    def currencySymbol(self):
        return self.__currencySymbol
    @currencySymbol.setter
    def currencySymbol(self,value):
        if type(value) != type('bla'):
            print('Error: symbol must be string')
        else:
            self.__currencySymbol = value

    @property
    def currencyISOCode(self):
        return self.__currencyISOCode
    @currencyISOCode.setter
    def currencyISOCode(self,value):
        if type(value) != type(10):
            print('Error: ISO code must be integer')
        else:
            self.__currencyISOCode = value


    def moveBalance(self,value):
        tryValue = self.currencyBalance + value
        if tryValue < 0:
            print('Withdrawal exceeds balance')
            return 'Withdrawal exceeds balance'
        else:
            self.currencyBalance = tryValue
            return False
