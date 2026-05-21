from turtle import Turtle,Screen
import time
class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(50,70)
        self.pendown()
    def display_game(self):
        self.write("مرحبا إلي لعبة \n   Ping Pong\n\nيمكنك اللعب عن طريق \n  🔼 🔽 'w' 's'",font=("courier",30,"normal"),align="center")
    def game_over(self,r_score,b_score,screen):
            time.sleep(1)
            screen.clear()
            self.goto(0,100)
            screen.bgcolor("yellow")
            self.color("black")
            self.write("Game👊✌🤟Over",font=("arial",40,"normal"),align="center")
            self.penup()
            self.goto(50,50)
            self.pendown()
            if r_score>b_score:
                self.color("red")
                self.write("\nاللاعب الأحمر يفوز            ",font=("arial",30,"normal"),align="center")
            else:
                self.color("blue")
                self.write("\nاللاعب الأرزق يفوز            ",font=("arial",30,"normal"),align="center")
            time.sleep(2)
    def game_continue(self,screen):    
        no_yes= screen.textinput("هل تريدان تلعب مرةإخري","نعم ام لا")
        if no_yes.lower() in ("n","no","لا"):
            game_on="no"
        else:
            game_on="yes"
        time.sleep(2)
        screen.clear()
        return game_on
            

