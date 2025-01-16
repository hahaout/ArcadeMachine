# Challenges

<img src="challenge_pictures\Pacman_logo.png" alt="Pacman Logo" height="auto" width="500"></img>

This game of Pacman is not much fun yet. It's still missing in so many parts.
So let's complete the game together. 
I am pretty sure, at the end we will have a super cool Pacman game!

---

## Before starting

1) Please mind the order of the challenges. They rely on each other. 
2) Most Challenges are marked in the code with a comment. Just search for `CHALLENGE x` where x is the number of the challenge.
3) The **basic** challenges come with a solution.  
4) The **extra** challenges are voluntary work that you can do with the resulting code of the other challenges if you want to.
For these challenges we do not have an example solution.

### Handbook

To help you get started, we compiled a handbook with many important information,
like how the basics of Pygame work and how to work with an
object-orientied code structure.

[Click here to access the Handbook](../../Handbook/Pacman_Handbook.md)

You will also find a great Readme file in this Pacman folder,
describing each the purpose of each file.

[Click here to access the Readme](README.md)

---

## Basic Challenges

### Pacman: The Digital Realm's Defender

Imagine Pacman as a “guardian of the digital realm” venturing through a
pixelated world to recover stolen code or “bits of light.” 
Each challenge represents a part of Pacman’s journey to retrieve these fragments 
from “data ghosts” threatening the peace of his world.

### Challenge 1

**Difficulty:** ⭐

**Learning-Goal:** Learn how to play sounds in Pygames. 
Practice finding your way around in an unknown code base.

**Task:** Every time Pacman defeats a Data Ghost, it lets out a distorted digital wail, 
signaling the release of corrupted energy back into the system. When Pacman dies, 
a dramatic system alert sound plays, symbolizing a critical system failure in the Digital Realm.

Find the function where pacman dies. 
There you can play the sound just like it's played, when a ghost gets eaten.

**Let the sounds of your journey echo across the Data Grid. 
Will it be the call of victory or the alarm of failure?**


<details>
  <summary>Hint 1</summary>

- Pacman dies in the Pacman.py `die()` function
</details> 

<details>
  <summary>Hint 2</summary>

- In the file `sounds.py` you will find all the sounds you can play
</details> 

<details>
  <summary>Hint 3</summary>

- play the dying sound by calling: `pacman_death_sfx.play()`
</details> 

### Challenge 2

**Difficulty:** ⭐⭐

**Learning-Goal:** Understand how to add numbers to a score using variables 
and conditional logic (if statements).

**File:** `Scoring.py`

**Story:** Occasionally Pacman eats rare Digital Relics, 
represented as pills or fruits like Cherries and Strawberries. 
These relics hold value in the Digital Realm and grant a high score when collected. 
Fixing their scoring logic in the `add_points_for` function in the `Scoring.py` is important to 
fully restoring the system.

Every relic recovered is a step closer to save the Digital Realm. 
Assign their true value and let Pacman reap the rewards!

**Task:** Pacman is eating pills, but the score isn't going up? 
Well let's take a look at the `add_points_for` function in the `Scoring.py`. 
Seems like it gets called, but the score isn't increasing. 
The function gets the variable `eaten` as an argument.
The variable may be: "ghost", "pill", "energizer" or the name of a fruit. 
For this game only the "cherry" and "strawberry" are relevant.
The point values are: Pill - 10, Energizer - 50, Ghost - 200, Fruits - see below

![fruit_points.jpeg](challenge_pictures%2Ffruit_points.jpeg)

<details>
  <summary>Hint 1</summary>

- You need to program an if statement
</details>

<details>
  <summary>Hint 2</summary>

- increase the value of the variable `self.score` based on the `eaten` argument
</details>


### Challenge 3.1

**Difficulty:** ⭐⭐⭐⭐

**Learning-Goal:** Practice using lists and loops to update multiple items.

**File:** `PillManager.py`

**Task:** 
Energizers (big circles) has special power in the Digital Realm. 
When Pacman eats one, it sends out a wave that scares the ghosts, 
making them vulnerable for a short time. 
This gives Pacman a chance to eat them and earn some extra points.
But something isn’t working. The energizers aren’t scaring the ghosts. 
Your job is to fix this by updating the `eat_pill` function so the energizers work properly 
and help Pacman turn the game around!

When you are finished, you can try to kill a ghost by eating it.

<details>
  <summary>Hint 1</summary>

-  If a pill is an energizer, it should make the ghosts scared. So you should make an if statement.
</details> 

<details>
  <summary>Hint 2</summary>

