import pygame as pg
import os
import sys

from games.space_invaders.config import config
from games.space_invaders.control import Control
from games.space_invaders.game_over_screen import GameOverScreen
from games.space_invaders.space_invaders import SpaceInvaders
from games.space_invaders.score_screen import ScoreScreen
from games.space_invaders.start_screen import StartScreen


def main():
    """
    Main function to initialize and run the Space Invaders game.

    This function sets up the game environment by initializing Pygame, creating the Control instance,
    and defining the states of the game. It then starts the main game loop and gracefully handles exiting.

    Workflow:
    1. Initialize Pygame.
    2. Create a Control object with the game configuration.
    3. Define the game states: start screen, score screen, main game, and game over screen.
    4. Set the initial state to "start_screen".
    5. Enter the main game loop.
    6. Quit Pygame and exit the application when the game ends.

    Returns:
        None
    """
    pg.init()
    app = Control(**config)
    state_dict = {
        "start_screen": StartScreen(app.get_screen(), app.get_settings()),
        "score_screen": ScoreScreen(app.get_screen(), app.get_settings()),
        "space_invaders": SpaceInvaders(app.get_screen(), app.get_settings()),
        "game_over_screen": GameOverScreen(app.get_screen(), app.get_settings()),
    }
    app.setup_states(state_dict, "start_screen")
    app.main_game_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
