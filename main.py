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
player_x = (drawer.width /2) - (player_width)
player_y = 0
ball_x = drawer.width / 4
ball_y = 0

ballDirX = 1
ballDirY = random.randint(-1,1)
if ballDirY == 0:
    ballDirY = -1

def drawBall():
    global ball_x, ball_y, ballDirX, ballDirY

    drawer.Circle(ball_x, ball_y, ball_size, "white")
    ball_x = ball_x + ballDirX
    ball_y = ball_y + ballDirY
    
def drawPlayer():
    drawer.Rect(player_x, player_y, player_height, player_width, "purple")
    print("Player Y: ", player_y)


def ballTouchPlayer():
     global ball_x, ball_y, player_y, player_x, ballDirY, ballDirX

     if ball_x >= player_x and (ball_y <= player_y) and ball_y >= player_y - player_height:
        ballDirX *= -1
        ballDirY *= -1

def ballTouchWall():
    global ball_x, ball_y, ballDirX, ballDirY

    if ball_y >= drawer.height / 2 or ball_y <= -drawer.height / 2:
        ballDirY *= -1
        ball_y = min(max(ball_y, -drawer.height / 2), drawer.height / 2)

    if ball_x <= -drawer.width / 2:
        ballDirX *= -1
        ball_x = -drawer.width / 2

    if ball_x >= drawer.width / 2:
        print("Ball left the right side!")
        ball_x = 0
        ball_y = 0
        ballDirY = 0
        ballDirX = 0

def move_left():
    global player_y
    player_y -= 50

def move_right():
    global player_y
    player_y += 50


def gameUpdate():
    drawer.clearScreen()
    drawBall()
    drawPlayer()
    ballTouchPlayer()
    ballTouchWall()


# BIND KEYS
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
while True:
    gameUpdate()
