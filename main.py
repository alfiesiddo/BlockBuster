from Drawer import Drawer
import turtle
import random

class Brick:
    
    def __init__(self, brick_id, X, Y, col):
        self.id = brick_id
        self.isHit = False
        self.brickX = X
        self.brickY = Y
        self.col = col

    def UpdateValue(self):
        self.isHit = True

    def Touched(self):
        global ball_x, ball_y, ballDirX, ballDirY, brickHeight, brickWidth, ball_size

        withinX = self.brickX <= ball_x - (ball_size / 2) <= self.brickX + brickWidth
        withinY = self.brickY - brickHeight <= ball_y <= self.brickY

        if withinX and withinY and self.isHit == False:
            self.UpdateValue()
            ballDirY = (ballDirY + randY()) * -1
            ballDirX *= -1

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

ballDirX = 2
ballDirY = random.randint(-3,4)
if ballDirY == 0:
    ballDirY = random.randint(-3,4)

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
def  randY():
    num = random.choice([-2, -1, 1, 2])
    return num

def drawBricks():
    global brickHeight, brickWidth, bricks
    for brick in bricks:
        brick.Touched()
        if(brick.isHit == False):
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
        ballDirY = (ballDirY + randY()) * -1

def ballTouchWall():
    global ball_x, ball_y, ballDirX, ballDirY

    if ball_y >= drawer.height / 2 or ball_y <= -drawer.height / 2:
        ballDirY = (ballDirY + randY()) * -1
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

def second_chance():
    global ballDirY, ballDirX

    if ballDirX == 0 and ballDirY == 0:
        ballDirX = 2
        ballDirY = randY()

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
win.onkeypress(second_chance, "space")

generateBrickObjects()

while True:
    gameUpdate()
