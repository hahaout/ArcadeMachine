# **Space Invaders Challenges**

We prepared for you a simple modified version of the classic Space Invaders game using Python and the Pygame library.\
But the game isn't finished yet, there are still some features missing.\
In order to implement these features you'll have to face some challenges.

These challenges have different difficulties. You can start with whichever one your team wants. However, beware that some pieces will not function properly without the other.\
Besides the difficulty we estimated the time that you might need to complete the challenge.\
There's also a short explanation about the specific challenge in the dropdown.

The basic challenges are marked inside the code with a comment. Use `str + f` and search for task 1-4 to find them.\
Further information about the given code can be found in the README.

## Example Demo

Here's an example of how the Space Invaders game might look like in the end.

[![Space Invaders Demo](https://img.youtube.com/vi/5hSqtYqUNSY/0.jpg)](https://www.youtube.com/watch?v=5hSqtYqUNSY)

## Helpful resources

Here are some resource that may help you to cope with the challenges.

- [Pygame Documentation Front Page](https://www.pygame.org/docs/)
- [Collection of Pygame Tutorials from pygame.org](https://www.pygame.org/wiki/tutorials)
- [In depth Pygame Tutorial from coderslegacy.com](https://coderslegacy.com/python/python-pygame-tutorial/)
- [Python tutorial about classes](https://docs.python.org/3/tutorial/classes.html)
- [W3schools tutorial about classes](https://www.w3schools.com/python/python_classes.asp)
- [Geeksforgeeks tutorial about classes and objects](https://www.geeksforgeeks.org/python-classes-and-objects/)
- [Python Time Library for e.g. measuring time](https://docs.python.org/3/library/random.html)
- [GitHub repo for the scores](https://github.com/simon1573/Roadrunner/blob/master/leaderboard.py)

---

## Challenges

### Challenge 1: Moving and Shooting
**Difficulty:** ⭐
#### Learning Goals:
This challenge aims to practice `Conditions`, `Array-Selection using key indexes`, some `Game-logic` and give you a quick start in `Object-Oriented Programming`. You will learn how to `Create a new Object` from a pre-defined class and understand and use `attributes`.

#### Story:
You can't fight back, and the Earth is doomed. Save the Earth by sending a strong warrior to fight on behalf of humanity.
Finish the Player class. Fight For All That's Beautiful In The World.

<details>
<summary>Challenge Tasks: Implementing Player Control</summary>

### Task 1: Implement Player Movement
- Open `player.py` and locate the `Player` class, a `Sprite` class representing the player.
- Find the `get_event()` method.
- Modify `get_event()` to handle player movement using arrow keys:
  - **Left:** `pygame.K_LEFT`
  - **Right:** `pygame.K_RIGHT`
  - **Up:** `pygame.K_UP`
  - **Down:** `pygame.K_DOWN`.

### Task 2: Implement Player Shooting
- Within the `Player` class, find the `shoot()` method.
- Implement the `shoot()` method to fire bullets at enemies.
- Update `get_event()` to handle shooting when the space key (`pygame.K_SPACE`) is pressed.

</details>

<details>
<summary>Hint: Pygame getting key presses</summary>

- Use `pygame.key.get_pressed()` to get the state of all keys:
  - It returns a list of booleans, where `True` indicates a key is pressed.
  - Example: `[False, False, True, ...]`.
  - Use predefined constants for key detection:
  - `pygame.K_LEFT`, `pygame.K_RIGHT`, etc.
  ```python
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    # move left
  ```

</details>

<details><summary>Hint: accessing Class attributes</summary>

- Access class-specific attributes using the `self` keyword.
  ```python
  class user:
    def __init__(self, name, age):
    # Class attributes
        self.name = name
        self.age = age

    def change_name(self, new_name):
  # Using `self` to change name to the new name
        self.name = new_name
  ```
  </details>


<details> <summary>Hint: Movement Conditions</summary>

- Use `if-elif` conditions to detect specific key presses.
- Move the player only if:
  1. The corresponding key is pressed.
  2. The movement keeps the player within screen boundaries(edges).
    - left player edge is on the right of the left screen edge(left player edge > 0)
    - right player edge is on the left of right screen edge(right player edge < screen width)
    - same for top and bottom
</details>

<details><summary>Hint: getting screen boundaries</summary>

- use the `settings` to get constants from our `config.py` where the dictionary with all constants is defined
```python
    screen_width = settings.get("general").get("window_width")
    screen_hight = settings.get("general").get("window_hight")
```

</details>
<details><summary>Hint: Accessing and changing player position</summary>

- player position is saved in a rectangle which is a built in pygame property, to access it use the `self` as mentioned before:
```python
  player_position_x = self.rect.x
  player_position_y = self.rect.y
  player_right_edge = self.rect.right
  player_left_edge = self.rect.left
  player_top_edge = self.rect.top
  player_bottom_edge = self.rect.bottom
  ```

```python
new_position_x = old_position_x + player_speed_x
new_position_y = old_position_y + player_speed_y
  ```

</details>

<details>

<summary>Hint: Player Shooting, Getting current time using pygame</summary>

- Use `pygame.time.get_ticks()` to track the current game time in milliseconds.
  ```python

    current_time = pygame.time.get_ticks()
  ```
</details>


<details><summary>Hint: Creating a new Bullet object</summary>

- Refer to the `Bullet` class in `bullet.py` to understand its attributes and behavior.
- Use the class constructor (`__init__()`) to create new bullet objects:
  ```python
  bullet = Bullet((x, y), speed, image_path, sound_path)
  ```
</details>

<details><summary>Hint: Shooting conditions and smaller hints</summary>

- only shoot after cooldown is finished:
  ```python
    if current_time - self.last_shot_time >= self.shoot_cooldown:
    # create a new bullet object
    ```
- dont forget to update the last shot time when a new bullet is shot.

</details>

<details><summary>Hint: adding bullet sprites to a sprite group</summary>
- Ensure all new bullets are added to the player's `bullets` group:

```python
  mySprites.add(x)
  ```

  ```python
  self.bullets.add(bullet)
  ```
</details>

---

### Challenge 2: Dynamic Enemies
**Difficulty:** ⭐⭐⭐

#### Learning Goals:
This challenge helps you understand `function behavior with different input`, `Class attributes`, `Constructors and the __init__()`, and practice `conditions` for different situations depending on the desired behavior.

#### Story:
"It’s time to kick ass and chew bubble gum…and I’m all outta gum."
Enemies started to fear you. They called for backup, and now they have a whole army of different ranks.

<details>
<summary>Challenge Tasks: Implementing Different Types of Enemies Depending on Player Level</summary>

### Task 1: Dynamic Enemy Rank
- Ensure the enemy rank matches the player's level to increase difficulty as the player progresses.
  - Navigate to `enemy.py` and look at the `__init__()` function in the `Enemy` class to understand how an enemy object is created.
  - In `space_invaders.py`, analyze the `update()` function. Why are enemies always `rank 1`? Identify the hardcoded logic and modify the call to `spawn()` so it spawns enemies based on `self.player.level`.

### Task 2: Health Scaling
- Make higher-ranked enemies harder to kill by increasing their health.
  - Review the health logic in the `Enemy` class `__init__()` and adjust it so that health scales with `rank`.

### Task 3: Mixed Enemy Waves
- Divide waves into weaker and stronger enemies starting from `player.level >= 2`.

  **Task 3.1: Spawn Weaker Enemies**
  - Spawn a random number of `weaker enemies` (3 to wave_length) using the `player's current level` as their `rank`.

  **Task 3.2: Spawn Stronger Enemies**
  - For the `remaining wave length`, spawn `stronger enemies` `(rank = player.level + 1)`.

  **Task 3.3: Add Enemies to Sprite Group**
  - Add both sets of enemies to `self.enemies`.

  **Task 3.4: Choosing Images**
  - Enemy images are stored in a dictionary in `config.py`. Use `f-strings` like `f"enemy_{rank}"` to dynamically select the correct image based on rank.

</details>

<details>
<summary>Hint: Using `Enemy.no_enemies()`</summary>

- This is a `static method` that checks if there are any enemies left on the screen.
- It returns `True` if there are no enemies and `False` otherwise.
- Example:
  ```python
  if Enemy.no_enemies(enemies=self.enemies):
      # Logic to spawn new enemies
  ```

</details>

<details>
<summary>Hint: Handling the `enemies` Sprite Group</summary>

- `SpaceInvaders` has an attribute `enemies`, which is a `Sprite Group`.
- A `Sprite Group` is used to manage and handle all sprites inside it, making it easier to draw them or check if the group is empty.
- To add a single sprite `x` to a group `mySprites`:
  ```python
  mySprites.add(x)
  ```
  - In this case, use `self.enemies.add(x)` to add an enemy sprite.
- To add all elements of a list `myList` to a sprite group:
  ```python
  mySprites.add(*myList)
  ```

</details>

<details>
<summary>Hint: Checking Player Level</summary>

- Use `if` conditions to check if the player has reached level 2 or higher:
  ```python
  if self.player.level >= 2:
      # Logic for spawning stronger enemies
  ```

</details>

<details>
<summary>Hint: Using `f-strings` for Enemy Images</summary>

- `f-strings` can dynamically manipulate strings to determine which enemy image to use.
- Example:
  ```python
  level = 2
  image = f"enemy_{level}"
  print(image)
  ```
  Output:
  ```
  enemy_2
  ```

</details>

<details>
<summary>Hint: Spawning Weaker and Stronger Enemies</summary>

- **Weaker Enemies:** Use the player level as their rank.
  ```python
  weak_enemies = Enemy.spawn(
      wave_length=random.randrange(3, self.wave_length + 1),
      rank=self.player.level,
      image=self.preload_images[f"enemy_{self.player.level}"]
  )
  ```

- **Stronger Enemies:** Use a rank one level higher than the player level.
  ```python
  strong_enemies = Enemy.spawn(
      wave_length=(self.max_wave_length - len(weak_enemies)),
      rank=self.player.level + 1,
      image=self.preload_images[f"enemy_{self.player.level + 1}"]
  )
  ```

- **Randomizing Weaker Enemy Count**
  - Use `random.randrange(start, end)` to generate a random number of weaker enemies.
  - Example:
    ```python
    num_weak_enemies = random.randrange(3, self.wave_length + 1)
    ```

</details>

---

### Challenge 3 Scoring System
**Difficulty:** ⭐⭐
#### Learning Goals:

In this Challenge you will furthermore work on `functions`, in addition to `up/down-casting` working with different `types`
and `data structures`, you will get more practice on `Object Orientated Programming`, and on general workflow
`using functions cross different modules`

#### Story:
The government decided to establish a training program for the future pilots. In order to show the best of the best you'll need a saving system. Complete the Score class.

<details>
<summary>Challenge Tasks: Implement a Scoring System</summary>

### Task01: Increase Score:
- Navigate to `score.py` take a look on the constructor `__init__()` get a general understanding how the `Score` class is built
  and which `attributes` it has.
- Implement the `increase_score()` to increase score every time an enemy is killed:
  - increase the current `score value` by `100 * killed enemy rank`
- Call the `increase_score()` function in `space_invaders.py` in the `update()` after an enemy is killed to increase player score

### Task02: Decrease Score:
- define and Implement the `decrease_score()` to increase score every time an enemy escapes without being killed:
  - decrease the current `score value` by `10 * enemy rank`
- Call the `decrease_score()` function in `enemy.py` in the `update()` after an enemy goes off the screen to decrease score

</details>
<details>
<summary>Hint: Check if enemy is dead using enemy attributes</summary>

- `Enemy` class has a Boolean `dead` which is set to `true` when an enemy is killed
</details>


<br>

---

### Challenge 4: Sorting Highscores
**Difficulty:** ⭐⭐⭐

#### Learning Goals:
In this challenge, you will practice:
- Working with `JSON data`.
- Implementing sorting algorithms manually `Bubble Sort`.
- Enhancing your skills with `data structures` like `lists` and `dictionaries`.
- Applying `for` loops and conditions to manipulate and process data.

#### Story:
Training pilots is a hard task. We want to find the best fighters to save us from the doom. However, we are missing a top score board and can't show it to others to brag. Damn :(
Help the participants to sort their scores and display the leaders on the leaderboard.

<details>
<summary>Challenge Tasks: Implement a Highscore Menu</summary>

### Task 1: Fetch and Process Scores
- Open the `JSONManager` class in `JSONManager.py`.
- take a look on `player_data.json` this where the scores are saved
- Locate the `get_highscores()` method. This method is responsible for retrieving and processing the scores.
- Implement the following logic:
  - Normalize the `score` field to ensure it is an integer and not a string.
  - Use `Bubble Sort` to sort the scores in descending order based on the `score` field.
  - Return only the top 3 scores.

### Task 2: Display Scores
- Modify the `ScoreScreen` class in `score_screen.py` to display the sorted high scores on the screen.
  - call your implemented `get_highscores()` function in the right place
  - delete the placeholder and remove the comments of the highscore displaying logic
  - fix naming and other minor issues that might appear

</details>

<details>
<summary>Hint: Implementing Bubble Sort</summary>

- Bubble Sort works by repeatedly comparing adjacent elements in the list and swapping them if they are in the wrong order.
- For sorting in descending order, larger scores should move toward the beginning of the list.
- Example Process:
  1. Compare the first two scores: If the first is smaller, swap them.
  2. Move to the next pair and repeat until the largest score is at the end of the list.
  3. Repeat the process for the rest of the list, excluding the already sorted elements.

- Pseudocode for Bubble Sort:
  ```python
  for i from 0 to n-1:
      for j from 0 to n-i-2:
          if current element < next element:
              swap them
  ```
</details>
<details>
<summary>Hint: Ensure that string scores are converted to integers before sorting</summary>

  ```python
  entry["score"] = int(score)
  ```
</details>

<details>
<summary>Hint: Surround with `try, except` if you get a Value Error when converting</summary>

```python
  try:
    # Convert logic
  except ValueError:
    # Handle Error or Pass
  ```
</details>

---

### Challenge 5 Implementing the Boss

**Difficulty:** ⭐⭐⭐⭐


#### Learning Goals:
In this challenge, you will practice:
- Understand object-oriented programming by working with `methods` and `attributes`.
- Understand `Classes` and `Inheritance`
- Enhance debugging skills by integrating new functionality into an existing game structure.


#### Story:

The enemies decided to create a special bigger, better, stronger ship which can shootback.


<details>
<summary> Challange Tasks: Finish the Boss class</summary>


### Task 1: Complete the Constructor
- Use the `super()` function to call the `Enemy` class constructor and initialize shared attributes.
- Add new attributes specific to the Boss:
  - `speed_x`: Controls horizontal movement.
  - `shoot_cooldown`: Limits shooting to one bullet every 1 second (`1000 ms`).
  - `last_shot_time`: Tracks the last time the boss fired a bullet.
  - `health`: Implements the health system based on the boss's rank.

### Task 2: Implement Methods to Define Boss Behavior
- **`move()`**: Handle horizontal movement, reversing direction when the boss hits screen edges.
- **`shoot()`**: Allow the boss to fire bullets at regular intervals controlled by `shoot_cooldown`.
- **`update()`**: Combine all behaviors by calling `move()` and `shoot()`, and updating the bullets.

</details>

<details>
<summary>Hint: super class constructor</summary>


- Use the `super()` function to initialize the parent class attributes:
```python
class ParentClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```
```python
class ChildClass(ParentClass):
    def __init__(self, param1, param2, param3):
        super().__init__(param1, param2)  # Initialize parent class
        self.param3 = param3  # Add child-specific attributes
```
</details>

<details><summary>Hint:  Adding Instance Attributes</summary>

- Use `self` to define and access instance-specific attributes:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "pet"
```
</details>

<details><summary>Hint: Implementing Movement(Reverse direction when hitting screen edges)</summary>

```python
if self.rect.left <= 0 or self.rect.right >= screen_width:
    self.speed_x *= -1
```


</details>

<details><summary>Hint: Implementing Shooting(Use a cooldown timer to limit firing rate)</summary>

```python
    # Check timing and update last shot timer
if current_time - self.last_shot_time >= self.shoot_cooldown:
    self.last_shot_time = current_time
    # Create and fire a bullet

```

</details>

<details> <summary>Hint: Combining Behaviors</summary>

- Use the `update()` method to combine movement, shooting, and bullet updates:
<br>
</details>

<details> <summary>Hint: `Overriding` Parent Class methods:</summary>

- when `overriding` Parent Class Methods like: `move()` and `update()` in this case, remember to have the same parameters in both `Parent and Child classes`
</details>

---

### Challenge 6 Applying Game Logic to Implement the Boss

**Difficulty:** ⭐⭐⭐⭐⭐

#### Learning Goals:

In this challenge, you will practice:
- Debugging and finding errors
- Adapting existing Code to new features

and learn:
- pygame collision handeling
- pygame drawing

#### Story:
Now that the Boss ship is built, we want it to come to life in the game.
your final challenge is to update the game logic to make the boss ship appear for a final battle

<details>
<summary>Challenge Tasks: Update the main gameplay state to make the final boss appear after reaching level 10</summary>

### Task 1: Spawn the Boss:
- add a `boss` attribute in `space_invaders.py` and give it a default value of `None`
- in the `update()` create a boss object after reaching a specific level if it doesn't already exist
- update the `draw()` function in `space_invaders.py` to draw the boss health-bar and bullets

### Task 2: Debug and fix
- you may notice now that the Boss is shooting Bullets but in the wrong direction
- update the `Bullet` class in `bullets.py` to make bullets adapt to player/boss bullets behaviour
- Check for other errors/unexpected behaviour from the boss and fix them if they exist

### Task 3 Bullets hitting player:

- if boss exists: check for collisions between player sprite and boss bullet
- `kill()` every bullet that hits the player
- everytime a bullet hits the player, the player loses a life
- update player lives

### Task 4 Game Over after Boss is defeated

- set the gameplay state to `done`
- set the next state to ` "game_over_screen" `

</details>

<details>
    <summary>Hint: Spawning The Boss general hints</summary>

- to make testing easier, try first to spawn the boss after reaching level 2 or at the start of the game
- make sure there are no other enemies on the screen `Enemy.no_enemies()`
- don't forget to add the boss to the enemy sprite group so it could be drawn to the screen
- Python is sensitve to where you write your code think of when should the Boss spawn/what conditions should be satisfied to know where to implement your logic
- 90% of the task is figuring out when should the `Boss` object be created

</details>

<details><summary>Hint: Boss Position</summary>

- `pos` is a tuple `(x, y)`, you can choose any `x` between `(50,750)` as for `y` its better to stick to `100`
</details>

<details><summary>Hint: Updating Bullet class</summary>

now the direction of the bullet is hardcoded in the `update()` of the `Bullet` class
```python
    self.rect.y -= self.speed  # Move bullet upwards
    if self.rect.top > pygame.display.get_surface().get_height():  # Kill bullet when it goes over the screen border
```
- find a way to make it move upwards and downwards
- maybe add a new `direction` attribute to the class and give it values `1` or `-1` depending on wanted direction?
- `-1 * current direction = opposite direction `
- what happens if bullet goes below screen borders?

</details>

<details><summary>Hint: Handle Player getting hit by a Bullet</summary>

- Remember Boss Bullets only exist if boss exists
- pygame offers `rect.colliderect()` to handle `rect-collisions`
```python
if self.player.rect.colliderect(bullet.rect):
  # Handle Collision
```
</details>

<details><summary>Hint: sprite.kill() </summary>

- The kill() function removes a sprite from all sprite groups it is in
- in easier words in our case: the sprite will not be drawn, if its drawn it will be deleted from the screen

```python
bullet.kill()
```

</details>

<details><summary>Hint: Updating Player Lives:</summary>

- step_1 : player loses a life(use a function from the `Player` class)
- step_2 :

```python
 Life.update_lives_group(
                        self.lives,
                        self.player.lives,
                        self.settings.get("images").get("life_image_path"),
                    )
```

</details>



<br>


---

## Advanced Bonus Challenges

You have successfully established the defence training program for Your fellow pilots.\
However, if you want to further improve your game or code and make it more interesting, these challenges are for you.


<details>
<summary>Animation of Enemy Explosion</summary>

The game doesn't feel epic enough. We need explosions. Go ka-Boom.

- Add an explosion at the position of the enemy when it dies. The required assets are defined in the SpaceInvaders class.
- Add the explosion sounds.

</details>


<details>
<summary>Obstacle Appearance</summary>

Need to take a breath from the boss shooting back? Hide. Use random meteorites for shelter.

- Add an obstacle that blocks the bullets but can be destroyed by bullets.

</details>

<details>
<summary>Game Background</summary>

Take the fight into outer space

- draw a moving backround behind the game play to make your ship fly in the endless cosmos

</details>
