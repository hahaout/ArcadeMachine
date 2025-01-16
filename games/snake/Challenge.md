## Snake Challenges
This game of snake is not much fun yet. It has so many missing parts. 
So let's make it as our challenge to complete the game.
Hopefully, at the end we will have a super cool snake game.
To keep track, we recommend you fix the game in the following steps.

**Please, mind the order.**

Most challenges are marked in the code with a comment.
Jus search for `CHALLENGE X` where X is the number of the challenge.

The `Main` challenges come with a solution.

The `Advanced Bonus Challenges` are voluntary work that you can do with the resulting code of the other challenges if you want
to.
---
## Helpful resources

Here are some resources that may help you to cope with the challenges.

- [Pygame Documentation Front Page](https://www.pygame.org/docs/)
- [Collection of Pygame Tutorials from pygame.org](https://www.pygame.org/wiki/tutorials)
- [In depth Pygame Tutorial from coderslegacy.com](https://coderslegacy.com/python/python-pygame-tutorial/)
- [Python tutorial about game development](https://www.pygame.org/wiki/tutorials)

---

## Challenges

### Challenge 1: Snake Movement

- **Difficulty**: ⭐⭐
- **Learning Goal**: Using `if-else` conditions to modify variables.
- **Task**: Within the main game loop, specify how the UP, DOWN, and LEFT directions affect the `snake_position` array. Currently, the snake does not respond to user key presses. Your task in this challenge is to specify the actions
triggered when a key is pressed. Upon completing this challenge,
the snake should be responsive to key presses, allowing for movement.

<details>
<summary>Hint 1</summary>
<p>You can use the already defined manipulation for the direction RIGHT as orientation.</p>
</details>

<details>
<summary>Hint 2</summary>
**Pygame Element:** `pygame.event.get()` and `pygame.draw.rect()`. To control the snake’s movement, you need to handle user input using `pygame.KEYDOWN` events. This example shows how to capture the arrow key presses and update the snake's position accordingly
You have to change the value of the direction variable.

The type of event you are going to be using is `pygame.KEYDOWN`
</details>

---

### Challenge 2: Feed the Snake, Implementing Fruit Spawning

- **Difficulty**: ⭐️⭐️⭐️
- **Learning Goal**: Using functions and generating random numbers with `random.randrange`.
- **Task**: the snake needs food! Spawn the first fruit for the snake by implementing the `generate_fruit_position` function

<details>
<summary>Hint 1</summary>
<p>Generate random fruit position within window boundaries, the generated position is going to be a tuple. 
</p></details>

<details>
<summary>Hint 2</summary>
<p>The randrange should be between 1 and (window_x // 10). 
</p></details>

<details>
<summary>Hint 3</summary>
<p>Ensure that the fruit spawns on a multiple of 10 to align with the snake's grid movement. Next: Generate the initial fruit position by calling the `generate_fruit_position` function.
</p></details>

<details>
<summary>Hint 4</summary>
<p>Ensure the first fruit is spawned using the boolean variable 'fruit_spawn'
</p></details>

---

### Challenge 3: Generate a new fruit position when the previous one is eaten

- **Difficulty**: ⭐️⭐️⭐️
- **Learning Goal**: Detecting collisions with conditions and boolean logic.
- **Task**: In the previous challenge we spawned the first fruit in the game window. 
Make a new fruit apper after this one is eaten and don't forget to increase the score.

<details>
<summary>Hint 1</summary>
<p>Increase `score` by 10 when the snake collides with the fruit. 
</p></details>

<details>
<summary>Hint 2</summary>
<p>Make the food disappear by changing the `fruit_spawn`value.  
</p></details>

<details>
<summary>Hint 3</summary>
<p>check with an if statement if a fruit is spawned 
if not then call the 'generate_fruit_position' function that you implemented in the previous challenge. 
</p></details>

<details>
<summary>Hint 4</summary>
<p>set 'fruit_spawn' back to true. 
</p>
</details>

---

### Challenge 4: Make sure the fruit doesn't spawn on the snakes body

- **Difficulty**: ⭐️⭐️⭐️⭐️
- **Learning Goal**: Using recursion and conditions to validate and regenerate positions.
- **task**: Oh no! The fruits are playing hide-and-seek with the snake!  
Your task is to continue implementing the function, `generate_fruit_position`, to make sure that the fruit doesn’t accidentally appear on the snake’s body. 
Use recursion to check if the fruit's position matches any part of the snake’s body and adjust it if needed. 
Let’s make the snake’s life a little easier, shall we?

<details>
<summary>Hint</summary>
<p> Call the function you implemented in challenge 3 again IF the position of the fruit is on the 'snake_body.'
</p>
</details>

---

### Challenge 5: Stay Inside the Arena!!

- **Difficulty**: ⭐️⭐️⭐️⭐️⭐️
- **Learning Goal**: Performing boundary checks with comparisons.
- **Task**: Keep the snake in its playground!! Implement the `check_boundary_collision` function to prevent the snake from escaping the game window. 
If the snake crosses the borders, it’s game over! 
Stay sharp and protect the edges of your world.


<details>
<summary>Hint 1</summary>
<p>Compare the snake's head position to the game window's boundaries (`window_x` and `window_y`). If the head position goes beyond these limits, end the game.
</p></details>


<details>
<summary>Hint 2</summary>
<p>This function should return a boolean value, it checks if the snake's head is outside the game window boundaries.
</p></details>

<details>
<summary>Hint 3</summary>
<p>Use if-else conditions to make sure the 'snake_position' is safe (not >= window_x or window_y)
</p></details>

<details>
<summary>Hint 4</summary>
<p>Don't forget to make the appropriate changes in the game loop!</p> 
</details>

---

### Challenge 6: Stay in One Piece!!

- **Difficulty**: ⭐️⭐️⭐️⭐️
- **Learning Goal**: Using list iteration and functions to detect self-collisions.
- **Task**: Oh no, the snake can run into itself!
Implement the `check_self_collision` function to ensure the snake doesn’t accidentally eat itself! 
If the snake’s head overlaps with any part of its body... well, that's game over! 

<details> 
<summary>Hint 1</summary>
<p>Implement the `check_self_collision` function to check if the snake's head matches any of its body parts (except the head itself).</p>
</details>

<details>
<summary>Hint 2</summary>
<p>If it does, it's time to call it quits! (this function should return a boolean value)
</p></details>

<details>
<summary>Hint 3</summary>
<p>Don't forget to make the function you implemented useful!</p> 
</details>

---

### Challenge 7: Game Over in Style!

- **Difficulty**: ⭐️⭐️⭐️⭐️
- **Learning Goal**: Rendering and aligning text with functions.
- **Task**: When the game ends, why just quit when you can go out in style?  
Your task is to create a Game Over screen that lets the player know they’ve done their best (or not so best).
Implement a `game_over` function to display the words "Game Over" in bold, red text on the screen (displaying the score would also be a good idea!). 
Make it appear centered, with a sleek black background. 

<details> 
<summary>Hint 1</summary>
<p> use for the font : ('Arial bold', 80).
</p></details>

<details>
<summary>Hint 2</summary>
<p>Do the rendering of the text and choose the color red defined in config.py. 
</p></details>

<details>
<summary>Hint 3</summary>
<p>Center the text and make sure the score test doesn't overlap with the game over text.
</p></details>

<details>
<summary>Hint 4</summary>
<p>Try : (window_x // 2, window_y // 2 -100), change the '-100' to adjust the vertical position.
</p></details> 

<details>
<summary>Hint 5</summary>
<p>Fill the background with black and blit (google blit to understand how it works).
Don't forget to use this function in the game loop! (instead of quitting immediately, call game over and break the loop).
</p></details>

---

### Challenge 8: High-score

- **Difficulty**: ⭐️⭐️⭐️⭐️⭐️  
- **Learning Goal**: Working with file operations (read/write) and comparing values.
- **Task**: Enhance the game by implementing a high-score tracking system!  

#### Objective 1: File Operations

Create functions to **read** and **write** the high score from/to a text file: 'filename'.  

<details>
<summary>Hint</summary>
<p>
These functions should handle reading the highest score from a file when the game starts and updating it when the player achieves a new high score. Use Python's built-in file handling (`open`, `read`, `write`) for this. 
</p>
</details>

#### Objective 2: High Score Logic  

Compare the **current score** with the **stored high score** from the file.  

<details>
<summary>Hint</summary>
<p>
If the current score is greater than the stored high score, update the high score in the file.  
Start by setting the first game's score as the initial high score.  
Use conditional statements to compare and update.
</p>
</details>

#### Objective 3: Display High Score on Game Over Screen  

Update the Game Over screen (Challenge 7) to show the **high score**. Align the text properly for a clean look!  

---

# Advanced Bonus Challenges

### Challenge 9: Pause the screen

- **Difficulty**: ⭐️⭐️⭐️⭐️⭐️
- **Learning Goal**: Managing state changes with boolean flags.
- **Task**: It's time to flex your programming muscles and create something awesome from scratch! 
Your mission (should you choose to accept it) is to implement a brand-new function that makes your Snake game even more user-friendly with a pause screen.

<details> 
<summary>Good to know!</summary> 
<p>
- Here's the plan:

- When the player presses 'P', the game should stop and display a stylish pause screen.
- The pause screen should include a clear message like "Game Paused. Press 'P' to Resume!".
- The game should stay paused until the player presses 'P' again, resuming gameplay exactly where they left off.
- Show creativity with fonts and colors! 
</p>
</details>

<details> 
<summary>Hint 1</summary> 
<p>
Create a new function 'pause_screen' with the following parameters: 'game_window', 'window_x', 'window_y', 'colors' in the part where the functions are implemented.
</p>
</details>

<details>
<summary>Hint 2</summary>
<p>
In this function, make sure to display a good text. You can use the font: 'Arial bold' and 50. Render a text that indicates that the game is paused and center it.
</p>
</details>

<details>
<summary>Hint 3</summary>
<p>
Display the pause screen by filling the background in black, rendering the pause text using 'blit'. Don't forget to refresh the screen.
</p>
</details>

<details>
<summary>Hint 4</summary>
<p>
Now comes the tricky part! You have to allow the user to unpause the screen. Create a boolean variable that ensures that the screen is paused.  
Create a loop that keeps checking the event type 'KEYDOWN' and if 'P' is pressed, the boolean value changes (similar to what you did in Challenge 2 with the event handling).
</p>
</details>


<details>
<summary>Hint 5</summary>
<p>
Call your function in the Game Loop (in the event handling part).
</p>
</details>

---

### Challenge 10: Bombs

- **Difficulty**: ⭐️⭐️⭐️⭐️⭐️
- **Learning Goal**: Using loops, condition, and lists for dynamic mechanics.
- **Task**: Time to make the game even more exciting by adding some bombs in the field! Your task is to implement two essential game mechanics:

#### Objective 1: Spawn Bombs Based on Player Score

In Challenge 5, you implemented a function that generates the fruit position. Here we have the same concept. We want to spawn a bomb with a random position that shouldn't appear on the snake's body (the bomb size can be 10).


<details> 
<summary>Hint 1</summary> 
<p> 
Implement 'generate_bomb_position' function that does what's mentioned before and go back to 'generate_fruit_position' to ensure the fruit doesn't spawn on the bomb.
</p> 
</details>

<details> 
<summary>Hint 2</summary> 
<p> 
Initialize a list in the setup to hold the bombs. Each time a bomb is generated, append it to the list of bombs. 
</p> 
</details>

<details> 
<summary>Hint 3</summary> 
<p> 
In the game loop, make sure a new bomb is spawned every time the score is a multiple of 50.
</p> 
<details> 
<summary>Tip</summary> 
<p> 
Use a flag to track whether a Bomb has already been spawned for the current score.
</p> 
</details>
</details>

<details> 
<summary>Hint 4</summary> 
<p> 
Draw bombs in the game window. Use: `'pygame.Rect(bomb[0], bomb[1], 10, 10)'` in a for loop.
</p> 
</details>


#### Objective 2: Detect Bomb Collisions and End the Game

<details> 
<summary>Hint</summary> 
<p> 
Here you have to implement a new function to check when the snake collides with the bombs.
</p>
<details> 
<summary>If it's not working, check this</summary> 
<p> 
Snake position is saved as two elements in a list, but the bombs are saved as tuples in a list. (Printing both might help understanding the issue.)
</p> 
</details>
</details>

---

### Challenge 11: Let's eat some real fruits!

- **Difficulty**: ⭐⭐️️  
- **Learning Goal**: Loading and manipulating images with external libraries.
- **Task**: It's time to replace the boring white rectangle with a real fruit!  
Your task is to choose one of the provided `sprites` and use it to display the fruit in the game.
<details>
<summary>Hint</summary>
<p>
Use 'image.load' to load the sprite and 'transform.scale' to scale it.  
</p>
</details>