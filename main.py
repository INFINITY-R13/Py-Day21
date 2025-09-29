# Import necessary classes and modules
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# --- Screen Setup ---
# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the game window
screen.bgcolor("black")  # Set the background color
screen.title("My Snake Game")  # Set the title of the window
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# --- Game Objects ---
# Create instances of the Snake, Food, and Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- Keyboard Bindings ---
# Listen for keyboard input
screen.listen()
# Map arrow keys to the snake's movement methods
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- Main Game Loop ---
game_is_on = True
while game_is_on:
    # Manually update the screen inside the loop
    screen.update()
    # Pause the game for a short duration to control the snake's speed
    time.sleep(0.1)
    # Move the snake forward
    snake.move()

    # 1. Detect collision with food
    # If the distance between the snake's head and the food is less than 15 pixels
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()  # Increase the score

    # 2. Detect collision with wall
    # If the snake's head goes beyond the screen boundaries
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # End the game
        scoreboard.game_over()  # Display the "Game Over" message

    # 3. Detect collision with tail
    # Iterate through the snake's segments, excluding the head
    for segment in snake.segments[1:]:
        # If the head collides with any segment in the tail
        if snake.head.distance(segment) < 10:
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the "Game Over" message

# Exit the game when the screen is clicked
screen.exitonclick()