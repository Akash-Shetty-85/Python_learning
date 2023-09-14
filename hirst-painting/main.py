import turtle as t_module
import random

color_list = [(232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189),
              (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252),
              (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209),
              (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211),
              (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]
t_module.colormode(255)
tim = t_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
screen = t_module.Screen()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dots_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
