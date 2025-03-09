from turtle import Turtle, Screen
from random import randint

from game import Game
from settings import settings

class Food(Turtle, Game):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food_taken = 0
        self.food_coordinates = []
        self.food_spawn()

    def food_spawn(self):
        width = settings["screen_width"] - 40
        height = settings["screen_height"] - 40

        food_x = randint(-int(width / 2), int(width / 2))
        food_y = randint(-int(height / 2), int(height / 2))

        self.goto(food_x, food_y)
        print(f"Food position: {self.position()}")
