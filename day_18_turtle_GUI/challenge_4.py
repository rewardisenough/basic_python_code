import random
import turtle
from turtle import Turtle,Screen
tim = Turtle()

# move turtle to the center.
def center(x,y):
    tim.setx(x)
    tim.sety(y)

# code
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(1000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

    if(tim.xcor()<-400 or tim.xcor()>400 or tim.ycor()<-400 or tim.ycor()>400):
        center(random.randint(-100,100),random.randint(-100,100))


screen = Screen()
screen.exitonclick()
