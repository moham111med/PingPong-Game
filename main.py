from turtle import Screen
from paddle import Paddle
from square import Square
from ball import Ball
from game_display import Game
from scores_board import Score
import time
#*التجهيز
window=Screen()
window.tracer(0)
window.setup(800,600)
game=Game()
square=Square()
game_again=True
def game_ping_pong():
    game.display_game()
    window.bgcolor("green")
    time.sleep(1)
    while True:
        window.update()
        point_win=window.textinput("Ping   ^_^   Pong","كم عدد النقاط التي تريد أن تكون هدف الفوز؟")
        if point_win.isdigit(): 
           if int(point_win)>0:
             break
    window.clear()
    window.bgcolor("black")
    window.title("Ping Pong Game")
    window.tracer(0)
    right_score=Score()
    f_score=Score()
    right_score.goto(200,250)
    f_score.goto(-200,250)
    right_score.pendown()
    right_score.color("red")
    f_score.color("blue")
    f_score.pendown()
    ball=Ball()
    r_paddle=Paddle((350,0))
    f_paddle=Paddle((-350,0))
    r_paddle.color("red")
    f_paddle.color("blue")
    right_score.update_score()
    f_score.update_score()
    speed=0.05
    while True:
        if speed<=0.015:
            speed=.015
        time.sleep(speed)
        window.update()
        if right_score.score==int(point_win) or f_score.score==int(point_win):            
            game.game_over(right_score.score,f_score.score,window)
            break
        ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
        #* شرط لكي ترتد الكرة في الجانب العلوي او السفلي
        #*اكتشاف التصادم مع الجانب العلوي او السفلي
        if ball.ycor()>=280 or ball.ycor()<=-280:
            ball.y_move*=-1
        #*اكتشاف التصادم مع المضارب
        if (ball.xcor()>=330 and ball.distance(r_paddle)<=49) or (ball.xcor()<=-330 and ball.distance(f_paddle)<=49):
            ball.x_move*=-1
            speed-=0.01
            print(speed)
        #*إذا خرجت من جهة اليمين
        if ball.xcor()>405:
            ball.goto(0,0)
            ball.x_move*=-1
            time.sleep(1)
            f_score.acrease_score()
            speed=.04
        #*إذا خرجت من جهة اليسار
        if ball.xcor()<-405:
            ball.goto(0,0)
            ball.x_move*=-1
            time.sleep(1)
            right_score.acrease_score()
            speed=.04
        window.listen()
        window.onkey(r_paddle.get_up,"Up")
        window.onkey(r_paddle.get_down,"Down")
        window.onkey(f_paddle.get_up,"w")
        window.onkey(f_paddle.get_down,"s")
        square.draw_square()
    if game.game_continue(window)=="yes":
        game_ping_pong()
game_ping_pong()