from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_len=1,stretch_wid=6)
    def get_up(self):
        self.goto(self.xcor(),self.ycor()+40)
        
    def get_down(self):
        self.goto(self.xcor(),self.ycor()-40)
