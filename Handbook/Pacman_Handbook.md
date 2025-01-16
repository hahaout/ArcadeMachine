# Pacman handbook

<img src="images/codealone.png" alt="Alternativtext" style="width:30%; height:auto;">

In this handbook you'll learn base understanding and overview of the code you'll work with during the hackathon.

This Handbook is for the **Pacman** Game.


## <img src="images/introduction.png" alt="Alternativtext" style="width:auto; height:auto;">
<img src="images/pygamelogo.png" alt="Alternativtext" style="width:30%; height:auto;">

#### **What is Pygame?**



Pygame is a library designed for creating video games and multimedia applications in python. <br>
It provides modules and tools that simplify game development by handling many low-level tasks like rendering <br>
graphics, playing sounds, and processing input from devices like keyboards, mice, or game controllers.<br>
<br>
For a introduction in Pygame and some beginner tutorials we recommend reading the Pygames tutorial you can find in gitlab. :)


<img src="images/pacmanlogo.png" alt="Alternativtext" style="width:30%; height:auto;">

#### **Game Rules and Goals**

Pacman is a classic arcade game where the player controls a yellow circular character, "Pacman", navigating a maze while avoiding ghosts.<br> The goal is to eat all the dots in the maze to advance to the next level. <br>
<br>
The four ghosts "Blinky", "Pinky", "Inky" and "Clyde" patrol the maze, trying to catch Pacman.<br><br>
Blinky is a bit aggressive and chases Pacman directly.<br>
Pinky is more sneaky and tries to ambush Pacman. <br>
Inky is a bit special and is often disoriented in the maze. He combines randomnes with calculated movement.<br>
Clyde is a moody ghost. Sometimes he chases Pacman and sometimes he just wanders around aimlessly.<br><br>
When Pacman eats an **"Energizer"**(the bigger dots), he temporarily receive the power to eat the ghosts.<br>
Because they are ghosts, they will respawn in the ghost house, trying to catch Pacman again.<br>
Also, periodically, there'll appear fruits in the maze, which'll grant extra points when eaten.   

## <img src="images/ProjectOverview.png" alt="Alternativtext" style="width:auto; height:auto;">

The hackathon Pacman game consists of **14 python files** and a **text file** which contains the highscore.<br>
Also, there are two markdown files. One explaining your hackathon challenges and and a readme file, which contains a **summary** <br>
over the game files and some other noteworthy stuff. Read it to have a better overview of the files before you begin with the challenges. :)<br>
<br>
The ressources like sprites and sounds are organized in folders each with the same name.
<br>

* `Character.py`: Class for all kinds of characters. This file defines a average character class, which is used to model various core functionalities like position, movement and rendering of characters. 
<br>
This class is used by Pacman and the ghosts!
<br>

* `CharacterMode.py`: For moving sprites. This class holds all variables that belong to a character mode (like ghosts are scared or hunting).
<br>

* `Fruit.py`: Class for fruits.
<br>

* `game_constants.py`: Constants. Defines core constants and configurations of the game like screen dimensions and the direction constant,
<br> 
which defines possible movement directions and their effect on the position. 
<br>
These constants are essential for important game files like Pacman.py and MainGame.py

* `game_grid.py`: Grid that overlays the maze picture. We have a one dimensional array as a grid but for a lot of
functionality we map those indices to world coordinates (x-/y-coordinates).
<br>

* `Ghost.py`: Inherits all functionalities from the character class file and adds unique behaviors and the ghosts movement logic and strategy. 
<br>

* `high_score.txt`: Saves highscore.
<br>

* `load_image.py`: Contains a function to load the sprites from a specified path and converts them to a format compatible to Pygame's rendering system.
<br>

* `main.py`: Runs the game. See next chapter.
<br>

* `MainGame.py`: Manages main elements of the game. see next chapter.
<br>

* `MovableSprite.py`: Contains a function, that splits the sprite sheets to individual frames to use in animations. The class represents a game object that can move and display different frames.
<br>
Pacman and the ghosts inherit from this file so they can be animated. 
<br>

* `Pacman.py`: Same to the ghosts file, this file inherits from the character class file and includes movement logic, input handling and state handling (e.g. dead or alive) for Pacman.
<br>

* `Pill.py`: Defines the behavior and appearance of a pill in the game and differentiate between a normal pill and an energizer.
<br>

* `PillManager.py`: Spawns and removes pills. Manages all the pills and energizers within the game, including their initialization, tracking, and the action of Pacman eating them.
<br>

* `Scoring.py`: Manages points.
<br>

* `sprites (folder)`: Images for the game elements.


## <img src="images/HowDoesTheGameWork.png" alt="Alternativtext" style="width:auto; height:auto;">

As you have may have already seen, the code of the game is written in a object-oriented way. For Python beginners this could be a little hard to understand.<br>
<br>
Object-oriented programming (OOP) is necessary for a game, because it helps organizing the game into logical, reusable components.<br>
With this approach Pacman is represented in key elements like Pacman, the ghosts, the maze, the game logic and so on **as classes** and their behavior as **methods**.<br>
<br>
To create an easier entry into the challenge this handbook provides some simple explanations of the code you'll be working with.

1. **The main game files**

