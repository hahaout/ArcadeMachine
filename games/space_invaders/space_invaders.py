import pygame
import random

from pygame.transform import scale

from enemy import Enemy
from life import Life
from states import States
from player import Player
from score import Score
from JSONManager import JSONManager
from JSONHandler import JSONHandler
from boss import Boss


def display_level(level, screen, name, size):
    """
    Displays the current level of the player on the screen.

    :param level: The current level of the player.
    :param screen: The main display surface where the level text will be rendered.
    :param name: The path to the font file used for rendering the level text.
    :param size: The size of the font used for rendering the level text.
    """
    font = pygame.font.Font(name, size)
    level_text = font.render(f"level: {level}", False, "white")
    level_rect = level_text.get_rect(topleft=(10, 60))
    screen.blit(level_text, level_rect)


class SpaceInvaders(States):
    """
    Main gameplay state. Manages all the game elements visible during the active gameplay,
    including the player, enemies, score, and other game mechanics.
    """

    def __init__(self, screen, settings):
        """
        Initializes all attributes of the SpaceInvaders class.

        :param screen: The main display surface where all game elements are rendered.
        :param settings: A dictionary containing the game settings, such as images, fonts, and texts.
        """
        super().__init__(screen, settings)
        self.preload_images = None
        self.screen = screen
        self.settings = settings
        self.initialize_game_state()

        # JSON
        file_path = "./player_data.json"
        self.handler = JSONHandler(file_path)
        self.manager = JSONManager(self.handler)

    def initialize_game_state(self):
        """
        Initializes all required objects and data for the game state, such as player, enemies,
        score, and lives.
        """
        # TODO Challenge06: add a Boss attribute
        self.wave_length = 5
        self.max_wave_length = 10
        self.player = Player(settings=self.settings)
        self.enemies = pygame.sprite.Group()
        self.score = Score(
            screen=self.screen,
            name=self.settings.get("fonts").get("font_path"),
            size=self.settings.get("fonts").get("font_size_initial"),
            start_score=self.settings.get("tracking_utilis").get("score"),
        )
        # Initialize lives using the create_lives method from Life
        self.lives = Life.create_lives(
            self.player.lives, self.settings.get("images").get("life_image_path")
        )

        # Preload and scale all enemy images to avoid lag during gameplay
        self.preload_images = Enemy.preload_all_images(settings=self.settings)

    def startup(self, **persistent):
        """
        Executed when entering the state after switching from another state.
        Sets up the game state when first entering this state.

        :param persistent: Persistent data passed from the previous game state.
        """
        self.initialize_game_state()

    def get_event(self, event):
        """
        Handles user input events, such as quitting the game or any other key events.
        This is executed before the update function.

        :param event: The event object representing a user action, such as a key press or quit action.
        """
        if event.type == pygame.QUIT:
            self.done = True

    def update(self, dt):
        """
        Handles the main game logic, including spawning enemies, detecting collisions, and updating
        the player, enemies, and score. This function is executed after get_event().

        :param dt: The time elapsed between the current and previous frame, used for continuous movement.
        """

        # Update Sprites for continuous movement
        self.player.get_event()
        self.enemies.update(self.settings, self.score)

        ####TODO Challenge02: Spawn Dynamic Enemies
        if Enemy.no_enemies(enemies=self.enemies):
            self.player.bullets.empty()
            if self.player.level == 1:
                spawned_enemies = Enemy.spawn(
                    wave_length=self.wave_length,
                    rank=self.player.level,
                    image=self.preload_images[("enemy_1")],
                )
                self.enemies.add(*spawned_enemies)
            else:
                rand_num = random.randint(3,self.wave_length)
                spawned_weak_enemies = Enemy.spawn(
                    wave_length=rand_num,
                    rank=self.player.level,
                    image=self.preload_images[(f"enemy_{self.player.level}")],
                )
                self.enemies.add(*spawned_weak_enemies)
                spawned_strong_enemies = Enemy.spawn(
                    wave_length=self.wave_length-rand_num,
                    rank=self.player.level+1,
                    image=self.preload_images[(f"enemy_{self.player.level+1}")],
                )
                self.enemies.add(*spawned_strong_enemies)


        # TODO Challenge06: Spawn Boss after level 10

        # Handle enemy-bullet collision
        enemy_hit_map = pygame.sprite.groupcollide(
            self.enemies, self.player.bullets, False, True
        )
        #### TODO Challenge Task01: Increase Score
        if enemy_hit_map:
            for enemy in enemy_hit_map:
                enemy_rank = enemy.handle_enemy_hit()
            if Enemy.no_enemies(enemies=self.enemies):
                self.player.bullets.empty()

        # Increase Player Level after reaching a certain score
        if int(self.score.value) >= 1000 * self.player.level:

            self.player.upgrade_level()
            if self.wave_length <= self.max_wave_length:
                self.wave_length += 3

        # Handle enemy-player collision
        player_hit_map = pygame.sprite.spritecollide(self.player, self.enemies, True)
        if player_hit_map:
            self.player.take_life()
            # Update life icons using the Life class's update method
            Life.update_lives_group(
                self.lives,
                self.player.lives,
                self.settings.get("images").get("life_image_path"),
            )

        ###TODO: Challenge 06 Handle Player-BossBullet Collision

        ###TODO: Challenge 06 endgame after Boss dead
        # TODO: Comment this out when you reach Challenge 06
        # if self.boss.dead:
        #     self.settings.get("tracking_utilis").update(
        #         {"score": int(self.score.value)}
        #     )
        #     self.manager.update_entry("score", self.score.value)

        # Check if player is defeated
        if self.player.lives <= 0:
            self.settings.get("tracking_utilis").update(
                {"score": int(self.score.value)}
            )

            self.manager.update_entry("score", self.score.value)
            self.done = True
            self.next = "game_over_screen"

        # Draw everything
        self.draw()

    def draw(self):
        """
        Draws all the game elements, including the player, enemies, bullets, lives, and score.
        :return: int
        """
        self.screen.fill("black")

        score_text, score_rect = self.score.make_text(message=str(self.score.value))

        self.score.draw(score_text, score_rect)
        self.enemies.draw(self.screen)
        self.player.bullets.draw(self.screen)
        self.lives.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)

        display_level(
            self.player.level,
            self.screen,
            self.settings.get("fonts").get("font_path"),
            self.settings.get("fonts").get("font_size_initial"),
        )
        ###TODO Challenge06 : Draw Boss Healthbar and bullets

        return self.score
