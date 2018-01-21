from currencyWallet import *

class clientAccount:

    def __init__(self,accountNumber):
        self.__accountNumber = accountNumber
        self.__clientFirstName = 'John'
        self.__clientMiddleName = None
        self.__clientLastName = 'Doe'
        self.wallets = {}

        self.addWallet(currencyList['usd'])
        self.addWallet(currencyList['brl'])

        #self.wallets['USD'] = currencyWallet('dollar','USD')
        #self.wallets['BRL'] = currencyWallet('real','BRL')

    def addWallet(self,symbol):
        try:
            self.wallets[symbol] = currencyWallet(symbol)

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
