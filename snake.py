from turtle import Turtle, Screen

from game import Game
from settings import settings

S_HEIGHT = settings["screen_height"]
S_WIDTH = settings["screen_width"]

class Snake(Game):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.increase_size()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.body = self.segments[1:]

    def increase_size(self, coordinates=(0, 0)):  # coordinates = Last square coords.
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.setposition(coordinates)
        self.segments.append(turtle)

    def create_snake(self):
        for i in range(settings["startLen"]):
            last_square_axis = [0, 0]
            axis = last_square_axis
            self.increase_size(axis)

    def extend_snake(self):
        self.increase_size(self.tail.position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(settings["step"])
        #print(f"Move to {self.segments[0].position()}")

    def face_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def face_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def face_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def face_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def collision(self):
        x_wall = S_WIDTH - (S_WIDTH / 2)
        y_wall = S_HEIGHT - (S_HEIGHT / 2)

        if self.head.xcor() > x_wall or self.head.xcor() < -x_wall or self.head.ycor() > y_wall or self.head.ycor() < -y_wall:
            return True

        for segment in self.body:
            if self.head.distance(segment) < 10:
                return True

        return False


