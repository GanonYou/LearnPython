import os,re,shutil

os.chdir('test')
currentDir = os.getcwd()
numberPattern = re.compile(r'bacon(\d\d\d)')

temp = []
for fileName in os.listdir():
    mo = numberPattern.search(fileName)
    if mo != None:
        number = int(mo.group(1))
        temp.append(number)

temp.sort()

for i in range(len(temp)):
    if temp[i] != i + 1:
        origin = str(temp[i]).zfill(3)
        new = str(i + 1).zfill(3)
        shutil.move(currentDir + '/bacon' + origin + '.txt',currentDir + '/bacon' + new + '.txt')




