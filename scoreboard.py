from turtle import Turtle

# --- Constants for styling the scoreboard text ---
ALIGN = "center"
FONT = ('Arial', 13, 'normal')

class Scoreboard(Turtle):
    """A class to manage and display the score."""

    def __init__(self):
        """Initialize the scoreboard's attributes."""
        super().__init__()
        self.score = 0  # Initialize score to 0
        self.color("white")  # Set the text color
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 270)  # Position the score at the top of the screen
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard() # Write the initial score

    def update_scoreboard(self):
        """Clear the old score and write the new score."""
        self.clear() # Clear any previous text written by this turtle
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increase the score by one and update the display."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Display the 'Game Over' message at the center of the screen."""
        self.goto(0, 0) # Move to the center
        self.write("GAME OVER", align=ALIGN, font=FONT)