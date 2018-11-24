import random
guess = ''
while guess not in ('heads','tails'):
    print("Guess the coin toss!Enter heads or tails:")
    guess = input()

num = random.randint(0,1) #0代表heads,1代表tails
if num == 0:
    toss = 'heads'
else:
    toss = 'tails'
    
if toss == guess:
    print("You got it!")
else:
    print("Nope!Guess again:")
    guess = input()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope!You are stupid...")