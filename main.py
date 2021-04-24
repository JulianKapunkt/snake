from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Snake!")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")

snakey = Snake()
foodey = Food()
scorey = Scoreboard()

screen.listen()
screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.025)
    snakey.move()

    #Collision Detection
    if snakey.head.distance(foodey) < 30:
        foodey.refresh()
        scorey.increase_score()
        for i in range (10):
            snakey.add_segment()

    #Border Collision Detection
    if snakey.head.xcor() > 290 or snakey.head.xcor() < -290 or snakey.head.ycor() > 290 or snakey.head.ycor() < -290:
        game_is_on = False
        scorey.game_over()

    #Tail Collision Detection
    for segment in snakey.segments[1:]:
        if snakey.head.distance(segment) <= 5:
            game_is_on = False
            scorey.game_over()

screen.exitonclick()

