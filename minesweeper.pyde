import random

X = 30
maxX = 350
Y = 30
maxY = 350
h = 20
w = 20
cells = []
mines = []

def setup():
    size(380, 380)
    background(255)
    textSize(12)

    fill(209)
    for i in range (X,maxX,w):
        for j in range (Y,maxY,h):
            rect(i,j,w,h)
            cells.append((i,j))

    for i in range(0,40):
        while True:
            mineIndex = random.randint(0,len(cells))
            if not (mineIndex in mines):
                mines.append(mineIndex)
                break
    print (len(cells))
    print (len(mines))
    mines.sort()
    print(mines)
def draw():
    pass
    
    
def mousePressed():
    for i in cells:
        if mouseX>=i[0] and mouseX<i[0]+w and mouseY>=i[1] and mouseY<i[1]+h:
            if cells.index(i) in mines:
                fill(255,0,0)
                #print(cells.index(i))
            else:
                fill(255)
                #print(cells.index(i))
            rect(i[0],i[1],w,h)
            
            fill(0)
            textAlign(i[0],i[1])
            text("1",i[0],i[1],w,h)
        
