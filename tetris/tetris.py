from tkinter import *
from random import *

## Relevant variables
window = Tk()
game_height, game_width = 500, 250
game_bg = "#000000"
block_size = block_speed = game_width / 10
score = 0
tetriminos = []
tetriminos_type = ["I", "J", "S", "Z", "L", "O", "T"]
game_speed = 500

## Relevant Functions
# Draw the background grid
def drawBackgroundGrid():
    for i in range(0, game_width, int(block_size)):
        for j in range(0, game_height, int(block_size)):
            BackgroundBlock(i, j)

def randomTetriminos():
    return choice(tetriminos_type)

def randomOrientation():
    return randint(0, 3)

def main():
    canvas.bind("<Up>", activeTetrimino.rotate)
    canvas.focus_set()

    activeTetrimino.ypos += block_speed

    for i in range(4):
        canvas.move(activeTetrimino.squares[i].block_body, 0, block_speed)

    canvas.after(game_speed, main)

## Create objects
class Tetrimino:
    def __init__(self, xpos, ypos, type, orientation):
        self.xpos = xpos
        self.ypos = ypos
        self.type = type
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
                x1, y1 = (self.xpos), (self.ypos + block_size)
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos - block_size), (self.ypos - block_size)
            elif(self.orientation == 2):
                x1, y1 = (self.xpos + block_size), (self.ypos)
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
                x3, y3 = (self.xpos - block_size), (self.ypos - block_size)
            elif(self.orientation == 3):
                x1, y1 = (self.xpos), self.ypos + block_size
                x2, y2 = (self.xpos - block_size), (self.ypos)
                x3, y3 = (self.xpos - block_size), (self.ypos - block_size)
        
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
            for i in range(4):
                self.squares.append(Block(self.points[i][0], self.points[i][1], self.color))
        else:
            for i in range(4):
                self.squares[i].moveBlock(self.points[i][0], self.points[i][1])
    
    def rotate(self, event):
        for i in range(0, len(self.points)):
            self.points.pop()

        if(self.orientation < 3):
            self.orientation += 1
        else:
            self.orientation = 0

        self.createBody()
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
        self.occupied = 0
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
activeTetrimino = Tetrimino(3 * block_size, 3 * block_size, "L", 0)
main()

# Starts loop and event listener
window.mainloop()
