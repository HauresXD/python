# Alphabet
#-----------------------------------------------------------
def alphabetLower():
    return 'abcdefghijklmnopqrstuvwxyz'

def alphabetUpper():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# SEARCH IN DICTONARY
#-----------------------------------------------------------
def findAll(where, what):
    q = 0
    z = 0
    for key, value in where.items():
        if key == what:
            return [key, value, z]
        elif value == what:
            return [key, value, z]
        else:
            q = 1
            z += 1
    if q == 1:
        return None

def findKey(where, what):
    q = 0
    z = 0
    for key, value in where.items():
        if value == what:
            return key
        elif z == what:
            return key
        else:
            q = 1
            z += 1
    if q == 1:
        return None

def findValue(where, what):
    q = 0
    z = 0
    for key, value in where.items():
        if key == what:
            return value
        elif z == what:
            return value
        else:
            q = 1
            z += 1
    if q == 1:
        return None

def findPlace(where, what):
    q = 0
    z = 0
    for key, value in where.items():
        if key == what:
            return z
        elif value == what:
            return z
        else:
            q = 1
            z += 1
    if q == 1:
        return None
