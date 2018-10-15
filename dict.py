theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(tb):
    print(tb['top-L'] + '|' + tb['top-M'] + '|' + tb['top-R'])
    print('-+-+-')
    print(tb['mid-L'] + '|' + tb['mid-M'] + '|' + tb['mid-R'])
    print('-+-+-')
    print(tb['low-L'] + '|' + tb['low-M'] + '|' + tb['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '.Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