-  You can check if the eaten pill was an energizer with using: `pill_to_eat.is_energizer`
</details> 

<details>
  <summary>Hint 3</summary>

-  You need to iterate all ghosts with a for-loop, to make every ghost scared.
</details> 

<details>
  <summary>Hint 4</summary>

-  you can get the ghosts from here: `self.game.ghosts`
</details> 

<details>
  <summary>Hint 5</summary>

-  `ghost.make_scared()` makes all the ghosts scared
</details> 


### Challenge 3.2

Difficulty: ⭐

**Learning-Goal:** Learn how to check a condition (like "is the ghost dead?") 
and call a function when the condition is true.

**File:** `Ghost.py`

**Task:**
When Pacman defeats a ghost, it’s supposed to return to the Reassembly Zone to recover. 
But right now, the ghosts don’t know how to move after they’re defeated.
We’ve already written the code to guide them back, but we forgot to call it. 
Your job is to check if a ghost’s mode is “dead” and make sure 
the code runs so they can return safely.

### Challenge 3.3

Difficulty: ⭐

**Learning-Goal:** Understand how to modify and differentiate scoring logic using 
conditional statements (if/elif) and variables to assign different point values based on object type.

**File:** `PillManager.py`

**Task:** 
Energizers (big circles) are important in the Digital Realm - but eating them
currently gives Pacman the same score as he would eat a normal circle.
To appreciate the courageous performance of Pacman eating the big pills,
they should give him more points than a normal pill.

<details>
  <summary>Hint 1</summary>

-  look into the `eat_pill` function.
</details> 

<details>
  <summary>Hint 2</summary>

-  if an eaten pill as an energizer, it should also add the points for a energizer.
</details> 

<details>
  <summary>Hint 3</summary>

-  add `self.game.current_score().add_points_for("energizer")`
</details>

### Challenge 4

**Difficulty:** ⭐⭐⭐

**Learning-Goal:** Use Python to read and write files to store data like the high score.

**File:** `MainGame.py`

**Task:** 
The high score represents the greatest achievement in the 
Digital Realm — a record of Pacman’s most heroic efforts!
But right now, even when a new high score is reached, 
it isn’t being saved to the system’s memory (`high_score.txt`). 
Without this update, the greatest victories risk being forgotten.

Your task is to fix the `update_high_score` function in `MainGame.py`. 
Make sure the high score file is updated 
whenever the current score beats the previous record, 
ensuring Pacman’s legacy lives on.

**Don’t let greatness go unrecognized! Fix the high score update and make every victory count!**

<details>
  <summary>Hint 1</summary>

- maybe you can steal something from the `init_scoring` in the MainGame.py
</details>

<details>
  <summary>Hint 2</summary>

- You can get the current and best score from `self.scores`
</details>


### Challenge 5 

**Difficulty:** ⭐⭐⭐⭐

**Learning-Goal:** Learn how to detect user inputs and working with existing code.

**File:** `MainGame.py`

**Task:** 
When Pacman fails to save the Digital Realm, 
all seems lost... but every hero deserves a second chance.
Right now, there’s no way to restart the mission after a game over, 
leaving Pacman stuck in failure.

Your job is to fix this by updating the `handle_event` function.

Make it so that pressing the space bar resets all the necessary variables, 
giving Pacman the opportunity to try again and restore the Digital Realm.
But only if it's actually a game over of course.

**Every hero needs another shot! Add the restart option so Pacman can rise.**

<details>
  <summary>Hint 1</summary>

- the value for the space bar key is stored in is `pygame.K_SPACE`
</details> 

<details>
  <summary>Hint 2</summary>

- to remove the game over background you can use `self.screen.fill("black")`
</details> 

<details>
  <summary>Hint 3</summary>

- the `self.reset()` function is really helpful
</details> 

<details>
  <summary>Hint 4</summary>

- You should look into the init code, because many of these things need to be 
re-called to restart the game. It's also helpful - but not necessary - to create a new 
function for these code lines. Because they are used multiple times in the code.
If you want to change something in the future, you would need to change the code at two
places. So this is the perfect opportunity to try to create a new function by your own.
</details> 

<details>
  <summary>Hint 5</summary>

- for the animations to work you have to adjust the `self.time_for_next_animation`
</details> 


### Challenge 6

**Difficulty:** ⭐⭐

**Learning-Goal:** Practice working with timers and conditions to create repeating patterns.

**File:** `Ghost.py`

