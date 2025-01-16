import pygame


class Life(pygame.sprite.Sprite):
    """Life class to represent the player's remaining lives."""

    def __init__(self, pos, image_path):
        """
        This class manages the life sprites displayed on the screen to indicate the player's
        remaining lives. It includes methods for creating and updating the group of life sprites.
        Initialize a life sprite with a given position and image.

        Args:
            pos (tuple[int, int]): Tuple representing the (x, y) position of the life sprite.
            image_path (str): File path to the image representing the life.
        """
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    @classmethod
    def create_lives(cls, player_lives: int, image_path: str) -> pygame.sprite.Group:
        """
        Create a group of life sprites based on the player's total lives.

        Args:
            player_lives (int): The number of lives the player currently has.
            image_path (str): File path to the image representing each life.

        Returns:
            pygame.sprite.Group: A group containing all the life sprites.
        """
        lives_group = pygame.sprite.Group()
        for i in range(player_lives):
            position = (
                15 + i * 15,
                20,
            )  # Each heart is spaced by 40 pixels horizontally
            lives_group.add(cls(position, image_path))
        return lives_group

    @staticmethod
    def update_lives_group(
        lives_group: pygame.sprite.Group, player_lives: int, image_path: str
    ):
        """
        Update the group of life sprites to match the current number of player lives.

        Args:
            lives_group (pygame.sprite.Group): The existing group of life sprites.
            player_lives (int): The updated number of lives the player has.
            image_path (str): File path to the image representing each life.

        Returns:
            No return value.
        """
        lives_group.empty()  # Clear all existing life sprites
        for i in range(player_lives):
            position = (
                15 + i * 15,
                20,
            )  # Each heart is spaced by 40 pixels horizontally
            lives_group.add(Life(position, image_path))
