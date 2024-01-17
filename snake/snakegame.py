from tkinter import *

window = Tk()

# Relevant variables
game_height = game_width = 600
snake_height = snake_width = food_height = food_width = snake_speed = game_height / 30
snake_xpos = snake_ypos = 0
chain_length = 1
snake_color = "#000000"
snake_array = []
game_speed = 300

# Set up GUI -- create window and canvas on top
def gui_setup(w):
    w.title("Snake Game")
    w.geometry(str(game_width)+"x"+str(game_height))
    w.configure(bg="#ffffff")

# Create snake object
class Snake:
    def __init__(self, canvas, xpos, ypos, chain_length):
        self.canvas = canvas
        self.xpos = xpos
        self.ypos = ypos
        self.xmove = 0
        self.ymove = 0
        self.chain_length = chain_length

        self.canvas.bind("w", self.snakePositiveY)
        self.canvas.bind("a", self.snakeNegativeX)
        self.canvas.bind("s", self.snakeNegativeY)
        self.canvas.bind("d", self.snakePositiveX)

        self.createSnake()
        self.canvas.focus_set()

    def createSnake(self):
        self.snake_link = self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos + snake_width, self.ypos + snake_height, fill=snake_color)

    def snakePositiveX(self, event):
        self.xmove = snake_speed
        self.ymove = 0
    
    def snakePositiveY(self, event):
        self.xmove = 0
        self.ymove = -snake_speed

    def snakeNegativeX(self, event):
        self.xmove = -snake_speed
        self.ymove = 0
        
    def snakeNegativeY(self, event):
        self.xmove = 0
        self.ymove = snake_speed
    
    def moveSnake(self):
        self.canvas.move(self.snake_link, self.xmove, self.ymove)
        self.canvas.after(game_speed, self.moveSnake)

gui_setup(window)
canvas = Canvas(window, width=game_width, height=game_height)
canvas.pack()

# Game functionality
snake_array.append(Snake(canvas, snake_xpos, snake_ypos, chain_length))
snake_array[0].moveSnake()

# Starts loop and event listener
window.mainloop()
