def increment_string(strng):
    letterStr = strng.rstrip('0123456789')
    digitStr = strng[len(letterStr):]
    
    if len(digitStr) == 0:
        return f'{letterStr}1'
    
    #Incremenet the digits
    digitStr = str(int(digitStr) + 1).zfill(len(digitStr))
    return letterStr + digitStr
