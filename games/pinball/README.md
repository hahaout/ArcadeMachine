# Pinball Machine

A pinball machine where you try to keep the ball as long as possible in the game to hit special obstacles to get points and reach a highscore


## How to Run

+ Run `python Menu.py`

## Controls

+ `Esc` to leave the current scene/End the game in the Main Menu
+ `W/S` to move in the menu, options and `Enter` to confirm selection
+ To launch the ball at the start use `Space`
+ Move the flippers with `a` and `d`

## Rules

+ Launch the ball into the playfield and let it bounce around
+ hit the green obstacles to get points
+ use the flippers to keep the ball going
+ if the ball reaches the hole at the bottom the game is over


## Files and functions

| File/Module            | Description                                                                                              | Key Functions/Methods                                                                                   |
|------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `Menu.py`              | Main loop, main menu, options, and high scores menu.                                                    | - `main()`: Initializes pygame, variables, and main game loop.                                          |
|                        |                                                                                                          | - `main_menu(screen, lastButton)`: Draws buttons, selects scenes, and displays the title.               |
|                        |                                                                                                          | - `options(screen, lastButton)`: Draws and adjusts options.                                             |
|                        |                                                                                                          | - `highscore(screen, lastButton)`: Loads and displays high scores; allows return to main menu.          |
|                        |                                                                                                          | - `leave(screen, lastButton)`: Handles exit button action from the main menu.                           |
|                        |                                                                                                          | - `draw_Text(screen, font, color, text, position)`: Helper function for drawing text.                   |
| `Highscore_Manager.py` | Manages writing and reading high scores from a text file.                                                | - `write_highscores(highscores)`: Saves high scores.                                                    |
|                        |                                                                                                          | - `read_highscores()`: Reads high scores.                                                               |
| `Music_Manager.py`     | Loads and manages music and sound effects.                                                              | - `play_selection()` and other functions: Play/stop music or sounds.                                    |
| `Game.py`              | Manages game states and rendering functions.                                                            | - `__init__(self, pMusic_Manager, main_Menu_Function, highscore_Menu_Function, draw_Text_Function)`:    |
|                        |                                                                                                          | Initializes variables and game setup.                                                                   |
|                        |                                                                                                          | - `game(self, screen, lastButtons)`: Manages game states and renders screens.                           |
|                        |                                                                                                          |   - `not_started(self)`: Default game state; loads resources for the first time.                        |
|                        |                                                                                                          |   - `ball_waiting(self)`: Waits for Space key to launch the ball.                                       |
|                        |                                                                                                          |   - `game_running(self)`: Handles ball physics, flipper movements, collisions, and playfield exits.     |
|                        |                                                                                                          |     - `hit_flipper()`: Detects ball collisions with flippers and adjusts bounce physics.                |
|                        |                                                                                                          |   - `game_finished(self)`: Allows entering a name, shows high scores, and updates rankings if eligible. |
| `GameObjects.py`       | Defines game objects like the ball, flippers, map, and point obstacles, along with their physics.        |                                                                                                         |


## Introduction

Hey, you! Welcome to the world of pinball! Play with the ball, Bobby Bounce-a-Lot, and his friends the brothers Larry und Louie Launch, they are the flippers.

Your goal is to launch Bobby into the playfield and let him bounce around. You can use the Flippers, Larry and Louie, to keep the ball going. When you hit the green obstacles, you earn points! If the ball Bobby reaches the hole at the bottom the game is over.

The Challenges are marked with HACKATHON CHALLENGE x. To find the place where you need to implement the code press ctrl+f and search for example for HACKATHON CHALLENGE 1. The file to search in is given with the Challenge.


## Challenges


### HACKATHON CHALLENGE 1
Difficulty: ⭐

File: GameObjects.py 

The Flippers, Larry and Louie Launch, can already move up, but unfortunately, they won’t come down! Help them!

**We want you to take a closer look at the first `if` statement in the "moveFlipper" function.
This statement allows the flipper to move up, but it does not return to its initial position.
To fix this issue, add another `if` statement and invert the logic of the first `if` statement so that the flippers return to their initial position.
The flippers can be triggered by pressing the `a` or `d` keys.**
<details>
  <summary>Hint</summary>
 