**Task:**
The Data Ghosts have been far too relaxed, 
lurking in their corners and letting Pacman roam free. 
But now, they’re ready to step up their game and actively hunt Pacman down. 
However, even the Ghosts need a strategy — they’ll switch between scattering 
to regroup and hunting to chase Pacman.

Your task is to update their behavior. 
Use the `change_mode("hunt")` function to make the ghosts actively chase Pacman. 
However, the ghosts shouldn't hunt all the time. 
They should scatter for 7 seconds and then hunt for 20 seconds.
This should repeat until they have hunted 5 times. After that: No scattering anymore.
In `movement_logic` there already is an elapsed time that you can use.

**The chase is on! Make the Ghosts smarter and more strategic to give Pacman a real challenge!**

<details>
  <summary>Hint 1</summary>

- remember to reset the `start_time` and `elapsed_time` before changing the mode
</details> 

<details>
  <summary>Hint 2</summary>

- you can create a variable `self.hunt_count` in the init function
- then increase it for every hunt and stop switching to scatter mode after it hits five
</details> 


<details>
  <summary>Is this too easy for you? Then here is an extra task:</summary>

- Change it so the cycle works as the original game:
  - scatter for 7 seconds, then hunt for 20 seconds, 
  - scatter for 7 seconds, then chase for 20 seconds, 
  - scatter for 5 seconds, then hunt for 20 seconds, 
  - scatter for 5 seconds, then switch to hunt mode permanently.
</details>

### Challenge 7

![Clyde](sprites\Clyde_tileset.png)

**Difficulty:** ⭐⭐⭐

**Learning-Goal:** Write custom rules for character movement by calculating 
distances and making decisions using math.

**File:** `Ghost.py`

**Task:**
The quirky Data Ghost Clyde, doesn’t like to follow the crowd — he wants to have his own style. 
But right now, he’s just copying Inky’s movements during the hunt. 
He needs his own logic to show his true personality.

Here’s the plan:
- When Clyde is more than 8 tiles away from Pacman, he should move just like blinky.
- But when he gets closer (within 8 tiles), Clyde gets nervous and
he should move just like he does, when he is in "scatter" mode.

Your task is to modify the `get_new_direction_for_intersection` function 
in the Ghost class, so Clyde behaves the way he’s meant to.

**Help Clyde stand out! Give him the unique movements that show his special personality.**

<details>
  <summary>Hint 1</summary>

- to compute the distance use `math.dist(clyde_pos, pacman_pos)`
- now you just have to find out how to get clydes and pacmans position 
  - (maybe look at the other ghosts for that)
</details> 

<details>
  <summary>Hint 2</summary>

- To correctly convert and check the distance of Clyde to pacman, you need to multiply tile_size by 8:
`TILE_SIZE * 8`
</details> 


### Challenge 8

**Difficulty:** ⭐⭐⭐⭐

**Learning-Goal:**
Change direction for the ghosts using Python functions, 
showing how small changes in code can make big differences.

**File:** `Ghost.py`

**Task:**
When Pacman eats an energizer, the ghosts are supposed to panic and run away 
in the opposite direction. But right now, they’re not reacting as they should — 
they just keep moving as if nothing happened.

The task is to fix this by ensuring that when the ghosts enter the “scared” state, 
they immediately change direction to flee from Pacman. Update their logic so 
their behavior matches their fear!

**When Pacman powers up, the ghosts should run! Fix their escape logic 
and make the chase exciting.**

<details>
  <summary>Hint 1</summary>

- you only need one line with 2 function calls and 1 variable
</details> 

<details>
  <summary>Hint 2</summary>

- use `self.change_direction()` and as parameter `get_opposite_dir()`
</details> 

### Challenge 9 

**Difficulty:** ⭐

**Learning-Goal:**
Learn how to create and update a counter for lives, starting with a simple function.

**File:** Pacman.py

**Task:**
Pacman is brave, but even heroes need more than one chance! 

Normally, Pacman has three lives to complete his mission and 
restore the Digital Realm. Right now, he has only one, making his task nearly impossible. 
Your job is to fix this by updating the `init_hearts` function so Pacman starts with three lives, 
giving him a fighting chance to save the world.

**Every hero deserves a second (and third) chance! 
Give Pacman the extra lives he needs to succeed.**

### Challenge 10.1

**Difficulty:** ⭐⭐

**Learning-Goal:**
Learn how to implement spatial logic in Python by using conditional statements (if/elif), 
accessing external data (like a grid from another file), 
and updating object properties (like coordinates) to enable dynamic position changes.

**File:** Character.py

**Task:**
The warp tunnels are Pacman’s secret escape routes, 
allowing him to instantly travel from one side of the Digital Realm to the other.

