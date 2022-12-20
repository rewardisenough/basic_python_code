import random
import turtle
from turtle import Turtle,Screen

# move turtle
tim = Turtle()
tim.penup()
tim.setx(-25)
tim.sety(100)
tim.pendown()

# my solution
# for i in range(3,11):
#     angle = 360/i
#     for k in range(i):
#         tim.forward(50)
#         tim.right(angle)

# class solution
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
