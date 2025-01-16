import pygame

from states import States
from score import Score
from JSONHandler import JSONHandler
from JSONManager import JSONManager


class GameOverScreen(States):
    """
    GameOverScreen class to manage the game over state.

    This screen is displayed when the player loses all their lives. It includes features such as
    displaying the "Game Over" message, the player's username, and score, along with options to
    return to the start screen, view the score screen, or quit the game.
    """

    def __init__(self, screen, settings):
        """
        Initialize the Game Over screen with necessary configurations.

        Args:
            screen (pygame.Surface): The display surface where the screen elements will be rendered.
            settings (dict): Dictionary containing game settings like fonts, images, and sounds.
        """
        super().__init__(screen, settings)
        self.screen = screen
        self.settings = settings
        self.initialize_game_over_state()

    def initialize_game_over_state(self):
        """
        Initialize all attributes required for the game over state, including loading assets
        such as background images, fonts, and sounds. Sets up dynamic properties for animations.

        Returns:
            No return value.
        """
        # Load assets
        self.background_image = pygame.transform.scale(
            pygame.image.load(self.settings.get("images").get("background_image_path")),
            (self.screen.get_width(), self.screen.get_height()),
        )
        self.font_path = self.settings.get("fonts").get("font_path")
        self.font_size_initial = self.settings.get("fonts").get("font_size_initial")
        self.font_size_large = self.settings.get("fonts").get("font_size_large")
        self.font_size_small = self.settings.get("fonts").get("font_size_small")

        # JSON setup
        file_path = "./player_data.json"
        self.handler = JSONHandler(file_path)
        self.manager = JSONManager(self.handler)
        self.user_name = self.settings.get("tracking_utilis").get("username")
        self.sound = pygame.mixer.Sound(
            self.settings.get("sounds").get("game_over_sound_path")
        )
        self.sound.play()

        # Dynamic properties for animation
        self.font_size = self.font_size_initial
        self.font_pos = (self.screen.get_width() // 2, self.screen.get_height() // 2)

    def startup(self, **persistent):
        """
        Setup the game over screen state when transitioning into it.

        Reinitializes the game over state attributes to ensure a fresh start when the state is
        re-entered.

        Args:
            persistent (dict): Optional persistent data passed between states.

        Returns:
            No return value.
        """
        # Reinitialize all game-over state attributes to ensure the screen starts fresh
        self.initialize_game_over_state()

    def get_event(self, event):
        """
        Handle user input events for the game over screen.

        Handles quitting the game, returning to the start screen, viewing the score screen, or exiting.

        Args:
            event (pygame.event.Event): Event object representing user input.

        Returns:
            No return value.
        """

        if event.type == pygame.QUIT:
            self.done = True
            self.next = "quit"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.done = True
                self.next = "start_screen"
            elif event.key == pygame.K_SPACE:
                self.done = True
                self.next = "score_screen"
            elif event.key == pygame.K_ESCAPE:
                self.done = True
                self.next = "quit"

    def update(self, delta_time):
        """
        Update the game over screen's state and render its elements.

        Updates include animating the "Game Over" text and rendering other screen elements like
        the username, score, and navigation instructions.

        Args:
            delta_time (float): Time elapsed since the last frame update.

        Returns:
            None
        """
        # Render the background
        self.draw(self.background_image, (0, 0))

        # Render the "Game Over" text with increasing font size
        self.font = pygame.font.Font(self.font_path, self.font_size)
        game_over_text, game_over_rect = self.make_text(
            message=self.settings.get("texts").get("game_over_text"),
            color="red",
            font_size=self.font_size,
            font_path=self.font_path,
            position=self.font_pos,
        )
        self.draw(game_over_text, game_over_rect)

        # Animate font size and position
        if self.font_size < self.font_size_large:
            self.font_size += 1
            self.font_pos = (self.font_pos[0], self.font_pos[1] - 1)

        # Render the username
        username_text, username_rect = self.make_text(
            message=f"{self.settings.get('texts').get('username_text')} {self.user_name}",
            color="white",
            font_size=self.font_size,
            font_path=self.font_path,
            position=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50),
        )
        self.draw(username_text, username_rect)

        # Render the score
        score_text, score_rect = self.make_text(
            message=f"{self.settings.get('texts').get('score_text')} {self.settings.get("tracking_utilis").get("score")}",
            color="white",
            font_size=self.font_size,
            font_path=self.font_path,
            position=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2 + 100,
            ),
        )
        self.draw(score_text, score_rect)

        # Render the continue instructions
        continue_text, continue_rect = self.make_text(
            message=self.settings.get("texts").get("continue_text"),
            color="white",
            font_size=self.font_size_small,
            font_path=self.font_path,
            position=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2 + 200,
            ),
        )
        self.draw(continue_text, continue_rect)

        # Render the highscore instructions
        highscore_text, highscore_rect = self.make_text(
            message=self.settings.get("texts").get("highscore_text"),
            color="white",
            font_size=self.font_size_small,
            font_path=self.font_path,
            position=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2 + 250,
            ),
        )
        self.draw(highscore_text, highscore_rect)

        # Render the exit instructions
        exit_text, exit_rect = self.make_text(
            message=self.settings.get("texts").get("exit_text"),
            color="white",
            font_size=self.font_size_small,
            font_path=self.font_path,
            position=(
                self.screen.get_width() // 2,
                self.screen.get_height() // 2 + 300,
            ),
        )
        self.draw(exit_text, exit_rect)

    def draw(self, object, object_rect):
        """
        Draw an object on the screen.

        Args:
            object (pygame.Surface): The object to be drawn.
            object_rect (pygame.Rect): The rectangle defining the position and size of the object.

        Returns:
            None
        """
        self.screen.blit(object, object_rect)

    def make_text(self, message, color, font_size, font_path, position=None):
        """
        Create a text surface and its rectangle for rendering.

        Args:
            message (str): The text content to display.
            color (str or tuple): The color of the text.
            font_size (int): Font size for the text.
            font_path (str): Path to the font file.
            position (tuple[int, int], optional): The position of the text's center on the screen.

        Returns:
            tuple[pygame.Surface, pygame.Rect]: The rendered text surface and its rectangle.
        """
        font = pygame.font.Font(font_path, font_size)
        text = font.render(message, True, color)
        rect = text.get_rect(center=position)
        return text, rect
