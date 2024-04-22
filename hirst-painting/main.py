import colorgram
import turtle
import random
# rgb_colors= []
# colors= colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g,b)
#     rgb_colors.append(new_color)

cm = turtle.colormode(255)
color_list =[(233, 225, 81), (109, 176, 212), (188, 10, 65), (193, 78, 24), (185, 169, 18), (212, 164, 107), (206, 139, 178), (217, 63, 135), (56, 93, 155), (195, 35, 123), (113, 190, 154), (36, 28, 156), (20, 24, 62), (228, 222, 13), (224, 171, 201), (91, 93, 210), (60, 115, 71), (79, 172, 91), (19, 48, 28), (61, 13, 29), (67, 25, 9), (127, 215, 234), (152, 212, 191), (169, 182, 232), (218, 77, 50), (35, 88, 40)]



tim = turtle.shape("arrow")
#tim = turtle.pensize(3)


turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

number_of_dots = 101


for dot_count in range(1, number_of_dots):
    tim = turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dot_count % 10 ==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0) 
        
    



screen = turtle.Screen()
screen.exitonclick()