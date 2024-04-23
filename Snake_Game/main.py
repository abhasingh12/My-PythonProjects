from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My snake game")




snake = Snake()
food = Food()
count=ScoreBoard()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect distance with food
    if snake.head.distance(food) < 15:
        count.update()
        snake.extend()
        food.refresh()
        
    #Detect collision with wall.
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_is_on = False
        count.game_over()

    #Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            count.game_over()


screen.exitonclick()