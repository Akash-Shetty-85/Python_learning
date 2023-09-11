import random
from turtle import Turtle, Screen

t = Turtle()

# t.shape("turtle")
# t.color("red")
# for i in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

colors = ["dark green", "dark green", "firebrick", "violet", "orange red", "dark goldenrod", "light steel blue",
          "lawn green", "steel blue", "green yellow", "gold"]

# def draw_shape(sides):
#     angle = 360 / sides
#     t.width(2)
#     t.color(random.choice(colors))
#     for _ in range(sides):
#         t.forward(100)
#         t.right(angle)
#
#
# for i in range(3, 15):
#     draw_shape(i)

directions = [0, 90, 180, 270]
t.speed("fastest")
t.width(3)


def random_color():
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    random_color_value = (r, g, b)
    return random_color_value


def random_walk():
    choice_of_directions = random.choice(directions)
    color = random_color()
    print(color)
    t.color(color)
    t.forward(30)
    t.setheading(choice_of_directions)


for _ in range(300):
    random_walk()
screen = Screen()
screen.exitonclick()
