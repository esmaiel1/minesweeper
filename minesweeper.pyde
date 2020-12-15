import random

gridWidth = 380
gridHeight = 380
cellH = 20
cellW = 20
rows = 16
columns = 16
mineNum = 30

startX = 30
endX = startX + (rows * cellW)
startY = 30
endY = startY + (columns * cellH)

cells = []
mines = []
checkedCells = []



def setup():
    size(gridWidth, gridHeight)
    background(255)
    
# creates a grid and adds the cordinations of every cell as a tuble in the array "cells"
    CreateGrid()
            
# creates the mines and adds the indexes of every mine in the array "mines"
    AddMines()
        
    
def draw():
    pass
    
    
def mousePressed():
# i = (W,H) 
    for i in cells:
        if mouseX>=i[0] and mouseX<i[0]+cellW and mouseY>=i[1] and mouseY<i[1]+cellH:
            ShowSurroundings(i)


def CreateGrid():
    fill(209)
    for i in range (startX,endX,cellW):
        for j in range (startY,endY,cellH):
            rect(i,j,cellW,cellH)
            cells.append((i,j))  


def AddMines():
    for i in range(0,mineNum):
        while True:
            mineIndex = random.randint(0,len(cells))
            if not (mineIndex in mines):
                mines.append(mineIndex)
                break     


def ShowSurroundings(i):
    minesAround = 0
    surroundings = Surroundings(i)

# changes the color of the cells whenever it is clicked (white if it is a normal cell - red if it is a mine)         
    if cells.index(i) in mines:
        fill(255,0,0)
    else:
        for j in surroundings:
            if j in mines:
                minesAround+= 1

        if minesAround == 0:
            for j in surroundings: 
                if not j in checkedCells:
                    checkedCells.append(j)
                    ShowSurroundings(cells[j])    
        fill(255)
    rect(i[0],i[1],cellW,cellH)
    
# adds text in the clicked cell
    if minesAround != 0:
        CellText(i,minesAround)  
        
# returns an array that contains the indexes of the the surrounding cells 
def Surroundings(i):
    if i[0] == startX and i[1] == startY:
        return [ cells.index(i)+1,cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1])]
    elif i[0] == startX and i[1] == endY - cellH:
        return [cells.index(i)-1, cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns])]
    elif i[0] == endX - cellW and i[1] == startY:
        return [ cells.index(i)+1,cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
    elif i[0] == endX - cellW and i[1] ==  endY - cellH:
        return [cells.index(i)-1, cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns])]
    elif i[0] == startX:
        return [cells.index(i)-1, cells.index(i)+1,cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1])]
    elif i[0] == endX - cellW:
        return [cells.index(i)-1, cells.index(i)+1, cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
    elif i[1] == startY:
        return [cells.index(i)+1,
                cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1]),
                cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
    elif i[1] ==  endY - cellH:
        return [cells.index(i)-1,
                cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),
                cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns])]
    else :
        return [cells.index(i)-1, cells.index(i)+1,
                cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1]),
                cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]    


def CellText(i,minesAround):
        fill(0)
        textAlign(CENTER)
        text(str(minesAround),i[0],i[1],cellW,cellH)    





            
        
        
