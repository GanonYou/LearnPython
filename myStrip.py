import re

def my_strip(s,arg = ' '):
    if arg == ' ':
        removeRegex = re.compile(r'^\s* | \s*$')
    else:
        start = '^(' + arg + ')+'
        end = '(' + arg + ')+$'
        removeRegex = re.compile(start + '|' + end)
    ss = removeRegex.sub('',s)
    return ss

myString1 = '    asveg 52 g 52wrbsr    '
print(my_strip(myString1))
myString2 = 'SpamSpamBaconSpamEggsSpamSpam'
print(my_strip(myString2,'Spam'))