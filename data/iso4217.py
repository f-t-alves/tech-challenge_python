import csv

currencyList = {}
dictRow = {}

with open('data/iso4217.csv') as csvfile:
    readData = csv.reader(csvfile, delimiter=',')
    next(readData)
    for row in readData:
        #print("'",row[0].lower(),"': {'symbol': '",row[0],"', 'numcode': ",row[1],", 'decimals': ",row[2],"'name': '",row[3],"'}",sep='',flush=True)
        key = row[0].lower()
        dictRow['symbol'] = row[0]
        dictRow['numcode'] = int(row[1])
        dictRow['decimals'] = int(row[2])
        dictRow['name'] = row[3]
        currencyList[key] = dictRow.copy()
