from abc import abstractmethod


class States(object):
    """
    Abstract base class for defining game states in the state-/game-machine architecture.

    The `States` class provides a standardized framework for implementing various game states (e.g., menu screens,
    gameplay, game over screens) within a game. Each state represents a distinct phase or view in the game, such as
    the start screen, the game itself, or the score screen.

    ### Purpose:
    - To manage the transition between different states in a controlled manner.
    - To encapsulate logic and rendering specific to each state, keeping the overall game structure organized.

    ### Abstract Nature:
    This class is designed as an abstract base class, meaning it defines the required structure and methods that all
    derived states must implement. This ensures that all states adhere to a common interface, which is critical for
    seamless state transitions and consistent game behavior.

    ### Key Attributes:
    - `done`: A boolean flag to indicate when the current state is finished and needs to transition to another state.
    - `next`: A reference to the next state to be displayed.
    - `quit`: A boolean flag to signal exiting the application.
    - `previous`: A reference to the previous state, useful for returning to earlier views.
    - `username`: Placeholder for storing user-related data if required by the state.
    - `screen`: The Pygame surface on which the state will render its visual elements.
    - `settings`: A dictionary of settings containing configuration data for the game.

    ### Abstract Methods:
    Derived classes must implement the following methods:
    - `startup()`: Initialize or reset any necessary state-specific variables.
    - `get_event(event)`: Handle user input events (e.g., key presses, mouse clicks).
    - `update(dt)`: Update the state logic, typically called every frame.
    - `draw(text, rect)`: Render visual elements to the screen.
    - `make_text(message, color, center, font_size, font_path)`: Utility for creating and positioning text elements.
    - `cleanup()`: Perform cleanup tasks when transitioning away from the state.

    By enforcing these methods, the `States` class ensures that all game states can be integrated into the overall
    game loop and interact with each other in a predictable manner.
    """

    def __init__(self, screen, settings):
        self.done = False  # running boolean to check if a view needs to be left to show another one
        self.next = None  # this will be the next shown view eg ScoreScreen
        self.quit = False  # leave application
        self.previous = None  # this is previous shown view
        self.username = None
        self.screen = screen
        self.settings = settings

    @abstractmethod
    def startup(self):
        pass

    @abstractmethod
    def get_event(self, event):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, text, rect):
        pass

    @abstractmethod
    def make_text(self, message, color, center, font_size, font_path):
        pass

    @abstractmethod
    def cleanup(self):
        pass
