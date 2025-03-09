from turtle import Turtle

from game import Game
from settings import settings

S_HEIGHT = settings["screen_height"]

class Scoreboard(Turtle, Game):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=(S_HEIGHT / 2) - (S_HEIGHT * 0.1))
        self.points = 0

    def increase_points(self, amount = 10):
        self.points += amount
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.points}", align="center" ,font=("Montserrat", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=("Montserrat", 40, "bold"))