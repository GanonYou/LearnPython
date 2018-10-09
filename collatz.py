def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1

while True:
    print('Enter number:')
    try:
        num = int(input())
    except Exception as e:
        print(e)
        continue
    break

while num != 1:
    num = collatz(num)
    print(num)
