config = {
    # General Settings
    "general": {
        "window_width": 800,
        "window_height": 700,
        "fps": 60,
        "shoot_cooldown": 300,
    },
    # Fonts
    "fonts": {
        "font_path": "games/space_invaders/assets/font/ArcadeClassic.ttf",
        "font_size_large": 36,
        "font_size_small": 20,
        "font_size_initial": 12,
        "font_size_score": 30,
    },
    # Texts
    "texts": {
        "game_over_text": "Game Over",
        "username_text": "Username: ",
        "score_text": "Score: ",
        "enter_username": "Enter your name",
        "continue_text": "Press Enter to play again",
        "highscore_text": "Press Space to see highscores",
        "start_text": "Press <Enter> to start the game",
        "exit_text": "Press Esc to Exit",
    },
    # Images
    "images": {
        "background_image_path": "games/space_invaders/assets/graphics/Space_Sprites/Space_1.png",
        "bullet_image_path": "games/space_invaders/assets/graphics/bullet.png",
        "life_image_path": "games/space_invaders/assets/graphics/heart16.png",
        "enemy_sheet_path": "games/space_invaders/assets/graphics/enemy_sheet.png",
        "explosions_sheet_path": "games/space_invaders/assets/graphics/PC_Computer_Spelunky_Classic_Explosion.png",
        "player_image_path": "games/space_invaders/assets/graphics/ship1.png",
    },
    # Sounds
    "sounds": {
        "game_over_sound_path": "games/space_invaders/assets/audio/gameover.mp3",
        "bullet_sound_path": "games/space_invaders/assets/audio/laser1.mp3",
        "explosion_sound_path": "games/space_invaders/assets/audio/hit.mp3",
        "life_sound_path": "games/space_invaders/assets/audio/add_life.mp3",
    },
    # Enemy Attributes
    "enemy_attributes": {"enemy_speed_y": 0.75, "normal_enemy_scale": (50, 50)},
    # Enemy Coordinates from Spritesheet (x, y, x + offset, y + offset)
    "enemy_coordinates": {
        "enemy_1": (939, 7, 318, 282),
        "enemy_2": (1300, 7, 300, 232),
        "enemy_3": (1700, 7, 349, 290),
        "enemy_4": (945, 436, 294, 350),
        "enemy_5": (1300, 436, 315, 320),
        "enemy_6": (1700, 436, 331, 326),
        "enemy_7": (1120, 896, 361, 385),
        "enemy_8": (1565, 883, 315, 377),
        "enemy_9": (632, 1343, 568, 553),
        "enemy_10": (1267, 1417, 593, 438),
        "enemy_11": (1996, 1323, 507, 565),
        "enemy_12": (513, 2023, 724, 1166),
        "enemy_13": (1329, 2030, 708, 1263),
        "enemy_14": (2078, 2046, 605, 1060),
        "enemy_15": (0, 3369, 1638, 1266),
        "boss_enemy": (1755, 3379, 1245, 1344),
    },
    # Explosion Animation
    "explosion_animation_frames": [
        (72, 3, 110 - 72, 45 - 3),
        (113, 3, 160 - 113, 45 - 3),
        (164, 3, 197 - 164, 45 - 3),
        (201, 3, 238 - 201, 45 - 3),
        (242, 3, 283 - 242, 45 - 3),
        (287, 3, 329 - 287, 45 - 3),
        (333, 3, 364 - 333, 45 - 3),
        (368, 3, 393 - 368, 45 - 3),
    ],
    "tracking_utilis": {"score": 0, "username": ""},
}