- Use `not` **and** instead of adding degrees you need to subtract.
</details>

### HACKATHON CHALLENGE 2

Difficulty: ⭐⭐⭐

File: Game.py<br>

Larry and Louie are finally in their element, but when Bobby Bounce-a-Lot gets tired, he just leaves without telling us how much fun he had. Add a score to the pinball world after Bobby left! 

**Complete the "game_running" function by solving all 5 Subtasks.**

2.1 **Check if the ball Sprite´s position is out of the map.**<br>

<details>
  <summary>Hint</summary>

- Compare if the ball is in it´s **y** position **above** 1600.
</details>
<details>
  <summary>Hint</summary>

- this is the ball description: `self.balls_Group.sprites()[0]`
- you need to compare the `.position.y` of the ball.
</details>

2.2 **Decrease the ball amount by one, if the ball is out of the map.**  

<details>
  <summary>Hint</summary>

- In the `__init__` function of the game you can find the description for the ball amount.
</details>

2.3 **The game is finished when the ball amount is zero. Make sure the game changes to the right state, if the ball amount is zero.**

<details>
  <summary>Hint</summary>

- The game states are described as functions.
</details>

2.4 **The game is not finsished, when there are still balls avaiable. Implement a switch to the right game state, by using an else statement.**


2.5 **Finally you need to set the right gamestate, if the ball´s y position is below zero.**  

<details>
  <summary>Hint</summary>
  
- Compare the ball´s position like in subtask 1.
- the game hasn´t started if the statement is true.
</details>

### HACKATHON CHALLENGE 3
Difficulty: ⭐⭐  

File: Highscore_Manager.py<br>

 
Bobby can already tell us how much fun he had – but now he wants to compare his happiness with bounces in the past. Give him a diary so he can write his happiness down!

3.1 **Create a text file to save the Highscores. First you need to check if this text file already exists.**

<details>
  <summary>Hint</summary>
 
- Use the `os.` module: `os.path.exists`
- If the path doesen´t exist you need to create it, by using `os.mkdir`
</details>

3.2 **Now that the "Highscore.txt" exists we want you to read out the Highscores.  
Use a for statement to iterate threw the score in the array.**

<details>
  <summary>Hint</summary>
 
- Open the file for reading it.
- Create an array and fill it with the Score.
  - Use `.read()` and `.splitlines()`

</details>

<details>
  <summary>Hint</summary>
 
- For every score in the array you need to:
  - `.append(score)` to the highscores
  - Don´t forget to `.split(" ")` from the score.

</details>

3.3 **Finally you need to add a function to write down the highscores in the txt. file.  
Open the txt. file for writing in it. And for every score in highscroes you need to write the name and the score.**

<details>
  <summary>Hint</summary>
 
- Use `.write()`
- `score[0]` is the name.
- `score[1]` is the score.
- Don´t forget to add a line break at every end.

</details>

### HACKATHON CHALLENGE 4
Difficulty: ⭐⭐⭐⭐

File: Game.py<br>

Bobby has now a way to write and read his diary, but he doesn’t know how to write his name! He also missed the class in which sorting was taught and now he doesn’t know how to check if his happiness is as big as the last time. Please help him!

You should add a function, so that Bobby, the ball, can write his name down and also a sort that does a ranking of the diary.


4.1 **First of all you need to import the Highscore Manager. And read out the highscores.**
4.2 **Okay, now you need to implement the ability to detect if any buttons are pressed. Use a for Statement that checks the last (pressed) buttons.**
<details>
<summary> Hint </summary>

- for `pressedButton` in `self.lastButtons`
</details>

4.3 **The first thing to check in every iteration is: if any Key is pressed. If the type of the pressedButton is a pygame.KEYDOWN ..**

<details>
<summary> Hint </summary>

- If  `pressedButton.type` is `pygame.KEYDOWN`
</details>

4.4 **.. you first need to check if the pressedButton key is Backspace to delete a character.<br> Implement the ability to delete the last character of the var: `self.entered_Name`.**
<details>
<summary> Hint </summary>

- If  `pressedButton.key` is `pygame.K_BACKSPACE`
</details>

<details>
<summary> Hint </summary>

- for deleting use the `[:]` method.
</details>

