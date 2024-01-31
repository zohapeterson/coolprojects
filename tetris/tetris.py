from tkinter import *
from random import *

## Relevant variables
window = Tk()
game_height, game_width = 500, 250
game_bg = "#000000"
block_size = block_speed = game_width / 10
score = 0
tetriminos = []
backgroundBlocks = []
tetriminos_type = ["I", "J", "S", "Z", "L", "O", "T"]
game_speed = 500

## Relevant Functions
# Draw the background grid
def drawBackgroundGrid():
    for i in range(0, game_width, int(block_size)):
        for j in range(0, game_height, int(block_size)):
            backgroundBlocks.append(BackgroundBlock(i, j))

def randomTetriminos():
    return choice(tetriminos_type)

def randomOrientation():
    return randint(0, 3)

def checkBreak():
    row_num = 0
    occupied = [0] * 20
    for a in range(0, game_height, int(block_size)):
        for b in range(0, game_width, int(block_size)):    
            for i in range(0, len(tetriminos)):
                for j in range(0, len(tetriminos[i].points)):
                    if(tetriminos[i].points[j][0] == b and tetriminos[i].points[j][1] == a and tetriminos[i].active == 0):
                        # print("Hello")
                        # print(a)
                        occupied[row_num] += 1
        row_num += 1
    
    for i in range(0, len(occupied)):
        if(occupied[i] == 10):
            # print("Row " + str(i) + " needs to be cleared.")
            pass

    occupied = [0] * 20
        
def main():
    checkBreak()
    activeTetrimino = tetriminos[len(tetriminos) - 1]
    if(activeTetrimino.checkBottom()):
        tetriminos.append(Tetrimino(block_size, block_size, randomTetriminos(), randomOrientation()))
        activeTetrimino = tetriminos[len(tetriminos) - 1]

    canvas.bind("<Up>", activeTetrimino.rotate)
    canvas.bind("<Left>", activeTetrimino.set_leftMove)
    canvas.bind("<Right>", activeTetrimino.set_rightMove)
    canvas.focus_set()

    activeTetrimino.ypos += block_speed

    for i in range(len(activeTetrimino.squares)):
        canvas.move(activeTetrimino.squares[i].block_body, 0, block_speed)
        activeTetrimino.points[i][1] += block_speed

    canvas.after(game_speed, main)

