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
ball_starting_angle = random.randint(-1,1)

if ball_starting_angle == 0:
        ball_starting_angle = -1

def drawBall():
    global ball_x
    global ball_y
    global ball_starting_angle
    drawer.Circle(ball_x, ball_y, ball_size, "white")
    ball_x = ball_x + 1
    ball_y = ball_y + ball_starting_angle
    


def drawPlayer():
    drawer.Rect(player_x, player_y, player_height, player_width, "purple")

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