4.5 **And now you need another If Statement to save the Highscore.**

<details>
<summary> Hint </summary>

- Use the correct form of the If statement. 
- Use `pressedButton.key` and compare it to `pygame.K_RETURN`.
</details>

4.6 **Okay, now you need to check if the highscore is under top ten. Use a for statement and iterate threw the `Highscore_Manager.highscores`.**

<details>
<summary> Hint </summary>

- It is easier to use the `range` and `len` methods.

</details>

4.7 **In every iteration you need to check if the `self.score` is bigger than the Highscore in the list.**

<details>
<summary> Hint </summary>

- The score of the Highscore is in place `[1]`

</details>

4.8 **Okay now it´s time to replace the old Highscore with the new Highscore. You need to cut out the old Highscore and replace it with a placeholder for the first instance.**

<details>
<summary> Hint </summary>

- `Highscore_Manager.highscores = Highscore_Manager.highscores[:place] + ["x"] + Highscore_Manager.highscores[place:-1]`
  
</details>                                                                  

4.9 **Now that you have a placeholder, you need to replace it with the `self.entered_Name` and the `self.score`.**

<details>
<summary> Hint </summary>

- Use the created `place` var to select the correct line in the `Highscore_Manager.highscores`.
- Remember that the entered name and score are strings.
</details>

4.10 **Wow, you are almost finished! <br> Now, you just need to call the Highscore_Manager with the `.write_highscores` method and add the `.highscores`.**

<details>
<summary> Hint </summary>

- `Highscore_Manager.write_highscores(Highscore_Manager.highscores)`

</details>

**You´ve made it, you only need to add the ability to go to the Highscores if you have a highscore. But don´t worry we put you the remaining code in the Hint, because it´s not GPT related knowledge.**

<details>
<summary> Hint </summary>

```python
# go to highscores if you have a highscore
                            self.current_Scene = self.highscore_menu
                            self.music_Manager.Play_Music_In_Loop()
                            Highscore_Manager.read_highscores()
                            self.gamestate = self.not_started
                            return
                    #go to Main Menu when no Highscore
                    self.current_Scene = self.main_menu
                    self.music_Manager.Play_Music_In_Loop()
                    self.gamestate = self.not_started
                    return
                elif pressedButton.key != pygame.K_SPACE:
                    self.entered_Name += pressedButton.unicode

```

</details>

### HACKATHON CHALLENGE 5
Difficulty: ⭐⭐⭐⭐⭐

File: Highscore_Manager.py<br>

Story..

**Add a function for encrypting Information.<br>
And also add a function for decrypt the encrypted Information.<br>
We recommend using Cesar encryption. You can, of course, choose any encryption you like.**

5.1 **Create a function for encrypting information.**
<br>

5.2 **Create a function for decrypting the information.**<br>

5.3 **Adapt the code in the “read_highscores” and “write_highscores” functions.**

<br>

**Cesar Encryption Explained:**

In Caesar ciphering (also known as shifting cipher), each letter of the plaintext 
is mapped to a ciphertext letter. For this purpose, the characters of the alphabet are shifted a specific
number (the key) to the right. If you go beyond 
'z', then you start again at 'a'.<br>
**Example:** 'python' becomes 'ravjqp' with key 2. 
### HACKATHON EXTRA CHALLENGE 1
Bobby has so much fun sometimes that he want to go immediatly again. Allow to go multiple times in a row!
Hint: Modify your code from Challenge 2

### HACKATHON EXTRA CHALLENGE 2: 
Be free to think about more fun stuff for Bobby to do :)

### HACKATHON CREATE YOUR OWN MAP! 
You can also create your own map in paint or other picture tools! Just make a picture with height 1600 px and use black as things which Bobby can collide with and white
as the background color. You can change Bobbys start position and the position of the flippers in the game properties and add new obstacles which bring scores in gamestate not_started(search OBSTACLES). You can load your new map in game at LOAD MAP.
Have fun creating your own Pinball machine :)

## Authors

+ Fabian Erbslöh
+ Ismail Yilmaz
+ Timon Hüsemann
+ Tobias Grzesch
+ Jasper Coelen
+ Lukas Kleineberg
+ Joyce Filode
+ 
