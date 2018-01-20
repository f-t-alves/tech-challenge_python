class clientAccount:
    def __init__(self,accountNumber):
        self.__accountNumber = accountNumber
        self.__clientFirstName = 'John'
        self.__clientMiddleName = None
        self.__clientLastName = 'Doe'
        self.wallets = {}
        self.wallets['USD'] = currencyWallet('dollar','USD')
        self.wallets['BRL'] = currencyWallet('real','BRL')

    def move(self,amount,currency):
        try:
            currency = currency.upper()
        except:
            print('currency type must be a string')
            return 'currency type must be a string'
        if type(amount) != type(10):
            print('amount must be integer')
            return 'amount must be integer'
        else:
            if currency == 'USD':
                return self.wallets[currency].moveBalance(amount)
            if currency == 'BRL':
                return self.wallets[currency].moveBalance(amount)
        print('currency not supported')
        return 'currency not supported'

    def status(self):
        balances = {}
        print('Balances:')
        for key in self.wallets:
            balances[key] = self.wallets[key].currencyBalance
        return balances

class currencyWallet:
    def __init__(self,name,symbol):
        self.__currencyBalance = 0
        self.__currencyDecimals = 0
        self.__currencyName = name
        self.__currencySymbol = symbol.upper()

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

    def moveBalance(self,value):
        tryValue = self.currencyBalance + value
        if tryValue < 0:
            print('Withdrawal exceeds balance')
            return 'Withdrawal exceeds balance'
        else:
            self.currencyBalance = tryValue
            return False
