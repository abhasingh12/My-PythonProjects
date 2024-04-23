from turtle import Turtle
#import random

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", align = "center",font = ("Courier",10,"normal") )

        self.update()



    def update(self):
        self.score +=1
        if self.score>0:
            self.clear()
            self.write(f"Score: {self.score}", align = "center",font = ("Courier",10,"normal") )

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center",font = ("Courier",10,"normal") )



