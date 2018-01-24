from classes.iso4217 import currencyList
from classes.clientAccount import clientAccount
import random

accounts = []
accounts.append(clientAccount(random.randrange(0,1000)))

accounts[0].addWallet(currencyList['usd'])
