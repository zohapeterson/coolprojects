from tkinter import *
from random import *

## Relevant variables
window = Tk()
game_height, game_width = 600, 400
game_bg = "#000000"
block_size = game_width / 10
score = 0
blocks = []

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

## Create types of objects
class I_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.type = "I"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (self.xpos + block_size), (self.ypos + 4 * block_size)
        return canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="white", width=1)

class J_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.type = "J"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (self.xpos + block_size), (self.ypos)
        x2, y2 = (self.xpos + block_size), (self.ypos + 3 * block_size)
        x3, y3 = (self.xpos - block_size), (self.ypos + 3 * block_size)
        x4, y4 = (self.xpos - block_size), (self.ypos + 2 * block_size)
        x5, y5 = (self.xpos), (self.ypos + 2 * block_size)
        return canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, fill="blue", outline="white", width=1)

class L_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.type = "L"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (self.xpos + block_size), (self.ypos)
        x2, y2 = (self.xpos + block_size), (self.ypos + 2 * block_size)
        x3, y3 = (self.xpos + 2 * block_size), (self.ypos + 2 * block_size)
        x4, y4 = (self.xpos + 2 * block_size), (self.ypos + 3 * block_size)
        x5, y5 = (self.xpos), (self.ypos + 3 * block_size)
        return canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, fill="indigo", outline="white", width=1)

class O_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.ID = "O"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (x0 + 2 * block_size), (y0 + 2 * block_size)
        return canvas.create_rectangle(x0, y0, x1, y1, fill="purple", outline="white", width=1)

class S_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.type = "S"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (self.xpos + 2 * block_size), (self.ypos)
        x2, y2 = (self.xpos + 2 * block_size), (self.ypos + block_size)
        x3, y3 = (self.xpos + block_size), (self.ypos + block_size)
        x4, y4 = (self.xpos + block_size), (self.ypos + 2 * block_size)
        x5, y5 = (self.xpos - block_size), (self.ypos + 2 * block_size)
        x6, y6 = (self.xpos - block_size), (self.ypos + block_size)
        x7, y7 = (self.xpos), (self.ypos + block_size)
        return canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, fill="pink", outline="white", width=1)

class T_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.type = "T"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (self.xpos + block_size), (self.ypos)
        x2, y2 = (self.xpos + block_size), (self.ypos + block_size)
        x3, y3 = (self.xpos + 2 * block_size), (self.ypos + block_size)
        x4, y4 = (self.xpos + 2 * block_size), (self.ypos + 2 * block_size)
        x5, y5 = (self.xpos - block_size), (self.ypos + 2 * block_size)
        x6, y6 = (self.xpos - block_size), (self.ypos + block_size)
        x7, y7 = (self.xpos), (self.ypos + block_size)
        return canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, fill="yellow", outline="white", width=1)

class Z_shape:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.type = "Z"
        self.body = self.createBody()
        
    def createBody(self):
        x0, y0 = self.xpos, self.ypos
        x1, y1 = (self.xpos + 2 * block_size), (self.ypos)
        x2, y2 = (self.xpos + 2 * block_size), (self.ypos + block_size)
        x3, y3 = (self.xpos + 3 * block_size), (self.ypos + block_size)
        x4, y4 = (self.xpos + 3 * block_size), (self.ypos + 2 * block_size)
        x5, y5 = (self.xpos + block_size), (self.ypos + 2 * block_size)
        x6, y6 = (self.xpos + block_size), (self.ypos + block_size)
        x7, y7 = (self.xpos), (self.ypos + block_size)
        return canvas.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, fill="orange", outline="white", width=1)


## Set up GUI -- create window and canvas on top
window.title("Tetris")
window.geometry(str(game_width)+"x"+str(game_height))
window.configure(bg="#FFFFFF")
canvas = Canvas(window, width=game_width, height=game_height, background=game_bg, highlightthickness=0)
canvas.pack()

## Draw Background
drawBackgroundGrid()

## Run game

# Starts loop and event listener
window.mainloop()
