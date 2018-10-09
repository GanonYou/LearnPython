import random
secretNum = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
count = 0

while True:
    print('Take a guess')
    guessNum = int(input())
    count = count + 1
    if guessNum < secretNum:
        print('Your guess is too low.')
        continue
    elif guessNum > secretNum:
        print('Your guess is too high')
        continue
    else:
        print('Good job!You guess the right number in ' + str(count) + ' times.')
        break
