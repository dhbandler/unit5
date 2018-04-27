#Sam Smedinghoff
#4/27/18
#matrixDemo.py - lists inside of lists

def printBoard(board):
    for r in range(0,3):
        for c in range(0,3):
            print(board[r][c],end=' ')
        print()

board = [['a','b','c'],['d','e','f'],['g','h','i']]
printBoard(board)

row = int(input('Enter a row: '))
col = int(input('Enter a column: '))
board[row-1][col-1] = 'X'
printBoard(board)
