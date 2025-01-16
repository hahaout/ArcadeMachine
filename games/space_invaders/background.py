import pygame


class Background:
    """
    Represents the background image and contains/should contain functionality to load, scale and render the image.
    """

    def __init__(self, image_path: str, speed: int, width: int, height: int):
        """
        Initialize the background.
        :param image_path: Path to the image file.
        :param speed: Speed of background movement.
        :param width: The window width.
        :param height: The window height.
        """
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.separation_line_y = 0
        self.width = width
        self.max_height = height

    def draw(self, window: pygame.Surface):
        """
        Draw the background.
        :param window: pygame window object.
        :return:
        """
        # TASK 6.2 - Make the background move

        pass
