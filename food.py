from turtle import Turtle
import random

class Food(Turtle):
    """A class to represent the food in the game."""

    def __init__(self):
        """Initialize the food's attributes."""
        super().__init__()
        self.shape("circle")  # Set the shape of the food
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the circle smaller
        self.color("blue")  # Set the food's color
        self.speed("fastest")  # Set the drawing speed to maximum
        self.refresh()  # Place the food at a random initial location

    def refresh(self):
        """Move the food to a new random position on the screen."""
        # Generate random x and y coordinates within the screen boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)