from tkinter import *
from random import *

## Relevant variables
window = Tk()
game_height, game_width = 500, 250
game_bg = "#000000"
block_size = block_speed = game_width / 10
tetriminos = []
backgroundBlocks = []
tetriminos_type = ["I", "J", "S", "Z", "L", "O", "T"]
game_speed = 300
score = 0

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

def randomSpawn():
    return randint(2, 8) * block_size

def checkBreak():
    row_num = 0
    remove_count = 0
    occupied = [0] * 20
    for a in range(0, game_height, int(block_size)):
        for b in range(0, game_width, int(block_size)):    
            for i in range(0, len(tetriminos)):
                for j in range(0, len(tetriminos[i].points)):
                    if(tetriminos[i].points[j][0] == b and tetriminos[i].points[j][1] == a and tetriminos[i].active == 0):
                        occupied[row_num] += 1
        row_num += 1
    
    for c in range(0, len(occupied)):
        if(occupied[c] == 10):
            remove_count += 1

    for i in range(0, len(occupied)):
        if(occupied[i] == 10):
            for j in range(0, int(game_width), int(block_size)):
                for k in range(0, len(tetriminos)):
                    for l in range(0, len(tetriminos[k].points)):
                        if(tetriminos[k].points[l][0] == j and tetriminos[k].points[l][1] == (i*25)):
                            tetriminos[k].squares[l].remove = 1
    
    for k in range(0, len(tetriminos)):
        for l in range(0, len(tetriminos[k].points)):
            if(tetriminos[k].squares[l].remove == 1):
                canvas.delete(tetriminos[k].squares[l].block_body)                
    
    remove_rows = [i for i, count in enumerate(occupied) if count == 10]

    for row in remove_rows:
        for i in range(row, 0, -1):
            for j in range(0, len(tetriminos)):
                for k in range(0, len(tetriminos[j].points)):
                    if tetriminos[j].points[k][1] == (i * int(block_size)):
                        tetriminos[j].points[k][1] += int(block_size)
                        canvas.move(tetriminos[j].squares[k].block_body, 0, int(block_size))

    return remove_count
        
def checkLoss():
    for i in range(0, len(tetriminos)):
        for j in range(0, len(tetriminos[i].points)):
            if(tetriminos[i].points[j][1] <= 0 and tetriminos[i].active == 0):
                return True
    return False

def main():
    global score
    score += checkBreak()
    activeTetrimino = tetriminos[len(tetriminos) - 1]
    if(activeTetrimino.checkBottom()):
        tetriminos.append(Tetrimino(randomSpawn(), -3 * block_size, randomTetriminos(), randomOrientation()))
        activeTetrimino = tetriminos[len(tetriminos) - 1]

    canvas.bind("<Up>", activeTetrimino.rotate)
    canvas.bind("<Left>", activeTetrimino.set_leftMove)
    canvas.bind("<Right>", activeTetrimino.set_rightMove)
    canvas.focus_set()

    activeTetrimino.ypos += block_speed

    for i in range(len(activeTetrimino.squares)):
        canvas.move(activeTetrimino.squares[i].block_body, 0, block_speed)
        activeTetrimino.points[i][1] += block_speed

    after_control = canvas.after(game_speed, main)
    
    if(checkLoss()):
        canvas.after_cancel(after_control)
        print("You lose! Score: " + str(score))

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
        if(self.checkSideways("right") and self.checkSideways("left")):
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
        self.remove = 0
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
tetriminos.append(Tetrimino(randomSpawn(), -3 * block_size, randomTetriminos(), randomOrientation()))
main()

# Starts loop and event listener
window.mainloop()
