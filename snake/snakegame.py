from tkinter import *

window = Tk()

# Relevant variables
game_height = game_width = 600
snake_height = snake_width = food_height = food_width = snake_speed = game_height / 30
snake_xpos = snake_ypos = game_height / 2
chain_length = 1
snake_color = "#000000"
game_speed = 300
score = 0
snake_array = []

# Set up GUI -- create window and canvas on top
def gui_setup(w):
    w.title("Snake Game")
    w.geometry(str(game_width)+"x"+str(game_height))
    w.configure(bg="#ffffff")

# Create snake object
class SnakeHead:
    def __init__(self, canvas, xpos, ypos, dir):
        self.canvas = canvas
        self.xpos = xpos
        self.ypos = ypos
        self.xmove = 0
        self.ymove = 0
        self.dir = dir
        self.snake_head = self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos + snake_width, self.ypos + snake_height, fill=snake_color)
        self.afterID = None

        self.canvas.bind("<Up>", self.snakePositiveY)
        self.canvas.bind("<Left>", self.snakeNegativeX)
        self.canvas.bind("<Down>", self.snakeNegativeY)
        self.canvas.bind("<Right>", self.snakePositiveX)
        self.moveSnake()
        
        self.canvas.focus_set()
        
    def snakePositiveX(self, event):
        if(self.dir != "Right" and self.dir != "Left"):
            self.xmove = snake_speed
            self.ymove = 0
            self.dir = "Right"
    
    def snakePositiveY(self, event):
        if(self.dir != "Up" and self.dir != "Down"):
            self.xmove = 0
            self.ymove = -snake_speed
            self.dir = "Up"

    def snakeNegativeX(self, event):
        if(self.dir != "Left" and self.dir != "Right"):
            self.xmove = -snake_speed
            self.ymove = 0
            self.dir = "Left"
        
    def snakeNegativeY(self, event):
        if(self.dir != "Down" and self.dir != "Up"):
            self.xmove = 0
            self.ymove = snake_speed
            self.dir = "Down"
    
    def checkSnakePos(self):
        if(self.xpos > game_width or self.ypos > game_height or self.xpos < 0 or self.ypos < 0):
            self.xmove = 0
            self.ymove = 0
            self.canvas.after_cancel(self.afterID)
            print("Youre score: " + str(score))
            return True
        else:
            return False

    def moveSnake(self):
        if(self.checkSnakePos() == False):
            self.canvas.move(self.snake_head, self.xmove, self.ymove)
            self.xpos = self.xpos + self.xmove
            self.ypos = self.ypos + self.ymove
            updateSnakePostion(self.xpos - self.xmove, self.ypos - self.ymove)
            self.afterID = self.canvas.after(game_speed, self.moveSnake)
        else:
            window.quit()
class SnakeBody:
    def __init__(self, canvas, xpos, ypos):
        self.canvas = canvas
        self.xpos = xpos
        self.ypos = ypos
        self.createSnakeBody()
    
    def createSnakeBody(self):
        self.snake_body = self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos + snake_width, self.ypos + snake_height, fill=snake_color)

def updateSnakePostion(pastXpos, pastYpos):
    for i in range(1, len(snake_array)):
        pastXpos_temp = snake_array[i].xpos
        pastYpos_temp = snake_array[i].ypos

        snake_array[i].xpos = pastXpos
        snake_array[i].ypos = pastYpos

        pastXpos = pastXpos_temp
        pastYpos = pastYpos_temp

        canvas.coords(snake_array[i].snake_body, snake_array[i].xpos, snake_array[i].ypos, snake_array[i].xpos + snake_width, snake_array[i].ypos + snake_height)

gui_setup(window)
canvas = Canvas(window, width=game_width, height=game_height)
canvas.pack()

snake_array.append(SnakeHead(canvas, snake_xpos, snake_ypos, "None")) # Create the snake head

window.mainloop() # Starts loop and event listener
