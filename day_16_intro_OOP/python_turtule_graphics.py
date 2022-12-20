from turtle import Turtle, Screen  # importing classes from module named 'turtle'

timmy = Turtle()  # creating object named timmy from Turtle class.

print(timmy)  # object and memory address

timmy.shape('turtle')  # method from Turtle class.
timmy.color('coral')  # method from Turtle class.
timmy.forward(100)  # method from Turtle class.

my_screen = Screen()  # creating object named my_screen from Screen class.
print(my_screen.canvheight)  # printing an attribute of object 'my_screen'.
my_screen.exitonclick()  # method from Screen class.
