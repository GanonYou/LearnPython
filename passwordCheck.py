import re

def checkStrong(password):
    eightRegex = re.compile(r'.{8}.*')
    lowerRegex = re.compile(r'[a-z]+')
    upperRegex = re.compile(r'[A-Z]+')
    numberRegex = re.compile(r'\d+')
    eightResult = eightRegex.search(password)
    lowerResult = lowerRegex.search(password)
    upperResult = upperRegex.search(password)
    numberResult = numberRegex.search(password)
    if eightResult != None and lowerResult != None and upperResult != None and numberResult != None:
        return True
    else:
        return False

myPassword = 'L1l33333'
print(checkStrong(myPassword))