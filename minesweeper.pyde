import random

rows = 16
columns = 16
cellH = 20
cellW = 20
startX = 30
endX = startX + (rows * cellW)
startY = 30
endY = startY + (columns * cellH)
cells = []
mines = []
mineNum = 20

def setup():
    size(380, 380)
    background(255)
    
# creates a grid and adds the cordinations of every cell as a tuble in the array "cells"
    fill(209)
    for i in range (startX,endX,cellW):
        for j in range (startY,endY,cellH):
            rect(i,j,cellW,cellH)
            cells.append((i,j))
            
# creates the mines and adds the indexes of every mine in the array "mines"
    for i in range(0,mineNum):
        while True:
            mineIndex = random.randint(0,len(cells))
            if not (mineIndex in mines):
                mines.append(mineIndex)
                break 
        
    
def draw():
    pass
    
    
def mousePressed():
    
# changes the color of the cells whenever it is clicked (white if it is a normal cell - red if mine) 
    for i in cells:
        if mouseX>=i[0] and mouseX<i[0]+cellW and mouseY>=i[1] and mouseY<i[1]+cellH:
            minesAround = 0
            if cells.index(i) in mines:
                fill(255,0,0)
            else:
                fill(255)
                surroundings = [cells.index(i)-1, cells.index(i)+1,
                                 cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1]),
                                 cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
                for j in surroundings:
                    if j in mines:
                        minesAround+= 1
            rect(i[0],i[1],cellW,cellH)
            
# adds text in the clicked cell
            if not (minesAround == 0):
                fill(0)
                textAlign(CENTER)
                text(str(minesAround),i[0],i[1],cellW,cellH)
            
            
            
            
        
