#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = ['aaa', 'bbb']
result = ''

for i in range(len(spam)):
    if i == len(spam) - 1:
        result += 'and ' + spam[i]
        break
    result += spam[i] + ', '

print(result)
