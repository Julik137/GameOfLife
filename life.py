import numpy as np
import pygame as pyg
# > 3: 1 -> 0 overpopulation
# < 2: 1 -> 0 underpopulation
# = 3: 0 -> 1 reproduction


# @np.vectorize
def printer(num):
    if num == 0:
        return ' '
    return '#'


n = 100  # number of rows
m = 100  # numver of columns

board = np.random.randint(0, 2, (n, m))

# without boundary condition


def countNeighbour(i, j):
    c = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if 0 <= i+x < n and 0 <= j+y < m:  # fixed mischanged n and m
                a = i+x
                b = j+y
            c += board[a][b]
    c -= board[i][j]
    return c

# with periodic boundary condition


def countNeighbourPB(i, j):
    c = 0
    if 0 < i < n-1 and 0 < j < m-1:  # hier können alle 8 nachbarn gezählt werden
        for x in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                c += board[i+x][j+y]

        c -= board[i][j]
    elif i == 0 and j == 0:  # oben links
        c += board[0][1]
        c += board[1][0]
        c += board[1][1]
        c += board[-1][-1]
        c += board[-1][0]
        c += board[0][-1]
        c += board[1][-1]
        c += board[-1][1]
    elif i == 0 and j == m-1:  # oben rechts
        c += board[0][0]
        c += board[-1][-1]
        c += board[-1][0]
        c += board[0][-2]
        c += board[1][-1]
        c += board[-1][-2]
        c += board[1][0]
        c += board[-1][-1]
    elif i == n-1 and j == 0:  # unten links
        c += board[-1][1]
        c += board[-2][0]
        c += board[-2][-2]
        c += board[0][-1]
        c += board[0][0]
        c += board[-1][-1]
        c += board[0][1]
        c += board[-2][-1]
    elif i == n-1 and j == m-1:  # unten rechts
        c += board[-2][-1]
        c += board[-1][-2]
        c += board[-2][-2]
        c += board[0][0]
        c += board[-2][0]
        c += board[0][-2]
        c += board[-1][0]
        c += board[0][-1]
    elif i == 0 and 0 < j < m-1:  # oben
        c += board[-1][j+1]
        c += board[-1][j]
        c += board[-1][j-1]
        c += board[1][j]
        c += board[1][j]
        c += board[1][j]
        c += board[0][j-1]
        c += board[0][j+1]
    elif i == n-1 and 0 < j < m-1:  # unten
        c += board[-2][j+1]
        c += board[-2][j]
        c += board[-2][j-1]

        c += board[0][j+1]
        c += board[0][j]
        c += board[0][j-1]

        c += board[-1][j-1]
        c += board[-1][j+1]
    elif 0 < i < n-1 and j == 0:  # links
        c += board[i+1][-1]
        c += board[i][-1]
        c += board[i-1][-1]
        c += board[i+1][1]
        c += board[i][1]
        c += board[i-1][1]
        c += board[i+1][0]
        c += board[i-1][0]
    elif 0 < i < n-1 and j == m-1:  # rechts
        c += board[i+1][-2]
        c += board[i][-2]
        c += board[i-1][-2]
        c += board[i+1][0]
        c += board[i][0]
        c += board[i-1][0]
        c += board[i+1][j]
        c += board[i-1][j]
    return c


def nextBoard(f=1):
    newBoard = np.zeros((n, m))
    for row in range(n):
        for coloumn in range(m):
            if f == 1:
                neighbour = countNeighbour(row, coloumn)
            elif f == 2:
                neighbour = countNeighbourPB(row, coloumn)

            if board[row][coloumn] == 0:
                if neighbour == 3:
                    newBoard[row][coloumn] = 1

            else:
                if neighbour == 2 or neighbour == 3:
                    newBoard[row][coloumn] = 1

    return newBoard


width = height = 800
dimensions = n
sq_size = height / dimensions
maxFPS = 60


def drawBoard(screen):
    colors = [pyg.Color("black"), pyg.Color("white")]

    for i in range(n):  # rows
        for j in range(m):  # columns

            pyg.draw.rect(screen, colors[int(board[i][j])], pyg.Rect(
                j * sq_size, i * sq_size, sq_size, sq_size))


pyg.init()
screen = pyg.display.set_mode((width, height))
screen.fill(pyg.Color("white"))
running = True

'''
mode = 1: without periodic boundary
mode = 2: with periodic boundary
'''

mode = 2

while running:
    for i in pyg.event.get():
        if i.type == pyg.QUIT:  # keyboard clicks
            running = False

    board = nextBoard(mode)
    drawBoard(screen)
    pyg.display.flip()
