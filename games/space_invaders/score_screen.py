import pygame
from states import States
from JSONHandler import JSONHandler
from JSONManager import JSONManager


class ScoreScreen(States):
    def __init__(self, screen, settings):
        """
        Initialize the highscore screen
        :param screen:
        :param settings:
        """
        super().__init__(screen, settings)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.background_image = pygame.transform.scale(
            pygame.image.load(self.settings.get("images").get("background_image_path")),
            (screen.get_width(), screen.get_height()),
        )

        self.font_path = settings.get("fonts").get("font_path")
        self.font_size = settings.get("fonts").get("font_size_large")

        self.json_manager = JSONManager(JSONHandler("player_data.json"))

    def update(self, dt):
        """
        Update the highscore screen.
        :param dt:
        :return:
        """
        vertical_spacing = 40
        position_y_axis = self.screen_rect.centery - self.font_size // 2 - 100

        # Draw background image
        self.draw(self.background_image, (0, 0))

        # TODO Challenge04 Task02 : call the function to get the highscores
        highscores = self.json_manager.get_highscores()
        # TODO: highscore displaying logic Comment this out when Completing Challenge04 Task02 and edit according to pass to your solution
        for index, score_entry in enumerate(highscores):
             message = f"{index + 1}. {score_entry[0]} - {score_entry[1]}"
             text, rect = self.make_text(
                message=message,
                 color="white",
                 position=(self.screen_rect.centerx, position_y_axis),
                 font_size=self.font_size,
                 font_path=self.font_path,
             )
             self.draw(text, rect)
             position_y_axis += vertical_spacing

        # TODO: Given Code Placeholder highscore text Delete when reaching Challenge04
        """placeholder_text, placeholder_rect = self.make_text(
            message="",
            color="white",
            position=(self.screen_rect.centerx, position_y_axis),
            font_size=self.font_size,
            font_path=self.font_path,
        )

        self.draw(placeholder_text, placeholder_rect)"""
        
        # Draw exit text
        position_y_axis += 250
        exit_text, exit_rect = self.make_text(
            message=self.settings.get("texts").get("exit_text"),
            color="white",
            position=(self.screen_rect.centerx, position_y_axis),
            font_size=self.font_size,
            font_path=self.font_path,
        )
        self.draw(exit_text, exit_rect)

        # Update the display
        pygame.display.update()

    def make_text(
        self, message, color, position, font_size, font_path, background=None
    ):
        """
        Make the text on the screen.
        :param message:
        :param color:
        :param position:
        :param font_size:
        :param font_path:
        :param background:
        :return:
        """
        font = pygame.font.Font(font_path, font_size)
        text = font.render(message, True, color, background)
        rect = text.get_rect(center=position)
        return text, rect

    def cleanup(self):
        """
        Cleanup all irrelevant data, when leaving the state.
        :return:
        """
        pass

    def startup(self):
        """
        Initialize all relevant variables needed.
        :return:
        """

        pass

    def draw(self, object, object_rect):
        """
        Draw all visual components of the highscore screen. Has to be called for every blittable component.
        :param object:
        :param object_rect:
        :return:
        """
        self.screen.blit(object, object_rect)

    def get_event(self, event):
        """
        Gets a keypress event and handles it.
        :param event:
        :return:
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.done = True
