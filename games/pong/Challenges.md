# **Pong Challenges**

We prepared for you a simple version of the classic Pong game using Python and the Pygame library.\
But the game isn't finished yet, there are still some features missing.\
In order to implement these features you'll have to face some challenges.

These challenges are sorted per difficulty. You can start with whichever one your team wants.\
However, for some challenges you may need some parts to be already implemented.\
Besides the difficulty we estimated the time that you might need to complete the challenge.\
There's also a short explanation about the specific challenge in the dropdown.

The basic challenges are marked inside the code with a comment. Use `str + f` and search for task 1-4 to find them.\
Further information about the given code can be found in the README.

## Example Demo

Here's an example of how the pong game might look like in the end.

[![Pong Demo](https://img.youtube.com/vi/9DUlVqV8H7A/0.jpg)](https://www.youtube.com/watch?v=9DUlVqV8H7A)

## Helpful resources

- [Pygame Documentation Front Page](https://www.pygame.org/docs/)
- [Pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html)
- [Collection of Pygame Tutorials from pygame.org](https://www.pygame.org/wiki/tutorials)
- [In depth Pygame Tutorial from coderslegacy.com](https://coderslegacy.com/python/python-pygame-tutorial/)
- [Python Time Library for e.g. measuring time](https://docs.python.org/3/library/time.html)

<br>

## Challenges

### Challenge 1.

<summary>Player Right Movement</summary>

**Story:** Only Player left can move, that's pretty unfair if you ask me.

**Task:**\
    - (1)Help Player right to move. 

**Think about the following questions:**\
    - (1)Does the player only move up and down? Is there a restriction on movement?\
    - (2)What variables affect player movement?

**Difficulty:** ⭐\
estimated time = 30min
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - The variable for the player_left movement is changed multiple times in the code. 
  </details>
</details>  

 <br>

### Challenge 2.

<summary>Ball Bounce</summary>

**Story:** The ball is tampered with and bounces off the players for now and goes only left and right. Boring :(

**Task:**\
    - (1)Make it also go up and down after a bounce. Maybe even at the start and after a reset of the ball.\
    - (2)You will notic that the ball doesn't bounce off the top and bottom of the window, so you'll have to make it bounce there as well.

**Think about the following questions:**\
    - (1)What variables control the movement of the ball?\
    - (2)How can we check if the ball is touching the top and bottom of the window?

**Difficulty:** ⭐⭐\
estimated time = 1h +
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - look at the current implementation to change the balls direction.
  </details>

  <details>
  <summary>Hint 2</summary>
  
  - In order to set the initial direction of motion of the ball, the initial value of the global variable ball_speed_x needs to be set and changed in the function ball_reset() as well.
  </details>
</details>  

<br>

### Challenge 3.

<summary>Game Over</summary>

**Story:** Evil Dr. Bong warps your end button. Now no one can truly win in the endless game.

**Task:**\
    - (1)Make the game end.\
    - (2)Announce the winner.\
    - (3)Give the game over state its own screen display and the players the possibility to restart.

**Think about the following questions:**\
    - (1)What are the conditions for player victory?\
    - (2)How can we announce the winner on screen?\
    - (3)If we were to restart the game, how could we achieve the game state change?

**Difficulty:** ⭐⭐\
estimated time = 1h
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - A description of the rules can be found in the README file.
  </details>

  <details>
  <summary>Hint 2</summary>
  
  - We can use the pygame.font.render() function to edit the text formatting and the WINDOW.blit() function to display the text on the screen.
  </details> 

  <details>
  <summary>Hint 3</summary>
  
  - To enable restarting the game, need to set up a restart button first, which will automatically complete the transition of the game state when pressed..
  </details> 
</details>  

<br>

### Challenge 4.

<summary> Scoring System </summary>

**Story:** Congratulations on defeating the evil Dr. Bong! But he made a big destruction at the end and now you still need to fix the broken scoring system. Let the player's level be expressed by the score.\
In order to show the best of the best you'll need a saving system and show it somewhere e.g. the game over screen from challenge 3.

**Task:**
    - (1)We prepared three empty functions for saving, loading and updating the scores for you to work on and a `scores.txt` file. You need to refine these three functions.\
    - (PS: The `get_player_name()` function already gives you the name, so you don't have to worry about that.)

**Think about the following questions:**\
    - (1)How should we design the scoring model so that the score accurately reflects the level of the player?\
    - (2)In what format do we store the gamerscore data?\
    - (3)How will we implement file reading and writing?\
    - (4)At what point in time do we need to execute each of the three functions saving, loading and updating?

**Difficulty:** ⭐⭐\
estimated time = 1h 
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - A design pattern to refer to：Use rank_score to describe the player level, rank_score ≥ 0. rank_score changes according to the player's net winning score per game.
  </details>

  <details>
  <summary>Hint 2</summary>
  
  - A design pattern to refer to：player_name, and player_rank_score, we can use binary groups to describe the data. We can store the data in a .txt file .
  </details> 

  <details>
  <summary>Hint 3</summary>
  
  - We can use functions open('File_name.txt', 'r'), open('File_name.txt', 'w') to read and write files.
  </details> 
  <details>
  <summary>Hint 4</summary>
  
  - If a player forcibly quits in the middle of a match, the match data should not be recorded. Only fully completed matches will affect the rank_score.
  </details> 
</details> 
<br>

### Challenge 5.

<summary> Add more information </summary>


**Story:** From the tasks above, you have done all the hard work and completed your own design for Pong! Now it's time to add some information to help players understand the content of game.

**Task:**\
    - (1)Prompts the player about the conditions for winning before starting the game.\
    - (2)Display the player's name in the upper-left and upper-right corners, respectively, as the game progresses.\
    - (3)Adds background music to the game. (Needs to loop during the game and stop at the end of the game)\
    - (4)A match point tone is played when one player reaches the match point (when four points have been scored).

**Think about the following questions:**\
    - (1)How to play music in pygame.\
    - (2)How to loop or limit the music to play once?

**Difficulty:** ⭐\
estimated time = 30min
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - Synthesize what you have learned in previous challenges.
  </details>

  <details>
  <summary>Hint 2</summary>
  
  - The pygame.mixer.Sound() function imports music that is local to the game.
  </details>  
</details> 

<br>
<br>

## Advanced Bonus Challenges

If you want to further improve your game or code and make it more interesting, these challenges are for you.

### Bonus Challenges 1

<summary>Complex Ball Bounce</summary>

**Story:** You're trying to add some cooooooler changes to Pong! Maybe you can give the player more control over the ball or maybe take some control away.

**Task:**\
    - (1)You can try and make the ball bounce more realistic or dynamic.\
    - (e.g. make the ball go up when the player hits it with the top part of the paddle and straight with the middle etc.)

**Think about the following questions:**\
    - (1)Is it feasible to describe the process of impact and rebound in terms of vectors?\
    - (2)How to design the bounce pattern of the ball?

**Difficulty:** ⭐⭐⭐\
estimated time = 1h 30min
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - It is possible to describe the collision process using vectors, but how to avoid ball_speed_x=0?
  </details>

  <details>
  <summary>Hint 2</summary>
  
  - A design pattern to refer to：The impact event should not change the velocity of the ball. The angle of reflection of the ball is only related to the position of impact, the angle of reflection is between(0°，45°).
  </details> 

  <details>
  <summary>Hint 3</summary>
  
  - The object of trigonometric calculations in math package is radians, not angles, which have to be converted using the math.radians() function first.
  </details> 
</details> 

<br>

### Bonus Challenges 2

<summary>On Screen Obstacle</summary>

**Story:** You're trying to add some cooooooler changes to Pong! You're trying to add some randomly generated obstacles to the game to bring more challenge to the game.

**Task:**\
    - (1)Make the game a bit harder by placing a small object in the playfield after a certain amount of time.\
    - (2)It shouldn't be the same position all the time.\
    - (3)After each round/point the obstacle should disappear again and reappear if the time is met.\
    - (4)Since obstacles will appear after a certain amount of time, it is necessary to display the game time to prompt the player.

**Think about the following questions:**\
    - (1)How to generate an object in pygame and make its position random?\
    - (2)How do you achieve the transformation of objects from non-visible to visible?\
    - (3)How do you implement timing for the game?\
    - (4)How do you achieve the transformation of objects from non-collidable to collidable?

**Difficulty:** ⭐⭐⭐\
estimated time = 1h 30min
<details>
  <summary>🔐 Hints</summary>
  <details>
  <summary>Hint 1</summary>
  
  - Objects can be generated in pygame using the pygame.Rect() function.
  </details>
</details>  


<br>