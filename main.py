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

t.speed("fastest")


# t.width(3)


def random_color():
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    random_color_value = (r, g, b)
    return random_color_value


def draw_sprigrapg(size_pf_gap):
    for _ in range(int(360 / size_pf_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_pf_gap)


draw_sprigrapg(5)
screen = Screen()
screen.exitonclick()
