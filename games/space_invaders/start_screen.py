import os
import pygame
from pygame.locals import *
from states import States

from JSONHandler import JSONHandler
from JSONManager import JSONManager


class StartScreen(States):
    """
    Represents the start screen state of the game, where the player can enter their username,
    view instructions, and start the game. The start screen also allows navigating to other game states.

    Attributes:
        screen (pygame.Surface): The main display surface of the game.
        screen_rect (pygame.Rect): The rectangle representing the screen dimensions.
        settings (dict): A dictionary containing the game settings, such as images, fonts, and texts.
        background_image (pygame.Surface): The background image of the start screen.
        input_box (pygame.Rect): A rectangle representing the area where the player inputs their username.
        font_path (str): Path to the font file used for rendering text.
        username (str): The username entered by the player.
        handler (JSONHandler): The JSON handler for reading and writing player data.
        manager (JSONManager): The JSON manager for managing player data interactions.
    """

    def __init__(self, screen, settings):
        """
        Initializes the StartScreen class with the screen, settings, and other required components.

        :param screen: The main display surface where the start screen is rendered.
        :param settings: A dictionary containing various game settings such as images, fonts, and texts.
        """
        super().__init__(screen, settings)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.background_image = pygame.transform.scale(
            pygame.image.load(self.settings.get("images").get("background_image_path")),
            (screen.get_width(), screen.get_height()),
        )

        input_box_x = screen.get_width() // 4
        input_box_y = (
            screen.get_height() // 2
            - self.settings.get("fonts").get("font_size_large") // 2
        )

        input_box_width = screen.get_width() // 2
        input_box_height = self.settings.get("fonts").get("font_size_large") + 10

        self.input_box = pygame.Rect(
            input_box_x, input_box_y, input_box_width, input_box_height
        )

        self.font_path = settings.get("fonts").get("font_path")
        self.username = ""

        # JSON
        file_path = "./player_data.json"
        self.handler = JSONHandler(file_path)
        self.manager = JSONManager(self.handler)

    def get_event(self, event):
        """
        Handles user input events on the start screen, such as key presses to enter a username,
        navigate to the next game state, or quit.

        :param event: The event object representing a user action, such as a key press.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                self.done = True
            elif event.key == K_RETURN:
                if self.username != "":
                    self.manager.add_entry({"username": self.username})
                    self.settings.get("tracking_utilis").update(
                        {"username": self.username}
                    )
                    self.done = True
                    self.next = "space_invaders"
            elif event.key == pygame.K_SPACE:
                self.done = True
                self.next = "score_screen"
            elif event.key == K_BACKSPACE:
                # added elif block to handle backspace
                self.username = self.username[:-1]
            else:
                # ignore if length of object is greater than 10
                if len(self.username) < 10:
                    self.username += event.unicode

    def cleanup(self):
        """
        Cleans up the current state before transitioning to the next state.

        This could be used for logging purposes or to reset any variables if needed.
        """
        # TODO could be utilized for logging purposes
        pass

    def startup(self):
        """
        Prepares the start screen when it is first loaded.

        This could be used for logging purposes or initializing specific elements.
        """
        # TODO could be utilized for logging purposes
        pass

    def update(self, delta_time):
        """
        Updates and renders the start screen elements, such as drawing the background, input box,
        and text instructions. This method is called continuously in the game loop.

        :param delta_time: Time elapsed between the current and previous frame, used for animations if needed.
        """
        vertical_spacing = 20

        # Calculate initial y-position based on input box and font size
        font_size_large = self.settings.get("fonts").get("font_size_large")
        position_y_axis = self.input_box.top - font_size_large - vertical_spacing

        # Draw background image
        self.draw(self.background_image, (0, 0))

        # Draw instruction text
        instruction_text, instruction_rec = self.make_text(
            message=self.settings.get("texts").get("enter_username"),
            color="white",
            position=(self.screen_rect.centerx, position_y_axis),
            font_path=self.font_path,
            font_size=font_size_large,
        )
        self.draw(instruction_text, instruction_rec)

        # Draw the username input text field
        username_textfield, _ = self.make_text(
            message=self.username,
            color="lightskyblue3",
            font_size=font_size_large,
            position=(self.input_box.centerx, self.input_box.centery),
            font_path=self.font_path,
            background="black",
        )
        self.draw(
            username_textfield,
            username_textfield.get_rect(center=self.input_box.center),
        )

        # Draw border of username_textfield
        pygame.draw.rect(
            surface=self.screen,
            color="lightskyblue3",
            rect=self.input_box,
            width=2,
        )

        # Draw start game text
        position_y_axis = self.input_box.bottom + vertical_spacing
        start_text, start_rect = self.make_text(
            message=self.settings.get("texts").get("start_text"),
            color="white",
            font_size=font_size_large,
            font_path=self.font_path,
            position=(self.screen_rect.centerx, position_y_axis),
        )
        self.draw(start_text, start_rect)

        # Draw highscore text
        position_y_axis = start_rect.bottom + vertical_spacing
        highscore_text, highscore_rect = self.make_text(
            message=self.settings.get("texts").get("highscore_text"),
            color="white",
            font_size=font_size_large,
            font_path=self.font_path,
            position=(self.screen_rect.centerx, position_y_axis),
        )
        self.draw(highscore_text, highscore_rect)

    def draw(self, object, object_rect):
        """
        Draws an object onto the screen.

        :param object: The object (e.g., surface or text) to be drawn.
        :param object_rect: The rectangle defining the position to draw the object.
        """
        self.screen.blit(object, object_rect)

    def make_text(
        self, message, color, font_size, font_path, position=None, background=None
    ):
        """
        Creates a text surface and rectangle with the given properties.

        :param message: The text message to be rendered.
        :param color: The color of the text.
        :param font_size: The size of the font to be used.
        :param font_path: The path to the font file.
        :param position: The position where the text will be centered (default is None).
        :param background: The background color of the text (default is None for transparent).
        :return: A tuple containing the rendered text surface and its rectangle.
        """
        font = pygame.font.Font(font_path, font_size)
        text = font.render(message, True, color, background)
        rect = text.get_rect(center=position)
        return text, rect
