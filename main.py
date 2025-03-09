import time
from settings import settings
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=settings["screen_width"], height=settings["screen_height"])
screen.bgcolor('black')
screen.title("Snake Game - msworks.arw")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.create_snake()

screen.listen()

#Catch movement
screen.onkey(snake.face_up, "Up")
screen.onkey(snake.face_left, "Left")
screen.onkey(snake.face_down, "Down")
screen.onkey(snake.face_right, "Right")

#Game listener
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1 / settings["fps"])
    snake.move()

    if snake.head.distance(food) < 15:
        points_increase = settings["points_amount"]
        snake.extend_snake()
        food.food_spawn()
        scoreboard.increase_points(amount=points_increase * settings["points_multiplier"])
        print(f"Points amount: {scoreboard.points} (+ {points_increase})")

    if snake.collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()