import pygame


class Bullet(pygame.sprite.Sprite):
    """
    Each instantiation of this class is a single bullet. This class contains funcitonality to initialize (get size, sound and image) and update the bullets position.
    Contains the code to define individual bullets shot at the enemies.
    """

    # TODO Challenge06:  Optimize this class for Player and Boss Bullets
    def __init__(self, pos, speed, image_path, sound_path):
        """
        Initializes the Bullet-sprite.
        :param pos: position of the bullet.
        :param speed: moving speed of the bullet.
        """
        super().__init__()
        self.image = pygame.image.load(
            image_path
        ).convert_alpha()  # Use convert_alpha for transparency
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.sound = pygame.mixer.Sound(sound_path)
        self.sound.play()

    def update(self, boss):
        """
        Updates the bullets position. Removes it if it is off the screen.

        """
        if boss == True:
            self.rect.y += self.speed
            #if (
            #    self.rect.bottom < pygame.display.get_surface().get_height()
            #):  # Kill bullet when it leaves the screen
            #    self.kill()
        else:
            self.rect.y -= self.speed  # Move bullet upwards
            if (
                self.rect.top > pygame.display.get_surface().get_height()
            ):  # Kill bullet when it leaves the screen
                self.kill()
