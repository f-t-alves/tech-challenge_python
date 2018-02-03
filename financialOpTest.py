from data.iso4217 import currencyList
from classes.clientAccount import clientAccount
import random

accounts = []
accounts.append(clientAccount(random.randrange(0,1000)))

accounts[0].addWallet(currencyList['usd'])
accounts[0].addWallet(currencyList['bif'])
accounts[0].addWallet(currencyList['bhd'])
accounts[0].addWallet(currencyList['clf'])

print(accounts[0].move(100,'usd'))
print(accounts[0].move(-20.5,'usd'))
print(accounts[0].move(1.1,'bif'))

print(accounts[0].status())
