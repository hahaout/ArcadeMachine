"""
Snake Game Implementation

This script implements the classic Snake game using Pygame. It includes various challenges for functionality,
such as generating fruit, detecting collisions, and managing game state.
"""

import time
import pygame
import random
from config import get_game_config, initialize_snake

################################################################################################################
# Functions


def generate_fruit_position(snake_body, window_x, window_y):
    """
    Generates a random position for the fruit, ensuring it does not overlap with the snake's body.

    Args:
        snake_body (list): List of [x, y] positions representing the snake's body.
        window_x (int): Width of the game window.
        window_y (int): Height of the game window.

    Returns:
        tuple: A tuple (x, y) representing the fruit's position.
    """
    # CHALLENGE 4: make sure the fruit doesn't spawn on the snakes body
    # CHALLENGE 2: Implement the function generate_fruit_position to spawn a fruit RANDOMLY
    pass


def check_boundary_collision(snake_position, window_x, window_y):
    """
    Checks if the snake's head has collided with the game window's boundary.

    Args:
        snake_position (list): [x, y] position of the snake's head.
        window_x (int): Width of the game window.
        window_y (int): Height of the game window.

    Returns:
        bool: True if a collision occurred, False otherwise.
    """
    # CHALLENGE 5: stay Inside the Arena!!
    pass


def check_self_collision(snake_position, snake_body):
    """
    Checks if the snake's head has collided with its own body.

    Args:
        snake_position (list): [x, y] position of the snake's head.
        snake_body (list): List of [x, y] positions representing the snake's body.

    Returns:
        bool: True if a self-collision occurred, False otherwise.
    """
    # CHALLENGE 6: Stay in One Piece!!
    pass


def game_over():
    """
    Handles the Game Over sequence, displaying a message and pausing the game before quitting.

    Args:
        game_window (pygame.Surface): The Pygame surface for the game window.
        window_x (int): Width of the game window.
        window_y (int): Height of the game window.
        colors (dict): Dictionary of color mappings.

    Returns:
        None
    """
    # CHALLENGE 7: Game Over in Style!

    time.sleep(3)  # render game over for 3 sec then quit

# CHALLENGE 8: High-score (file operation)

# CHALLENGE 9: pause the screen

# CHALLENGE 10: Bombs

###########################################################################
# Setup

# # Initialize pygame
pygame.init()

# Load game configuration
config = get_game_config()
window_x, window_y = config["window_size"]
snake_speed = config["snake_speed"]
colors = config["colors"]

# Create game window
pygame.display.set_caption("Snake")
game_window = pygame.display.set_mode((window_x, window_y))

# Set up initial game state
snake_position, snake_body = initialize_snake()  # Initialize snake

# Initial fruit position (fixed position)
fruit_position = [360, 240]
fruit_spawn = True

#  CHALLENGE 2: call the function you implemented and spawn the fruit

# Define the initial direction and score
direction = "RIGHT"  # Snake starts moving to the right
score = 0

# CHALLENGE 10 : initialisation of list of bombs

# Highscore file name
filename = "high_score.txt"

# Set up the clock for controlling the game speed
fps = pygame.time.Clock()

#################################################################
# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:

            # CHALLENGE 1: Improve input handling for smoother gameplay
            pass

    # CHALLENGE 1: Movement logic
    if direction == "RIGHT":
        snake_position[0] += 10

    # Snake body growing mechanism if fruit and snake collide score
    snake_body.insert(0, list(snake_position))
    if (
        snake_position[0] == fruit_position[0]
        and snake_position[1] == fruit_position[1]
    ):
        # CHALLENGE 3: (Hints 1 and 2)
        pass
    else:
        snake_body.pop()

    # CHALLENGE 3: Generate a new fruit position when the previous one is eaten (Hints 3 and 4)

    # CHALLENGE 5: make sure the 'check_boundary_collision' is used

    # CHALLENGE 6: call the function you implemented

    # CHALLENGE 8: High-score Logic

    # CHALLENGE 10: use the function you implemented

    # Draw the game window
    game_window.fill(colors["black"])  # Fill background
    for pos in snake_body:
        pygame.draw.rect(
            game_window, colors["green"], pygame.Rect(pos[0], pos[1], 10, 10)
        )  # Draw snake

    # CHALLENGE 11

    pygame.draw.rect(
        game_window,
        colors["white"],
        pygame.Rect(fruit_position[0], fruit_position[1], 10, 10),
    )  # Draw fruit

    pygame.display.update()
    fps.tick(snake_speed)
