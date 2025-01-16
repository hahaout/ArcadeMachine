import random

import pygame
from pygame import Surface

from games.space_invaders.spritesheet import Spritesheet


class Enemy(pygame.sprite.Sprite):
    """
    Enemy class for creating enemy sprites with varying difficulty and behavior.

    This class handles enemy attributes, spawning, movement, health, and interactions such as explosions.
    It allows for the creation of enemies of different ranks and includes utilities for managing enemy states.
    """

    def __init__(
        self,
        pos: tuple[int, int],
        image: Surface,
        constraints: tuple[int, int],
        enemy_speed_y: float = 0.75,
        rank: int = 1,
    ):
        """
        Initialize an enemy instance with position, appearance, and behavior attributes.
        Args:
            pos (tuple[int, int]): Initial position of the enemy (x, y).
            image (Surface): Surface image representing the enemy.
            constraints (tuple[int, int]): Screen width and height boundaries for movement.
            enemy_speed_y (float, optional): Vertical speed of the enemy. Default is 0.75.
            rank (int, optional): Difficulty level of the enemy, affecting its health. Default is 1.
        """
        super().__init__()

        self.explosion_sound = None
        self.explosion_images = None

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos

        # Initialize parameters
        self.constraints = constraints
        self.speed_y = enemy_speed_y
        self.rank = rank
        self.health = 1
        self.dead = False

    @staticmethod
    def no_enemies(enemies) -> bool:
        """
        Check if the enemy group is empty.

        Args:
            enemies: List or group of enemy sprites.

        Returns:
            bool: True if no enemies are present, otherwise False.
        """
        return len(enemies) <= 0

    @staticmethod
    def spawn(
        wave_length: int, image: Surface, rank: int = 1
    ) -> list[pygame.sprite.Sprite]:
        """
        Spawn a wave of enemies.

        Args:
            wave_length (int): Number of enemies to spawn.
            image (Surface): Surface image for the enemy sprite.
            rank (int, optional): Difficulty rank for the enemies. Default is 1.

        Returns:
            list[pygame.sprite.Sprite]: List of spawned enemy instances.
        """
        spawned_enemies = []
        enemy_width = 50
        screen_width, screen_height = pygame.display.get_surface().get_size()

        # ADVANCED -TASK 2 - Add explosions
        for i in range(wave_length):
            enemy_x = random.randrange(0, screen_width - enemy_width)
            enemy_y = random.randrange(-10, 30)
            enemy = Enemy(
                pos=(enemy_x, enemy_y),
                image=image,
                constraints=(screen_width, screen_height),
                rank=rank,
            )
            spawned_enemies.append(enemy)

        return spawned_enemies

    @staticmethod
    def load_enemy_image(
        spritesheet: Spritesheet,
        location: tuple[int, int, int, int],
        scale: tuple[int, int],
    ) -> Surface:
        """
        Load and scale an enemy image from a spritesheet.

        Args:
            spritesheet (Spritesheet): Spritesheet containing enemy images.
            location (tuple[int, int, int, int]): Coordinates of the image on the spritesheet (x, y, width, height).
            scale (tuple[int, int]): Scaling dimensions for the image (width, height).

        Returns:
            Surface: The loaded and scaled enemy image.
        """
        enemy_image = spritesheet.image_at(location, -1)
        return pygame.transform.scale(enemy_image, scale)

    def handle_enemy_hit(self):
        """
        Update the enemy's position and state for each frame.

        Args:
            settings (dict): Game settings dictionary with screen dimensions and other configurations.
        """

        self.health -= 1
        if self.health <= 0:
            self.dead = True
            self.kill()
        return self.rank

    def update(self, settings, score):
        """
        Update the enemy's position and state for each frame.

        Args:
            settings (dict): Game settings dictionary with screen dimensions and other configurations.
        """
        # TODO Challange 03 Task02: Decrease Score
        if not self.dead:
            self.move()
            self.check_bounds()
        else:
            self.kill()

        # Remove enemy if it moves off-screen
        if self.rect.top > settings.get("general").get("window_height"):
            self.kill()

    def move(self):
        """
        Move the enemy vertically based on its speed.
        """
        self.rect.y += self.speed_y

    def check_bounds(self):
        """
        Check if the enemy is out of screen bounds and remove it if necessary.
        """
        if self.rect.top > self.constraints[1]:
            self.kill()

    @classmethod
    def preload_all_images(cls, settings: dict) -> dict[str, Surface]:
        """
        Preload and scale all enemy images from a spritesheet.

        Args:
            settings (dict): Settings containing the spritesheet path, image coordinates, and scaling details.
        Returns:
            dict[str, Surface]: A dictionary mapping enemy names to their respective images.
        """
        enemy_images = {}
        enemy_sheet = settings.get("images").get("enemy_sheet_path")
        spritesheet = Spritesheet(enemy_sheet)

        enemy_coordinates = settings.get("enemy_coordinates")
        enemy_scale = settings.get("enemy_attributes").get("normal_enemy_scale")

        for key, location in enemy_coordinates.items():
            enemy_image = cls.load_enemy_image(spritesheet, location, enemy_scale)
            # Store the loaded image in the dictionary with the key
            enemy_images[key] = enemy_image

        return enemy_images
