import os,re,shutil

datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
''',re.VERBOSE)

for usaFileName in os.listdir('test'):
    mo = datePattern.search(usaFileName)
    if mo == None:
        continue
    else:
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
    
    euFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    absWorkingDir = os.path.abspath('test')
    usaFileName = os.path.join(absWorkingDir,usaFileName)
    euFileName = os.path.join(absWorkingDir,euFileName)
    shutil.move(usaFileName,euFileName)





