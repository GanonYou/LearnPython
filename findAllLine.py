import re,os

path = '/Users/YWY/PythonProgram/LearnPython'
userRegex = re.compile(r'silly')

for root,dir,files in os.walk(path):
    for fileName in files:
        if fileName.find('.txt') != -1:
            txtFile = open(os.path.join(path,fileName))
            lines = txtFile.readlines()
            for line in lines:
                userResult = userRegex.search(line)
                if userResult != None:
                    print(line)
