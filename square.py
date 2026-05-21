from turtle import Turtle
class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.pensize(10)
        self.goto(400,-300)
        self.pendown()
    def draw_square(self):
       for _ in range(4): 
        self.left(90)
        self.fd(600)
        self.left(90)
        self.fd(800)
        
        