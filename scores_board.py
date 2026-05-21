from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.penup()
    def update_score(self):
        self.write(self.score,font=("courier",35,"normal"),align="center")
    def acrease_score(self):
        self.clear()
        self.score+=1
        self.update_score()
        