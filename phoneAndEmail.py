import pyperclip,re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?   #area code
(\s|-|\.)?           #sparator
(\d{3})              #first 3 digits
(\s|-|\.)?           #sparator
(\d{4})              #last 4 digits 
(\s*(ext|x|ext\.)\s*(\d{2,5}))?     #extension
)''',re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