## Create objects
class Tetrimino:
    def __init__(self, xpos, ypos, type, orientation):
        self.xpos = xpos
        self.ypos = ypos
        self.xmove = 0
        self.type = type
        self.active = 1
        self.orientation = orientation
        self.move = 0
        self.squares = []
        self.points = []

        self.setColor()
        self.createBody()
    
    def setColor(self):
        if(self.type == "I"):
            self.color = "red"

        elif(self.type == "J"):
            self.color = "blue"

        elif(self.type == "S"):
            self.color = "yellow"

        elif(self.type == "Z"):
            self.color = "orange"

        elif(self.type == "T"):
            self.color = "green"

        elif(self.type == "L"):
            self.color = "purple"

        elif(self.type == "O"):
            self.color = "pink"

    def createBody(self):
        x0, y0 = self.xpos, self.ypos

        if(self.type == "I"):
            if(self.orientation == 0):
                x1, y1 = self.xpos, (self.ypos + block_size)
                x2, y2 = self.xpos, (self.ypos - block_size)
                x3, y3 = self.xpos, (self.ypos + 2 * block_size)
            elif(self.orientation == 1):
                x1, y1 = (self.xpos - block_size), self.ypos
                x2, y2 = (self.xpos - 2 * block_size), self.ypos
                x3, y3 = (self.xpos + block_size), self.ypos
            elif(self.orientation == 2):
                x1, y1 = self.xpos, (self.ypos - block_size)
                x2, y2 = self.xpos, (self.ypos - 2 * block_size)
                x3, y3 = self.xpos, (self.ypos + block_size)
            elif(self.orientation == 3):
                x1, y1 = (self.xpos + block_size), self.ypos
                x2, y2 = (self.xpos + 2 * block_size), self.ypos
                x3, y3 = (self.xpos - block_size), self.ypos
            
        elif(self.type == "O"):
            if(self.orientation == 0 or self.orientation == 1 or self.orientation == 2 or self.orientation == 3):
                x1, y1 = self.xpos, (self.ypos + block_size)
                x2, y2 = (self.xpos + block_size), self.ypos
                x3, y3 = (self.xpos + block_size), (self.ypos + block_size)
        
        elif(self.type == "L"):
            if(self.orientation == 0):
                x1, y1 = self.xpos, (self.ypos + block_size)
                x2, y2 = self.xpos, (self.ypos - block_size)
                x3, y3 = (self.xpos + block_size), (self.ypos + block_size)
            elif(self.orientation == 1):
                x1, y1 = (self.xpos - block_size), (self.ypos)
                x2, y2 = (self.xpos + block_size), (self.ypos)
                x3, y3 = (self.xpos - block_size), (self.ypos + block_size)
            elif(self.orientation == 2):
                x1, y1 = self.xpos, (self.ypos - block_size)
                x2, y2 = self.xpos, (self.ypos + block_size)
                x3, y3 = (self.xpos - block_size), (self.ypos - block_size)
            elif(self.orientation == 3):
                x1, y1 = (self.xpos + block_size), (self.ypos)
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos + block_size), (self.ypos - block_size)

        elif(self.type == "T"):
            if(self.orientation == 0):
                x1, y1 = self.xpos, (self.ypos + block_size)
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos + block_size), (self.ypos)
            elif(self.orientation == 1):
                x1, y1 = self.xpos, (self.ypos - block_size)
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos), (self.ypos + block_size)
            elif(self.orientation == 2):
                x1, y1 = self.xpos, (self.ypos - block_size)
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos + block_size), (self.ypos)
            elif(self.orientation == 3):
                x1, y1 = self.xpos, (self.ypos + block_size)
                x2, y2 = (self.xpos + block_size), (self.ypos)
                x3, y3 = (self.xpos), (self.ypos - block_size)
        
        elif(self.type == "Z"):
            if(self.orientation == 0):
                x1, y1 = (self.xpos + block_size), self.ypos
                x2, y2 = (self.xpos), (self.ypos - block_size)
                x3, y3 = (self.xpos - block_size), (self.ypos - block_size)
            elif(self.orientation == 1):
                x1, y1 = (self.xpos), (self.ypos - block_size)
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos - block_size), (self.ypos + block_size)
            elif(self.orientation == 2):
                x1, y1 = (self.xpos - block_size), (self.ypos)
                x2, y2 = (self.xpos + block_size), (self.ypos + block_size)
                x3, y3 = (self.xpos), (self.ypos + block_size)
            elif(self.orientation == 3):
                x1, y1 = (self.xpos + block_size), (self.ypos)
                x2, y2 = (self.xpos + block_size), (self.ypos - block_size)
                x3, y3 = (self.xpos), (self.ypos + block_size)
        
        elif(self.type == "S"):
            if(self.orientation == 0):
                x1, y1 = (self.xpos), self.ypos + block_size
                x2, y2 = (self.xpos + block_size), (self.ypos + block_size)
                x3, y3 = (self.xpos - block_size), (self.ypos)
            elif(self.orientation == 1):
                x1, y1 = (self.xpos), self.ypos - block_size
                x2, y2 = (self.xpos + block_size), (self.ypos)
                x3, y3 = (self.xpos + block_size), (self.ypos + block_size)
            elif(self.orientation == 2):
                x1, y1 = (self.xpos + block_size), self.ypos
                x2, y2 = (self.xpos), (self.ypos + block_size)
                x3, y3 = (self.xpos - block_size), (self.ypos + block_size)
            elif(self.orientation == 3):
                x1, y1 = (self.xpos - block_size), self.ypos
                x2, y2 = (self.xpos - block_size), (self.ypos - block_size)
                x3, y3 = (self.xpos), (self.ypos + block_size)
        
        elif(self.type == "J"):
            if(self.orientation == 0):
                x1, y1 = self.xpos, (self.ypos + block_size)
                x2, y2 = self.xpos, (self.ypos - block_size)
                x3, y3 = (self.xpos - block_size), (self.ypos + block_size)
            elif(self.orientation == 1):
                x1, y1 = self.xpos - block_size, (self.ypos)
                x2, y2 = self.xpos + block_size, (self.ypos)
                x3, y3 = (self.xpos - block_size), (self.ypos - block_size)
            elif(self.orientation == 2):
                x1, y1 = self.xpos, (self.ypos - block_size)
                x2, y2 = self.xpos, (self.ypos + block_size)
                x3, y3 = (self.xpos + block_size), (self.ypos - block_size)
            elif(self.orientation == 3):
                x1, y1 = self.xpos - block_size, (self.ypos)
                x2, y2 = self.xpos + block_size, (self.ypos)
                x3, y3 = (self.xpos + block_size), (self.ypos + block_size)

        self.points.append([x0, y0])
        self.points.append([x1, y1])
        self.points.append([x2, y2])
        self.points.append([x3, y3])
        
        if(self.move == 0):
            self.move = 1
            for i in range(len(self.points)):
                self.squares.append(Block(self.points[i][0], self.points[i][1], self.color))
        else:
            for i in range(len(self.points)):
                self.squares[i].moveBlock(self.points[i][0], self.points[i][1])
    
    def rotate(self, event):
        for i in range(0, len(self.points)):
            self.points.pop()

        if(self.orientation < 3):
            self.orientation += 1
        else:
            self.orientation = 0

        self.createBody()
    
    def set_rightMove(self, event):
        if(self.checkSideways("right")):
            self.xmove = block_speed
            self.xpos += self.xmove
            for i in range(0, len(self.points)):
                self.points[i][0] += self.xmove

            self.move_sideways()

    def set_leftMove(self, event):
        if(self.checkSideways("left")):
            self.xmove = -block_speed
            self.xpos += self.xmove
            for i in range(0, len(self.points)):
                self.points[i][0] += self.xmove

            self.move_sideways()
    
    def move_sideways(self):
        for i in range(len(self.points)):
            canvas.move(self.squares[i].block_body, self.xmove, 0)

    def checkSideways(self, dir):
        if(dir == "right"):
            for i in range(0, len(self.points)):
                if((self.points[i][0] + block_size) >= game_width):
                    return False
                for k in range(0, (len(tetriminos) - 1)):
                    for j in range(0, (len(tetriminos[k].points))):
                        if((self.points[i][0] + block_size) == tetriminos[k].points[j][0]):
                            if((self.points[i][1]) == tetriminos[k].points[j][1]):   
                                return False
            return True
        
        elif(dir == "left"):
            for i in range(0, len(self.points)):
                if((self.points[i][0]) <= 0):
                    return False
                for k in range(0, (len(tetriminos) - 1)):
                    for j in range(0, (len(tetriminos[k].points))):
                        if((self.points[i][0]) == (tetriminos[k].points[j][0] + block_size)):
                            if((self.points[i][1]) == tetriminos[k].points[j][1]):   
                                return False
            return True
    
    def checkBottom(self):
        for i in range(0, len(self.points)):
            if((self.points[i][1] + block_size) >= game_height):
                self.active = 0
                return True
        
            if(len(tetriminos) > 1):
                for k in range(0, (len(tetriminos) - 1)):
                    for j in range(0, (len(tetriminos[k].points))):
                        if((self.points[i][1] + block_size) == tetriminos[k].points[j][1]):
                            if(self.points[i][0] == tetriminos[k].points[j][0]):
                                self.active = 0
                                return True
        return False
class Block:
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.block_body = canvas.create_rectangle(self.xpos, self.ypos, self.xpos + block_size, self.ypos + block_size, fill=self.color, outline="white", width=1)  

    def moveBlock(self, newXpos, newYpos):
        self.xpos, self.ypos = newXpos, newYpos
        canvas.coords(self.block_body, self.xpos, self.ypos, self.xpos + block_size, self.ypos + block_size)
class BackgroundBlock:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.bg_blockBody = canvas.create_rectangle(self.xpos, self.ypos, self.xpos + block_size, self.ypos + block_size, fill="", outline="#FFFFFF")

## Set up GUI -- create window and canvas on top
window.title("Tetris")
window.geometry(str(game_width)+"x"+str(game_height))
window.configure(bg="#FFFFFF")
canvas = Canvas(window, width=game_width, height=game_height, background=game_bg, highlightthickness=1)
canvas.pack()

## Draw Background
drawBackgroundGrid()

## Run game
# tetriminos.append(Tetrimino(3*block_size, block_size, "Z", 0))
tetriminos.append(Tetrimino(3*block_size, block_size, randomTetriminos(), randomOrientation()))
main()

# Starts loop and event listener
window.mainloop()
