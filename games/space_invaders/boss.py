import pygame
import random
from bullet import Bullet
from enemy import Enemy
from score import Score

class Boss(Enemy):
    """
    A specialized Boss class that extends the Enemy class with unique abilities:
    - Random left-right movement.
    - Shooting bullets back at the player.
    """

    # TODO: Challange05 Task01 Complete the constructor
    def __init__(self, pos, image, constraints, rank, settings, speed_y=0):
        print("Boss spawn success")
        super().__init__(pos, image, constraints, speed_y, rank)
        self.settings = settings
        self.bullets = pygame.sprite.Group()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=pos)

        self.speed_x = 1
        self.health = rank * 2
        self.last_shoot_time = 0
        self.shoot_cooldown = 900
        self.bullets = pygame.sprite.Group()
        self.dead = False

    # TODO: Challange05 Task01 define behavior
    def move(self):
        """
        Moves the boss left and right within screen boundaries.
        Reverses direction when hitting the boundaries.
        """
        #screen_width = self.settings.get("general").get("window_height")
        # if self.rect.left <= 0 or self.rect.right >= self.constraints[1]:
        # ?
        if self.rect.left <= 0 or self.rect.right > self.settings.get("general").get("window_height"):
            self.speed_x *= -1
        self.rect.x -= self.speed_x

    def shoot(self):
        """
        Fires bullets downward at intervals controlled by a cooldown timer.
        """
        curr_time = pygame.time.get_ticks()
        boss_position = ((self.rect.left + self.rect.right)//2, (self.rect.top + self.rect.bottom)//2)
        bullet_image_path = self.settings.get("images").get("bullet_image_path")
        bullet_sound_path = self.settings.get("sounds").get("bullet_sound_path")
        if curr_time - self.last_shoot_time >= self.shoot_cooldown:
            bullet = Bullet(boss_position,5,bullet_image_path,bullet_sound_path)
            self.bullets.add(bullet)
            self.last_shoot_time = curr_time

        self.bullets.update(boss = True)


    def update(self, settings, score):
        """
        Update the enemy's position and state for each frame.

        Args:
            settings (dict): Game settings dictionary with screen dimensions and other configurations.
        """
        if not self.dead:
            self.shoot()
            self.move()
        else:
            self.kill()


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

    def handle_boss_hit(self):
        self.health -= 1
        if self.health <= 0:
            self.dead = True
            self.kill()
        return self.rank, self.dead
