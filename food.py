import random
from turtle import Turtle


# We're inheriting Turtle class into our food class, and we're modifying some of the methods too.
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # the screen setup is 600 / 600, so +ve x as 300 so as y, and -ve x and y has -300 so the snake has to move
        # around -280 and 280 coz it won't go beyond the boundary.
        self.goto(random_x, random_y)
