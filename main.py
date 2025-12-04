from Drawer import Drawer
import turtle
import random

class Brick:
    
    def __init__(self, brick_id, X, Y, col):
        self.id = brick_id
        self.isHit = False
        self.brickX = X
        self.brickY = Y
        self.col =  col

    def UpdateValue(self, bool):
        self.isHit = bool

# Create screen and Drawer
win = turtle.Screen()
drawer = Drawer(bckgColour="black", scrnWidth=1280, scrnHeight=840)

# Object size
player_width = 25
player_height = 180

brickHeight = drawer.height / 10
brickWidth = brickHeight / 2

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

bricks = []
brickColours = {
    0 : "red",
    1 : "blue",
    2 : "BlueViolet",
    3 : "orange",
    4 : "green",
    5 : "SpringGreen",
    6 : "firebrick"
}

def generateBrickObjects():
    global bricks

    startX = -(drawer.width / 2) + 5
    startY = drawer.height / 2

    x = startX
    for col in range(3):
        col = random.randint(0,6)
        y = startY
        for i in range(10):
            bricks.append(Brick(i, x, y, col))
            y -= brickHeight + 10  
        x += brickWidth + 10

#Game logic
def drawBricks():
    global brickHeight, brickWidth, bricks
    for brick in bricks:
        drawer.Rect(brick.brickX, brick.brickY, brickHeight, brickWidth, brickColours[brick.col])


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


def startUp():
    generateBrickObjects()

def gameUpdate():
    drawer.clearScreen()
    drawBall()
    drawPlayer()
    ballTouchPlayer()
    ballTouchWall()
    drawBricks()


# BIND KEYS
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

generateBrickObjects()

while True:
    gameUpdate()
