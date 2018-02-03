def countDecimals(value):
    #Returns -integer- with number of decimal places in 'value', assuming either -float- or -integer-
    if type(value) != type(10) and type(value) != type(1.0):
        return 'value must be a number'
    string = str(value)
    length = len(string)
    decimalPosition = string.find('.') + 1
    decimalPlaces = length - decimalPosition
    if decimalPosition == 0:
        return 0
    else:
        return decimalPlaces

def insertDecimals(value,decimals):
    #Returns -string- of 'value' with 'decimals' decimal places, assuming 'value' is an -integer-
    if type(value) != type(10):
        return 'value must be an integer'
    if type(decimals) != type(10):
        return 'decimals must be an integer'
    if decimals == 0:
        return str(value)
    string = str(value)
    newString = string[:-decimals] + '.' + string[-decimals:]
    newValue = float(newString)
    offset = decimals - countDecimals(newValue)
    newString = str(newValue) + '0'*offset
    return newString
