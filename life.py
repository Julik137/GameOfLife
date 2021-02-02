import numpy as np
import pygame as pyg
#from numba import njit
# > 3: 1 -> 0 overpopulation
# < 2: 1 -> 0 underpopulation
# = 3: 0 -> 1 reproduction

@np.vectorize
def printer(num):
    if num == 0:
        return ' '
    return '#'



#np.random.seed(0)
n, m = 200, 200

board = np.random.randint(0, 2, (n, m))

def countNeighbour(i, j):
    c = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if 0 <= i+x < m and 0 <= j+y < n:
                c += board[i+x][j+y]

    c -= board[i][j]
    return c


def nextBoard():
    newBoard = np.zeros((n, m))
    for row in range(n):
        for coloumn in range(m):
            neighbour = countNeighbour(row, coloumn)

            if board[row][coloumn] == 0:
                if neighbour == 3:
                    newBoard[row][coloumn] = 1
                    
            else:
                if neighbour == 2 or neighbour == 3:
                    newBoard[row][coloumn] = 1

    return newBoard
'''
for i in range(100):
    board = nextBoard()
    print(printer(board))
    input()
'''




width = height = 800
dimensions = n
sq_size = height / dimensions
maxFPS = 60

def drawBoard(screen):
    colors = [pyg.Color("black"), pyg.Color("white")]

    for i in range(n):  # rows
        for j in range(m):  # columns

            pyg.draw.rect(screen, colors[int(board[i][j])], pyg.Rect(j * sq_size, i * sq_size, sq_size, sq_size))

pyg.init()
screen = pyg.display.set_mode((width, height))
screen.fill(pyg.Color("white"))
running = True


while running:
    for i in pyg.event.get():
        if i.type == pyg.QUIT:  # keyboard clicks
            running = False

    board = nextBoard()
    drawBoard(screen)
    pyg.display.flip()