Especially in bigger projects it's common to divide the initiating file from the remaining logic. In the Pacman game the _main.py_ file is the entry point for the game, which imports the functionality of the _MainGame.py_ file, which contains the game logic. 
<br>
This provides a better overview, readability and maintaining of the code. Furthermore it separates the responsibilities of both files.
<br>
<br>
On the base of this, the Pacman game is divided in many files. They're communicating on the base of importing other files, variables and functions.
<br>
**E.g.:**<br>
```python3
from pygame import Surface
from Ghost import init_ghosts
from Pacman import Pacman
from Scoring import Scoring
from game_constants import WIDTH, HEIGHT, TOP_OFFSET, TIME_BETWEEN_ANIMATIONS
from load_image import load_image
from PillManager import PillManager
from sounds import background_sfx
```

2. **Game Logic**
<br>

The game logic is responsible for game states and coordination of game behaviour in specific situations. 
<br><br>
`game_run`: The heart of the game. This is the main loop which continously processes the logic, player movement and rendering.
<br><br>
`move_characters`: Movement logic for Pacman and the ghosts. Calls it specifically for every character.
<br><br>
`check_collisions`: As the name suggests, this function checks, if Pacman or the ghosts are colliding with a pill, fruit, other character or a wall. <br>Behavior depends on the games rules. (E.g. Pacman dies, ghosts are scared etc.)
<br><br>
`ghost_collison`: Is the logic for the collision between Pacman and a ghost. Depending on the game state it adds points and lets the ghost die or it lets Pacman die.
<br><br>
`reset`: Resets back to the beginning state.
<br><br>
`game_over`: Setting the state *is_game_over* and shows the game-over-screen. 

3. **Event Handling**

The event handling reacts to user inputs like key-pressing or the closing of the game window.
<br><br>
`handle_events`: Checks for all events the game delivers and sends them directly to the *handle_event* method.
<br><br>
`handle_event`: Reacts to specific events. E.g. *pygame.QUIT* ending the game or *pygame.KEYDOWN* for the controls.
<br>

4. **Rendering**
<br>

The rendering part of the game is responsible to bring all grafical illustrations on your screen, including the background, the characters,<br>
the animation frames etc. 
<br><br>
`draw_frame`: The main function for rendering. Draws all the sprites on the screen and updates it to display the current states.
<br><br>
`handle_animations`: Animates Pacman and the ghosts at regular intervalls based on *TIME_BETWEEN_ANIMATIONS*.
<br><br>
`init_backgrounds`: Loads the background picture and saves it for Re-use. 
<br><br><br>
**For more Pygame specific explanations be sure to check out the Pygame tutorial in Gitlab!** 

## <img src="images/OOStructure.png" alt="Alternativtext" style="width:auto; height:auto;">
####  Objects
In object-oriented programming a group of related variables and functions get combined in Units. This is called the **object**.<br>
In Python, objects are instances of a class, so you need to create a class in order to create an object. <br>
A class is basically a "Blueprint" of specific objects. 

To create a class you need to use the keyword `class`. You can already assign properties to the class and create an object.
<br>
Python has a built in function called `__init()__` to assign values to object properties.
<br>
To make the object to something more than just a data-container, you can define `methods` which define functionalities based on its variables.
<br>
Methods encapsulate specific logic and behavior of a class and its instances. Similiar to the initiation function, you need to use `def` to define a method.
<br><br>
**Example of a simple object-oriented code:**
<details>
<summary>class example</summary>

```python3
class Dog:
    species = "Dog" #Class attribute -> General for all instances
    legs = 4

    def __init__(self, name, age):
        self.name = name #Instance attribute -> Specific and independent for every instance
        self.age = age

    def bark(self, times):
        return ("Bark!" * times)


d1 = Dog("Doggie", 36)

print(d1.name)  # Output: Doggie
print(d1.age)   # Output: 36
print(d1.species) # Output: Dog
print(d1.legs)  # Output: 4
print(d1.bark(4)) # Output: Bark!Bark!Bark!Bark!
```
</details>
<br>

The `self` parameter is used as a reference to the current instance. It is needed to access the variables and methods that belongs to the instance. 
<br> Without this parameter, Python wouldn't know how to divide between class and instance attributes!
<br>

Pacman uses classes for objects like the ghosts or Pacman self, but also for items like the pill and functionalities like the pill-manager.

<details>
<summary>Show code example</summary>

```Python3
from CharacterMode import CharacterMode
from game_constants import DIRECTIONS, COLUMN_COUNT, RIGHT, NONE
from game_grid import map_coordinates_to_index, map_index_to_coordinates, game_grid
from MovableSprite import MovableSprite

class Character:

    def __init__(self, name, pos, sprite: MovableSprite):
        self.sprite = sprite
        self.name = name

        # Starting position
        self.x, self.y = pos
        self.grid_index = map_coordinates_to_index(self.x, self.y)

        # Starting direction
        self.direction = RIGHT
        self.directX, self.directY = DIRECTIONS[self.direction]

        self.cur_animation_frame = 0

    def show(self, sprite_group):
        sprite_group.add(self.sprite)

    def move(self):
        # adjust the x and y based on the current direction
        self.x += self.directX
        self.y += self.directY
        # update the grid index, so it fits the current x and y
        self.grid_index = map_coordinates_to_index(self.x, self.y)
        self.sprite.move(self.x, self.y, True)

    !MORE CODE IN GAME FILE!

``` 
</details>


<br>


<br>
In this code example, you can see how the structure is similar to the example program, but slightly more complicated. Try to familiarise yourself 
with the code and its functions and methods and work your way through the challenges. If you need help, don't hesitate to use the **Pygame tutorial** 
or ask someone for support. We hope you enjoy the challenges!
<br>


