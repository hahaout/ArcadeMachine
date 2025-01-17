import pygame


class Score(pygame.font.Font):
    """
    Tracking the live-score
    """

    def __init__(self, screen, name, size, start_score):
        """
        Tracking the score reached by the player.
        Subclass of pygame.font.Font
        :param name: Font Path
        :param size: Font Size

        """
        # Inherited from super class
        super().__init__(name, size)
        self.font_path = name
        self.font_size_score = size
        self.screen = screen
        self.value = start_score
        self.font = pygame.font.Font(self.font_path, self.font_size_score)

    def make_text(self, message, color="white", pos=(10, 40)):
        """
        Convert score to text drawable to the screen by using given Font-object and create a rectangle containing the text.
        :param message: Text to be rendered
        :param color: Text Color
        :param pos: Screen Position
        :return: message text and its rectangle
        """
        font = pygame.font.Font(self.font_path, self.font_size_score)
        text = font.render(message, False, color)
        text_rect = text.get_rect(topleft=pos)
        return text, text_rect

    def draw(self, score, score_rect):
        """
        Draw the score on the screen.
        :param score: Score text to be rendered to screen
        :param score_rect: Score text rectangle
        """
        self.screen.blit(score, score_rect)

    # TODO Challenge03: Increase Score
    def increase_score(self, enemy_rank):
        """
        Calculate Points for killed enemies
          - this function will be called in the main gameplay state to implement scoring logic

        """
        self.score.value += 100 * enemy_rank


    # TODO Challenge03: Define decrease_score(parameters) here
