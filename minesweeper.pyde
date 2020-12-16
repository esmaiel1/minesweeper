import random

grid_width = 380
grid_height = 380
cell_width = 20
cell_height = 20
rows = 16
columns = 16
mine_count = 40

startX = 30
endX = startX + (rows * cell_width)
startY = 30
endY = startY + (columns * cell_height)

cells = []
mines = []
visible_cells = []
cells_text = []

game_over = False

def setup():
    size(grid_width, grid_height)
    background(255)

    create_grid()
    add_mines()
    count_mines()
            
    
def draw():
    pass
    
def mousePressed():
# i = (X,Y) 
    if game_over == False:
        for i in cells:
            if mouseX>=i[0] and mouseX<i[0]+cell_width and mouseY>=i[1] and mouseY<i[1]+cell_height:
                reveal(i)


# creates a grid and adds the cordinations of every cell as a tuble in the array "cells"
def create_grid():
    fill(209)
    for i in range (startX,endX,cell_width):
        for j in range (startY,endY,cell_height):
            rect(i,j,cell_width,cell_height)
            cells.append((i,j))  

# creates the mines and adds the indexes of every mine in the array "mines"
def add_mines():
    counter = 0
    while counter < mine_count:
        mine_index = random.randint(0,len(cells))
        if mine_index not in mines:
                mines.append(mine_index)
                counter = counter + 1
            
# counts the number of mines around every cell and add that number in the array "cells_text"
def count_mines():
    for i in cells:
        count = 0
        if cells.index(i) not in mines:
            surroundings = surrounding_cells(i)
            for j in surroundings:
                if j in mines:
                    count+= 1
        cells_text.append(count)
        
        
# Reveals the cell depending on which conditon is true           
def reveal(i):
    # i = (X,Y) 
    global game_over
    # True if the clicked cell is a mine
    if cells.index(i) in mines:
        fill(255,0,0)
        rect(i[0],i[1],cell_width,cell_height)
        game_over = True
        text('Game Over',endX/2,endY+cell_height)
    # True if the clicked cell doesn't contain a mine and isn't a white space (mines(s) around)
    elif cells_text[cells.index(i)] != 0:
        fill(255)
        rect(i[0],i[1],cell_width,cell_height)
        mines_around(i,cells_text[cells.index(i)])
    # True if the clicked cell is a white space
    else:
        surroundings = surrounding_cells(i)
        for j in surroundings:
            if j not in visible_cells:
                visible_cells.append(j)
                reveal(cells[j]) 
        fill(255)   
        rect(i[0],i[1],cell_width,cell_height)    
   
                          
# returns an array that contains the indexes of the the surrounding cells 
def surrounding_cells(i):
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
def mines_around(i,count):
    # i = (X,Y) 
    fill(0)
    textAlign(CENTER)
    text(str(count),i[0],i[1],cell_width,cell_height)    





            
        
        
