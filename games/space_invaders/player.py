import pygame
from pygame.sprite import Sprite

from bullet import Bullet


class Player(pygame.sprite.Sprite):
    """
    Represents the player's ship, managing its movement, rendering, and shooting mechanics.

    This class handles player controls, including movement and firing bullets, with a cooldown
    system to prevent rapid, uncontrolled bullet firing.
    """

    def __init__(self, settings):
        """
        Initialize the player object.
        :param settings:
        """
        super().__init__()
        self.level = 1
        self.settings = settings
        player_image = pygame.image.load(
            self.settings.get("images").get("player_image_path")
        )
        self.image = pygame.transform.scale(player_image, (100, 100))
        self.add_life_sound = pygame.mixer.Sound(
            self.settings.get("sounds").get("life_sound_path")
        )
        self.bullets = pygame.sprite.Group()
        self.shoot_cooldown = self.settings.get("general").get("shoot_cooldown")
        self.last_shot_time = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = self.settings.get("general").get("window_width") // 2
        self.rect.bottom = self.settings.get("general").get("window_height") - 10
        self.speed = 5
        self.lives = 3

    def get_event(self):
        """
        Handle player events: movement and firing bullets
        player moves using arrow keys, and shoots using space key
        :return:
        """
        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] ==True and self.rect.left >0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] ==True and self.rect.right <width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] ==True and self.rect.top >0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] ==True and self.rect.bottom<height:
            self.rect.y += self.speed
        # TODO:Challange01TASK01 Move player and shoot bullets

        self.bullets.update()

    # TODO: Challenge 01 Task 02
    def shoot(self):
        """
        Firing bullets.
        :return:
        """

    def reset(self):
        """
        Reset player position, lives and empty current fired bullets.
        :return: Nothing.
        """
        self.rect.centerx = self.settings.get("general").get("window_width") // 2
        self.rect.bottom = self.settings.get("general").get("window_height") - 10
        self.lives = 3
        self.bullets.empty()

    def upgrade_level(self):
        """
        Upgrade player level and add a life after every 5 upgrades.
        :return:
        """
        self.level += 1
        if self.level % 5 == 0:
            self.add_life_sound.play()
            self.add_life()

    def add_life(self):
        """
        Add life to the player

        """
        if self.lives <= 2 & self.lives >= 1:
            self.lives += 1

    def take_life(self):
        """

        Take life from the player.

        """
        if self.lives > 0:
            self.lives -= 1
        else:
            pass
