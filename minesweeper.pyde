import random
# The values of these variables can be changed if wanted 
grid_width = 380
grid_height = 380
cell_width = 20s
cell_height = 20
rows = 16
columns = 16
mine_count = 40
#########

startX = 30
endX = startX + (rows * cell_width)
startY = 30
endY = startY + (columns * cell_height)

cells = []
mines = []
visible_cells = []
numbers = []

game_over = False

def setup():
    size(grid_width, grid_height)
    background(255)

    createGrid()
    addMines()
    countMines()
            
    
def draw():
    pass
    
def mousePressed():
# i = (X,Y) 
    if game_over == False:
        for i in cells:
            if mouseX>=i[0] and mouseX<i[0]+cell_width and mouseY>=i[1] and mouseY<i[1]+cell_height:
                reveal(i)


# creates a grid and adds the cordinations of every cell as a tuble in the array "cells"
def createGrid():
    fill(209)
    for i in range (startX,endX,cell_width):
        for j in range (startY,endY,cell_height):
            rect(i,j,cell_width,cell_height)
            cells.append((i,j))  

# creates the mines and adds the indexes of every mine in the array "mines"
def addMines():
    counter = 0
    while counter < mine_count:
        mine_index = random.randint(0,len(cells))
        if mine_index not in mines:
                mines.append(mine_index)
                counter = counter + 1
            
# counts the number of mines around every cell and add that number in the array "numbers"
def countMines():
    for i in cells:
        count = 0
        if cells.index(i) not in mines:
            surroundings = getSurroundingCells(i)
            for j in surroundings:
                if j in mines:
                    count+= 1
        numbers.append(count)
        
        
# Reveals the cell depending on which conditon is true           
def reveal(cell):
    # i = (X,Y) 
    # True if the clicked cell is a mine
    if isABomb(cell):
        revealBomb(cell)
        endGame()
    # True if the clicked cell doesn't contain a mine and isn't a white space (mines(s) around)
    elif isANumber(cell):
        if not(isVisible(cell)):
            addToVisiblecells(cell)
            revealNumber(cell)
        
    # True if the clicked cell is a white space
    else:
        if not(isVisible(cell)):
            revealWhiteSpace(cell)
        surroundings = getSurroundingCells(cell)
        for surrounding_cell in surroundings:
            if not(isVisible(surrounding_cell)):
                addToVisiblecells(surrounding_cell)
                reveal(cells[surrounding_cell]) 
 
   
                          
# returns an array that contains the indexes of the the surrounding cells 
def getSurroundingCells(i):
    # i = (X,Y) 
    if i[0] == startX and i[1] == startY:
        return [ cells.index(i)+1,cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1])]
    elif i[0] == startX and i[1] == endY - cell_height:
        return [cells.index(i)-1, cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns])]
    elif i[0] == endX - cell_width and i[1] == startY:
        return [ cells.index(i)+1,cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
    elif i[0] == endX - cell_width and i[1] ==  endY - cell_height:
        return [cells.index(i)-1, cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns])]
    elif i[0] == startX:
        return [cells.index(i)-1, cells.index(i)+1,cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1])]
    elif i[0] == endX - cell_width:
        return [cells.index(i)-1, cells.index(i)+1, cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
    elif i[1] == startY:
        return [cells.index(i)+1,
                cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1]),
                cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]
    elif i[1] ==  endY - cell_height:
        return [cells.index(i)-1,
                cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),
                cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns])]
    else :
        return [cells.index(i)-1, cells.index(i)+1,
                cells.index(cells[cells.index(i) + columns - 1]),cells.index(cells[cells.index(i) + columns]),cells.index(cells[cells.index(i) + columns + 1]),
                cells.index(cells[cells.index(i) - columns - 1]),cells.index(cells[cells.index(i) - columns]),cells.index(cells[cells.index(i) - columns + 1])]    


# adds the count of mines around as text in the cell
def minesAround(i,count):
    # i = (X,Y) 
    fill(0)
    textAlign(CENTER)
    text(str(count),i[0],i[1],cell_width,cell_height)    

# Ends the game 
def endGame():
    global game_over
    game_over = True
    text('Game Over',endX/2,endY+cell_height)

# reveal a cell and fills it with the color red
def revealBomb(i):
    fill(255,0,0)
    rect(i[0],i[1],cell_width,cell_height)

# reveal a cell and fills it with the color white then displays a number inside of it
def revealNumber(i):
    fill(255)
    rect(i[0],i[1],cell_width,cell_height)
    minesAround(i,numbers[cells.index(i)])

# returns true if the given cell is a mine    
def isABomb(i):
    return cells.index(i) in mines

# returns true if the given cell contains a number  
def isANumber(i):
    return numbers[cells.index(i)] != 0

# returns true if the given cell has already been revealed   
def isVisible(cell):
    return cell in visible_cells

# reveal a cell and fills it with the color white
def revealWhiteSpace(i):
    fill(255)   
    rect(i[0],i[1],cell_width,cell_height)


def addToVisiblecells(i):
    visible_cells.append(i)

    

            
        
        
