import pygame as pg


class Control:
    """
    Control class that acts as the main driver for a game based on the state-machine concept.

    This class implements the principles of a state machine to handle transitions and execution
    between various game states (or screens), such as splash screens, menus, gameplay scenes, or
    credit screens. By encapsulating state logic, Control ensures a single unified main game loop
    and event handling mechanism, avoiding the complexity of multiple loops or scattered logic.

    Attributes:
        fps (int): Frames per second to control game update speed.
        state (States): The current active state of the game.
        state_name (str): The name of the currently active state.
        state_dict (dict): A dictionary mapping state names to their respective state objects.
        done (bool): A flag to indicate if the game loop should terminate.
        settings (dict): A dictionary of general settings passed during initialization.
        screen (pygame.Surface): The main display surface of the game.
        screen_rect (pygame.Rect): Rectangle representing the dimensions of the screen.
        clock (pygame.time.Clock): Pygame clock object to control frame timing.

    Methods:
        __init__(**settings): Initializes the Control object with settings.
        get_settings(): Returns the settings dictionary.
        get_screen(): Returns the pygame screen object.
        setup_states(state_dict, start_state): Configures the available game states and sets the initial state.
        flip_state(): Transitions to the next state as defined by the current state's `next` attribute.
        update(dt): Updates the active state, handling transitions and quit flags.
        event_loop(): Processes events, delegating handling to the current state.
        main_game_loop(): Executes the main game loop, coordinating events, updates, and screen rendering.
    """

    def __init__(self, **settings):
        """
        Initializes the Control object with provided settings.

        Args:
            **settings: Arbitrary keyword arguments containing game settings, such as screen dimensions
                        and general configurations.

        Raises:
            KeyError: If required settings such as `window_width` or `window_height` are missing.
        """
        self.fps = settings.get("fps", 60)
        self.state = None
        self.state_name = None
        self.state_dict = None
        self.__dict__.update(settings)
        self.done = False
        self.settings = settings

        # Initialize screen and other components.
        self.screen = pg.display.set_mode(
            (
                self.settings.get("general").get("window_width"),
                self.settings.get("general").get("window_height"),
            )
        )

        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()

        # TODO add score, username handling

    def get_settings(self):
        """
        Returns the current settings dictionary.

        Returns:
            dict: The settings dictionary.
        """
        return self.settings

    def get_screen(self):
        """
        Returns the main game screen surface.

        Returns:
            pygame.Surface: The display surface.
        """
        return self.screen

    def setup_states(self, state_dict, start_state):
        """
        Configures the available states and sets the initial state.

        Args:
            state_dict (dict): Dictionary mapping state names to state objects.
            start_state (str): The name of the state to initialize as the starting state.
        """
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        """
        Transitions from the current state to the next state.

        This method calls the cleanup method of the current state, updates the active state to
        the next one defined by the current state's `next` attribute, and invokes the startup
        method of the new state.
        """
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt):
        """
        Updates the current state and manages state transitions.

        Args:
            dt (float): The time elapsed since the last frame (delta time).
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def event_loop(self):
        """
        Processes events and delegates handling to the active state.

        This method checks for global events like quitting the game and forwards all events
        to the current state's event handling method.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        """
        Executes the main game loop, coordinating events, updates, and rendering.

        The loop continues until the `done` attribute is set to True, either by the user quitting
        or a state signaling the end of the game.
        """
        while not self.done:
            delta_time = self.clock.tick(self.fps) / 1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()
