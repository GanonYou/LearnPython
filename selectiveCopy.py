import os,shutil

targetFile = './Target'

if not os.path.exists(targetFile):
    os.mkdir(targetFile)

for root,dirs,files in os.walk('.'):
    print("Search in " + root)
    if root != targetFile:
        for fileName in files:
            if fileName.find('.txt') != -1:
                shutil.copy(os.path.join(root,fileName),targetFile + '/' + os.path.basename(fileName))
