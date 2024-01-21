from tkinter import *
from random import *
from math import *

## Relevant variables
window = Tk()
game_height = game_width = 400
ball_radius = 10
paddle_height, paddle_width = 10, 30
paddle_speed = 5
paddle_yconst = 350
game_speed = 10

## Create Classes/Objects
class Ball:
    def __init__(self, xpos, ypos):
        self.score = 0
        self.ball_speed = 2
        self.xpos = xpos
        self.ypos = ypos
        self.ball = canvas.create_oval(self.xpos, self.ypos, self.xpos + ball_radius, self.ypos + ball_radius, fill="#ffffff")
        self.initTheta = choice(range(30, 150, 1))
        self.xvel = self.ball_speed * cos((self.initTheta * (pi / 180)))
        self.yvel = self.ball_speed * sin((self.initTheta * (pi / 180)))

        self.moveBall()

    def moveBall(self):
        self.checkBallPos()
        checkBallCollision(self)
        canvas.move(self.ball, self.xvel, self.yvel)
        self.xpos = self.xpos + self.xvel
        self.ypos = self.ypos + self.yvel
        canvas.after(game_speed, self.moveBall)

    def checkBallPos(self):
        if(self.ypos >= (game_height - ball_radius)):
            print("You lose. Score: " + str(self.score))
            self.xvel = self.yvel = 0
            window.quit()
        if(self.xpos > (game_width - ball_radius)):
            self.xvel = self.xvel * -1
        elif(self.xpos < 0):
            self.xvel = self.xvel * -1
        elif(self.ypos < 0):
            self.yvel = self.yvel * -1

class Paddle:
    def __init__(self, xpos, ypos, paddle_speed):
        self.xpos = xpos
        self.ypos = ypos
        self.paddle = canvas.create_rectangle(self.xpos, self.ypos, self.xpos + paddle_width, self.ypos + paddle_height, fill="#ffffff")
        self.xmove = 0
        
        canvas.bind("<Left>", self.paddleNegativeX)
        canvas.bind("<Right>", self.paddlePositiveX)
        
        canvas.focus_set()
        
    def paddlePositiveX(self, event):
        self.xmove = paddle_speed
        self.movePaddle()

    def paddleNegativeX(self, event):
        self.xmove = -paddle_speed
        self.movePaddle()
    
    def movePaddle(self):
        self.checkPaddlePos()
        canvas.move(self.paddle, self.xmove, 0)
        self.xpos = self.xpos + self.xmove
    
    def checkPaddlePos(self):
        if(((self.xpos + self.xmove) > (game_width - paddle_width)) or (self.xpos + self.xmove) < 0):
            self.xmove = 0

def checkBallCollision(game_ball):
    if (((game_ball.xpos + ball_radius / 2) >= game_paddle.xpos) and ((game_ball.xpos + ball_radius / 2) <= (game_paddle.xpos + paddle_width)) and ((game_ball.ypos + ball_radius) >= game_paddle.ypos)):
        game_ball.yvel = game_ball.yvel * -1
        game_ball.score = game_ball.score + 1

## Set up GUI
# Create window
window.title("Pong")
window.geometry(str(game_width)+"x"+str(game_height))
window.configure(background="#000000")

# Create canvas
canvas = Canvas(window, width=game_width, height=game_height, bg="#000000", highlightthickness=1)
canvas.pack()

## Gameplay
# Create Ball and Paddle
game_paddle = Paddle((game_width / 2) - (paddle_width / 2), paddle_yconst, paddle_speed)
game_ball = Ball((game_width / 2) - ball_radius, 50)

window.mainloop() # Starts loop and event listener
