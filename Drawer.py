import turtle

class Drawer:
    width = 0
    height = 0

    def __init__(self, scrnWidth=800, scrnHeight=600, bckgColour="black", pensize=5, speed="fastest"):
        self.screen = turtle.Screen()
        self.screen.setup(scrnWidth, scrnHeight)
        self.screen.bgcolor(bckgColour) 
        turtle.tracer(0)

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.pensize(pensize)
        self.t.speed(speed)
        self.t.penup()
        self.width = scrnWidth
        self.height = scrnHeight
    def update(self):
        turtle.update()

    def clearScreen(self):
        turtle.update()
        self.t.reset()
        self.t.hideturtle()
        self.t.penup()
        self.t.pensize(5)
        self.t.speed("fastest")


    # ---------- Shapes ----------
    def Square(self, x, y, size, colour):
        self.t.goto(x, y)
        self.t.color(colour)
        self.t.fillcolor(colour)
        self.t.begin_fill()
        self.t.pendown()

        for _ in range(4):
            self.t.forward(size)
            self.t.right(90)

        self.t.end_fill()
        self.t.penup()

    def Rect(self, x, y, h, w, colour):
        self.t.goto(x, y)
        self.t.color(colour)
        self.t.fillcolor(colour)
        self.t.begin_fill()
        self.t.pendown()

        for i in range(4):
            self.t.forward(w if i % 2 == 0 else h)
            self.t.right(90)

        self.t.end_fill()
        self.t.penup()

    def Circle(self, x, y, size, colour):
        self.t.color(colour)
        self.t.fillcolor(colour)
        self.t.goto(x - size, y - size)
        self.t.begin_fill()
        self.t.pendown()
        self.t.circle(size / 2)
        self.t.end_fill()
        self.t.penup()

    def Text(self, x, y, size, font, style, colour, text):
        self.t.goto(x, y)
        self.t.color(colour)
        style = (font, size, style)
        self.t.pendown()
        self.t.write(text, font=style, align="center")
        self.t.penup()

    def Triangle(self, x, y, size, colour):
        self.t.goto(x + (x * 1.5), y)
        self.t.color(colour)
        self.t.fillcolor(colour)
        self.t.begin_fill()
        self.t.pendown()

        for _ in range(3):
            self.t.forward(size)
            self.t.left(120)

        self.t.end_fill()
        self.t.penup()
