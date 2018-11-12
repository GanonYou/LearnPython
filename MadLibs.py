import os,re

madFile = open('mad.txt')
madContent = madFile.read()
madFile.close()

myRegex = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')
myResult = myRegex.finditer(madContent)
newContent = ""
pos = 0

for item in myResult:
    print("Please input a(an) " + str(item.group()).lower() + ":")
    words = input()
    newContent += madContent[pos:item.span()[0]] + words
    pos = item.span()[1]
newContent += madContent[pos:]

print(newContent)


        
        