But right now, the warp system is broken, leaving Pacman trapped on one side.
Your task is to repair the `warp` function. 

If Pacman is on a tile marked with a 5 or 6 (as defined in `game_grid.py`), 
he should instantly warp to the corresponding tile on the opposite side.

<details>
  <summary>Hint 1</summary>

- use the `map_index_to_coordinates` function to change the grid index to the x and y coordinates
</details> 

<details>
  <summary>Hint 2</summary>

- for a character to move you have to change its `self.x` and `self.y` accordingly
</details> 

<details>
  <summary>Hint 3</summary>

- Pacman should teleport some coordinates further away from the warp teleporter, or he will
be stuck in a teleport loophole.
</details> 

### Challenge 10.2

**Difficulty:** ⭐

**Learning-Goal:**
Practice triggering sounds in Pygames conditionally based on actions.

**File:** Character.py

**Task:**
When Pacman uses the warp tunnel, there’s no sound. 
Let’s fix that! Add a sound effect when Pacman warps from one side of the screen to the other.
Feel free to be creative, you can use any sound you like.

<details>
  <summary>Hint 1</summary>

- you can download sound files with a youtube mp3 downloader
</details>

---

## Extra Challenges

### Challenge 11

**Difficulty:** ⭐⭐⭐⭐⭐

**Learning-Goal:**
Practice integrating the class into a larger program by uncommenting 
and connecting pre-existing code, enabling dynamic game features.

**File:** `Fruit.py` and `MainGame.py`

**Task:**
The fruits are rare and valuable items in the Digital Realm, 
appearing occasionally to reward Pacman with bonus points. 
But right now, the fruits are missing — they exist in name only, 
with all their functionality left unimplemented.

Your mission is to bring the fruits into the game.
Implement the fruit class, giving it all the behavior it needs, 
and uncomment the already existing calls in the main game, 
so the fruits can appear and function as intended. 

**Let Pacman enjoy the vitamins he deserves!**

### Challenge 12

**Difficulty:** ⭐⭐⭐⭐⭐

**Learning-Goal:**
Practice implementing logic to remove objects (like fruits) after a set duration, 
ensuring proper game flow and organization.

**File:** `MainGame.py`

**Task:**
The Digital Realm’s rare fruits, the strawberry and cherry, 
are showing up together, crowding the space and creating confusion.
Normally, a fruit should disappear 9 seconds after it spawns, 
making room for the next one. Fix this by implementing a timer in the fruit logic. 
Ensure that each fruit vanishes after 9 seconds, keeping the game clean and organized.

### Challenge 13

**Difficulty:** ⭐⭐⭐⭐⭐

**Learning-Goal:**
Practice modifying functions to show temporary effects 
(like displaying points and hiding Pacman briefly) using special techniques

**File:**  `MainGame.py`

**Task:**
In the Digital Realm, every victory — whether eating a fruit 
or defeating a ghost — is celebrated with a flash of points and a quick visual effect. 
But right now, these moments of triumph stay unnoticed, with no points displayed 
and Pacman’s quick vanish animation missing.

Your task is to bring these moments to life. Start by updating the `ghost_collision` 
function so that when a fruit or ghost is eaten, the points appear and Pacman 
momentarily disappears as part of the effect.

When a fruit or a ghost gets eaten, 
you normally see the points as a little number and pacman shortly disappears.

![Points_count](challenge_pictures/Points_count.png)

### Challenge 14

**Difficulty:** ⭐⭐⭐⭐⭐

**Learning-Goal:**
Learn how to implement multi-level game. Practice managing game state transitions, 
updating conditions for new events (like spawning fruits), 
and enhancing gameplay with dynamic rewards

**File:** `MainGame.py`

The Digital Realm is vast, and one level is just the beginning of Pacman’s big journey. 
After Pacman eats all the pills in the current level, he should advance to the next stage. 
Each new level resets the pills to their original positions and introduces 
new challenges with more fruits.

Here’s the behavior to implement:
- When all the pills are eaten, start Level 2, with the same pill layout as Level 1.
- In Level 2, introduce two new fruits, spawning after 70 and 170 pills are eaten, 
respectively. Use the guide to decide which fruits appear and how many points they grant.

Your mission is to specify and implement this progression logic, 
ensuring Pacman can continue his quest across multiple levels.

**The Digital Realm is far from conquered — add more levels and new rewards 
to keep Pacman’s adventure alive! He will be thankful.**

![fruit_points.jpeg](challenge_pictures%2Ffruit_points.jpeg)




