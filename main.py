from Drawer import Drawer
import turtle
import random

# Create screen and Drawer
win = turtle.Screen()
drawer = Drawer(bckgColour="black", scrnWidth=1280, scrnHeight=720)

# Object size
player_width = 25
player_height = 180

ball_size = 25

# Position Data
player_x = (drawer.width /2) - (player_width + 25)
player_y = 0
ball_x = drawer.width / 4
ball_y = 0

ballDirX = 0.1
ballDirY = random.randint(-1,1)
if ballDirY == 0:
        ballDirY = -1

def drawBall():
    global ball_x
    global ball_y
    global ballDirY
    global ballDirX
    drawer.Circle(ball_x, ball_y, ball_size, "white")
    ball_x = ball_x + ballDirX
    ball_y = ball_y + ballDirY
    
def drawPlayer():
    drawer.Rect(player_x, player_y, player_height, player_width, "purple")


def ballTouchPlayer():
     global ball_x
     global ball_y
     global player_y
     global player_x
     global ballDirX
     if ball_x >= player_x and (ball_y <= player_y) and ball_y >= player_y - player_height:
        ballDirX *= -1
          
def move_left():
    global player_y
    player_y -= 30

def move_right():
    global player_y
    player_y += 30


# BIND KEYS
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
while True:
    drawer.clearScreen()
    drawBall()
    drawPlayer()
    ballTouchPlayer()
