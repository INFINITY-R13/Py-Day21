from turtle import Turtle

# --- Constants ---
# Initial positions for the starting snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Distance the snake moves in each step
MOVE_DISTANCE = 20
# Heading angles for directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to represent the snake in the game."""

    def __init__(self):
        """Initialize the snake's attributes."""
        self.segments = []  # List to hold the snake's segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The head is the first segment

    def create_snake(self):
        """Create the initial 3-segment snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at a given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # Lift the pen to avoid drawing lines
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the end of the snake."""
        # The new segment is added at the position of the last existing segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward."""
        # The segments move by following the segment in front of them.
        # We loop from the last segment to the second segment.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get the position of the segment in front
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Move the current segment to that position
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head (first segment) forward
        self.head.forward(MOVE_DISTANCE)

    # --- Control Methods ---
    def up(self):
        """Change the snake's heading to UP, if not currently moving DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's heading to DOWN, if not currently moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's heading to LEFT, if not currently moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's heading to RIGHT, if not currently moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)