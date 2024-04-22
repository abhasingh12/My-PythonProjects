from turtle import Turtle, Screen
import random

screen = Screen()

# def move_ford():
#     tim.forward(10)

# def move_back():
#     tim.backward(10)

# def move_rotate():
#     new= tim.heading() + 10
#     tim.setheading(new)

# def move_anti():
#     new= tim.heading() - 10
#     tim.setheading(new)
    
# def move_clean():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(key="w", fun=move_ford)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=move_rotate)
# screen.onkey(key="d", fun=move_anti)
# screen.onkey(key="c", fun=move_clean)

screen.setup(width = 500, height = 400)
user_bet =screen.textinput(title="Make your bet", prompt = "Which turtle will win? Enter a color: ")
print(user_bet)
colors =["red", "orange", "yellow", "green", "blue", "purple"]
a= 0
is_race_on = False
all_turtles=[]

for i in range(6):
    place = -60 + a
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x= -240,y= place)
    a += 40
    all_turtles.append(tim)
    
if user_bet:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 230:
            winning_color = tur.pencolor()
            if winning_color == user_bet:
                print(f"you won! winner is {winning_color}")
            else:
                print(f"you lose! winner is {winning_color}")
            is_race_on = False
        distance = random.randint(0,10)
        tur.forward(distance)


screen.exitonclick() 