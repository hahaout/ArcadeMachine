import pygame
import random
from bullet import Bullet
from enemy import Enemy


class Boss(Enemy):
    """
    A specialized Boss class that extends the Enemy class with unique abilities:
    - Random left-right movement.
    - Shooting bullets back at the player.
    """

    # TODO: Challange05 Task01 Complete the constructor
    def __init__(self, pos, image, constraints, rank, settings, speed_y=0):
        self.settings = settings
        self.bullets = pygame.sprite.Group()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=pos)

    # TODO: Challange05 Task01 define behavior
    def move(self):
        """
        Moves the boss left and right within screen boundaries.
        Reverses direction when hitting the boundaries.
        """

    def shoot(self):
        """
        Fires bullets downward at intervals controlled by a cooldown timer.
        """

    def update(self, settings, score):
        """
        Update the enemy's position and state for each frame.

        Args:
            settings (dict): Game settings dictionary with screen dimensions and other configurations.
        """

    def draw_health_bar(self, surface):
        """
        Draws a health bar above the boss to indicate its remaining health.
        """
        bar_width = 100
        bar_height = 10
        health_ratio = self.health / (2 * self.rank)
        pygame.draw.rect(
            surface,
            (255, 0, 0),
            (self.rect.x, self.rect.top - 15, bar_width, bar_height),
        )  # Red bar
        pygame.draw.rect(
            surface,
            (0, 255, 0),
            (self.rect.x, self.rect.top - 15, bar_width * health_ratio, bar_height),
        )  # Green bar
