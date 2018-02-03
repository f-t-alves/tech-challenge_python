from classes.currencyWallet import *
from classes.utilities import countDecimals
from classes.utilities import insertDecimals

class clientAccount:

    def __init__(self,accountNumber):
        self.__accountNumber = accountNumber
        self.__clientFirstName = 'John'
        self.__clientMiddleName = None
        self.__clientLastName = 'Doe'
        self.wallets = {}

    def addWallet(self,currencyProps):
            self.wallets[currencyProps['symbol']] = currencyWallet(currencyProps)
            return False

    def move(self,amount,currency):
        try:
            currency = currency.upper()
        except:
            print('currency type must be a string')
            return 'currency type must be a string'
        try:
            amount = float(amount)
        except:
            print('amount must be a number')
            return 'amount must be a number'
        else:
            try:
                countedDecimals = countDecimals(amount)
                expectedDecimals = self.wallets[currency].currencyDecimals
                if countedDecimals > expectedDecimals:
                    return 'amount has too many decimal places'
                integerAmount = int(amount*10**expectedDecimals)
                return self.wallets[currency].moveBalance(integerAmount)
            except:
                return countDecimals(amount)
        print('account does have a wallet in this currency')
        return 'account does have a wallet in this currency'

    def status(self):
        balances = {}
        print('Balances:')
        for key in self.wallets:
            balances[key] = insertDecimals(self.wallets[key].currencyBalance,self.wallets[key].currencyDecimals)
        return balances
