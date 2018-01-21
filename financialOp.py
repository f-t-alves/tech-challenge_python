from classes.iso4217 import currencyList
import classes.clientAccount

accounts = []
accounts.append(clientAccount())

accounts[0].addWallet(currencyList['usd'])
