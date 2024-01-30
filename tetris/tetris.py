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

## Relevant Functions
# Draw the background grid
def drawBackgroundGrid():
    for i in range(0, game_width, int(block_size)):
        x0, y0 = i, 0
        x1, y1 = (x0 + block_size), game_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="", outline="#FFFFFF")
    
    for j in range(0, game_height, int(block_size)):
        x0, y0 = 0, j
        x1, y1 = game_width, y0 + block_size
        canvas.create_rectangle(x0, y0, x1, y1, fill="", outline="#FFFFFF")

def randomTetriminos():
    return choice(tetriminos_type)

## Create objects
class Tetrimino:
    def __init__(self, xpos, ypos, type):
        self.xpos = xpos
        self.ypos = ypos
        self.type = type
        self.squares = []
        self.points = []
        
        self.setColor()
        self.createBody()

        for i in range(4):
            self.squares.append(Block(self.points[i][0], self.points[i][1], self.color))
    
    def createBody(self):
        if(self.type == "I"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([self.xpos, (self.ypos + block_size)])
            self.points.append([self.xpos, (self.ypos + 2 * block_size)])
            self.points.append([self.xpos, (self.ypos + 3 * block_size)])
            
        elif(self.type == "O"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([self.xpos, (self.ypos + block_size)])
            self.points.append([(self.xpos + block_size), self.ypos])
            self.points.append([(self.xpos + block_size), (self.ypos + block_size)])
        
        elif(self.type == "L"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([self.xpos, (self.ypos + block_size)])
            self.points.append([self.xpos, (self.ypos + 2 * block_size)])
            self.points.append([(self.xpos + block_size), (self.ypos + 2 * block_size)])

        elif(self.type == "T"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([self.xpos, (self.ypos + block_size)])
            self.points.append([(self.xpos - block_size), (self.ypos + block_size)])
            self.points.append([(self.xpos + block_size), (self.ypos + block_size)])
        
        elif(self.type == "Z"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([(self.xpos + block_size), self.ypos])
            self.points.append([(self.xpos + block_size), (self.ypos + block_size)])
            self.points.append([(self.xpos + 2 * block_size), (self.ypos + block_size)])
        
        elif(self.type == "S"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([(self.xpos + block_size), self.ypos])
            self.points.append([(self.xpos), (self.ypos + block_size)])
            self.points.append([(self.xpos - block_size), (self.ypos + block_size)])
        
        elif(self.type == "J"):
            self.points.append([self.xpos, self.ypos])
            self.points.append([self.xpos, (self.ypos + block_size)])
            self.points.append([self.xpos, (self.ypos + 2 * block_size)])
            self.points.append([(self.xpos - block_size), (self.ypos + 2 * block_size)])
    
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
class Block:
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.block_body = canvas.create_rectangle(self.xpos, self.ypos, self.xpos + block_size, self.ypos + block_size, fill=self.color, outline="white", width=1)
    
## Set up GUI -- create window and canvas on top
window.title("Tetris")
window.geometry(str(game_width)+"x"+str(game_height))
window.configure(bg="#FFFFFF")
canvas = Canvas(window, width=game_width, height=game_height, background=game_bg, highlightthickness=0)
canvas.pack()

## Draw Background
drawBackgroundGrid()

## Run game
tetro = Tetrimino(block_size, block_size, randomTetriminos())

# Starts loop and event listener
window.mainloop()
