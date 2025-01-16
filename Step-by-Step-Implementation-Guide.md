# Contribution Guidelines for New Challenges in This Repo

Welcome to our GitLab repository! To keep our contributions organized and ensure we maintain high standards in the challenges we create,
we've established these detailed guidelines. Please follow them closely to make the process smooth and straightforward for everyone involved.

## Working from an Issue with Challenge Ideas
If you start working on a challenge idea from an existing **feature/challenge-ideas** issue, follow these steps:

1. **Create a New Issue for this Specific Challenge**
   - Create a **new issue** that targets precisely the new idea you want to implement.
   - Pull this issue into **Doing** (see setting Labels in the issue or just pull the issue on the issue board into the Doing-column)
   - **Add additional labels** if needed.

2. **Define the Scope**
   - Clearly explain **WHAT** you are planning to do and **WHY** it makes sense.

### Implementation of a challenge

1. **Implementation:** Begin the actual coding of the challenge. Remember to keep your implementation structured and well documented.
2. **Highlight Solution Code** using comments which are well formatted and clearly written. Additionally separate solution code to facilitate easy removal before distributing the challenge to participants.
3. Write the **full Challenge Description:** Once the implementation is complete, draft a complete challenge description. This includes the problem statement, requirements, and objectives.
4. **Update Hints:** Update and refine the hints after implementation, based on your experience. It’s often difficult to know exactly what additional information will be useful until the challenge has been implemented and tested.

### Tracking a new challenge implementation with a Merge Request

1. **Document Your Process**
   - In the merge request, explain **HOW** you implemented the feature, the decisions you made, and any trade-offs.

2. **Discuss Hints**
   - Write down the hints you plan to provide to participants. This helps maintain consistency and ensures the quality of the challenge.

3. **Facilitate the Review Process**
   - Make sure your reviewer has all the necessary information:
     - **Link the Issue**: In your MR description, link the issue you are addressing to provide context.
     - **Write Good Commit Messages**: Use [good commit messages](https://cbea.ms/git-commit/) that are concise but informative, explaining why a change was made, not just what was done.
     - **Write a Summary**: Include a short summary in the MR description that explains the original issue, how you approached it, and the final implementation. Make it easy for reviewers to understand the entire context without digging into all the details.

### Challenge Text: Description and Hints pattern:

1. **Challenge Number, and a very breif description**:
   - This should be a `Header` element of third level `### Challenge x: blabla`:
```markdown
### Challenge 1: Moving and Shooting
```
2. **Challenge Learning Goals**:
   - Start with a small `header` element of fourth level `#### Goals`
   - Write a small text explaining the particepants what are they learning/practicing while working on the task
   - Highlight the main concepts
```markdown
#### Goals:
This challange aims to practice `Conditions`, `Array-Selection using key indexes`, some `Game-logic` and give you a quick start in the `Object Oriented Programing` `Creating a new Object` from a pre-defined class and understanding and using `attributes`.
```
3. **Challenge Story**:
   - Start with a small `header` element of fourth level `#### Story`
   - Write a small fun text about the task
```markdown

#### Story:
You can't fight back and the Earth is doomed. Save the Earth by sending a strong warrior to fight on behalf of humanity.
Finish the Player class. Fight For All That's Beautiful In The World.

```
4. **Challenge Tasks**:
   - Make the section a drop down by surrounding it with `<details></details>` Tag
   - add a `<summary>Challenge Tasks: Main Goal of all the tasks</summary>`
   - add a task as a third header `### Task0x: Task Brief Description: `
   - add subtasks or steps or details to the task
```markdown

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
```
5. **Challenge Hints**:
- same process as challenge tasks:
```markdown

<details>
<summary>Hints:</summary>

### Task 1: Player Movement
- Use `pygame.key.get_pressed()` to get the state of all keys:
  - It returns a list of booleans, where `True` indicates a key is pressed.
  - Example: `[False, False, True, ...]`.
- Use `if-elif` conditions to detect specific key presses.
- Move the player only if:
  1. The corresponding key is pressed.
  2. The movement keeps the player within screen boundaries.
- Access class-specific attributes like `self.speed` using the `self` keyword.
- Update the player’s position by adding/subtracting `self.speed` to/from the current position:
  - Example for vertical movement:
    ```python
    self.rect.y += self.speed
    ```
- Use predefined constants for key detection:
  - `pygame.K_LEFT`, `pygame.K_RIGHT`, etc.

### Task 2: Player Shooting
- Use `pygame.time.get_ticks()` to track the current game time in milliseconds.
- Limit bullet creation:
  - Ensure only one bullet is fired per key press by checking:
    ```python
    current_time - self.last_shot_time >= self.shoot_cooldown
    ```
- Refer to the `Bullet` class in `bullet.py` to understand its attributes and behavior.
- Use the class constructor (`__init__()`) to create new bullet objects:
  - Syntax:
    ```python
    bullet = Bullet((x, y), speed, image_path, sound_path)
    ```
- Ensure all new bullets are added to the player's `bullets` group:
  ```python
  self.bullets.add(bullet)
</details>

```
6. **Challenge Level**:
- Easy, Medium, hard, advanced......
```markdown
difficulty = easy\medium

```
### General Best Practices
- **Write Clear Documentation**: Update relevant documentation if new challenges add new features or impact existing ones.
- **Keep Code Clean**: Make sure to write readable code with comments where necessary, especially where the logic might be complex or non-obvious.
- **Use Consistent Naming**: Follow consistent naming conventions to improve readability.
- **Test Thoroughly**: Ensure that challenges are well-tested, including edge cases, to avoid unexpected issues during participant use.
- **Peer Review**: Be open to feedback, and take time to review other people's code as well. Collaboration improves code quality and fosters team growth.

### Quick Checklist Before Submission
- [ ] The challenge idea is documented in the issue tracker.
- [ ] Notes and concrete implementation details are documented.
- [ ] The challenge is implemented.
- [ ] Solution code is highlighted for easy removal.
- [ ] Full challenge description is complete.
- [ ] Hints are updated based on implementation insights.
- [ ] A new issue was created for a specific challenge idea (if applicable).
- [ ] The MR includes **WHAT**, **WHY**, and **HOW** information.
- [ ] The issue is linked in the MR.
- [ ] Commit messages are well written.
- [ ] MR summary is written for easy review.

Thank you for helping us maintain the quality and consistency of our challenges. By following these guidelines, we can ensure an effective and smooth workflow for everyone!
