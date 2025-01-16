# Tutorial and Reference handbook for participants taking part in the CODE-ARCADE-Hackathon

## Table of Contents

[//]: # (1. **[Mastering Object-Oriented Programming]&#40;#1-mastering-object-oriented-programming&#41;**)

[//]: # ()
[//]: # (    1.1 [Understanding Objects: The Building Blocks]&#40;#11-understanding-objects-the-building-blocks&#41;)

[//]: # ()
[//]: # (    1.2 [Defining a Class: Your Blueprint for Objects]&#40;#12-defining-a-class-your-blueprint-for-objects&#41;)

[//]: # ()
[//]: # (    1.3 [Exploring Attributes &#40;Fields&#41;: What Objects Hold]&#40;#13-exploring-attributes-fields-what-objects-hold&#41;)

[//]: # ()
[//]: # (    1.4 [Methods in Classes: What Objects Can Do]&#40;#14-methods-in-classes-what-objects-can-do&#41;)

[//]: # ()
[//]: # (    1.5 [Constructors: Initializing Your Objects]&#40;#15-constructors-initializing-your-objects&#41;)

[//]: # ()
[//]: # (    1.6 [The `self` Keyword: Referencing the Object]&#40;#16-the-self-keyword-referencing-the-object&#41;)

[//]: # ()
[//]: # (    1.7 [Getter and Setter Methods]&#40;#17-getter-and-setter-methods&#41;)

[//]: # ()
[//]: # (    1.8 [Inheritance: Extending Functionality]&#40;#18-what-is-inheritance&#41;)

[//]: # ()
[//]: # (2. **[Dictionaries in Python: The Ultimate Data Organizer]&#40;#2-dictionaries-in-python&#41;**)

[//]: # ()
[//]: # (    2.1 [Introduction to Dictionaries: What Is a Dictionary?]&#40;#21-what-is-a-dictionary&#41;)

[//]: # ()
[//]: # (    2.2 [Creating Dictionaries: A Step-by-Step Guide]&#40;#22-creating-a-dictionary&#41;)

[//]: # ()
[//]: # (    2.3 [Accessing Dictionary Elements: The Right Way]&#40;#23-accessing-and-updating-values&#41;)

[//]: # ()
[//]: # (    2.4 [Mastering Nested Dictionaries: Access, Use, and Creation]&#40;#24-nested-dictionaries&#41;)

[//]: # ()
[//]: # (3. **[Pygame Essentials for Creating a Snake Game]&#40;#pygame-essentials-for-creating-a-snake-game&#41;**)

[//]: # ()
[//]: # (4. **[State-Machine Introduction]&#40;#4-state-machine&#41;**)

| Section | Topic                                                                                     | Link                                                                                      |
|---------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **1**   | **Mastering Object-Oriented Programming**                                                | [Go to Section](#1-mastering-object-oriented-programming)                                 |
| 1.1     | Understanding Objects: The Building Blocks                                               | [Go to Topic](#11-understanding-objects-the-building-blocks)                              |
| 1.2     | Defining a Class: Your Blueprint for Objects                                             | [Go to Topic](#12-defining-a-class-your-blueprint-for-objects)                            |
| 1.3     | Exploring Attributes (Fields): What Objects Hold                                         | [Go to Topic](#13-exploring-attributes-fields-what-objects-hold)                          |
| 1.4     | Methods in Classes: What Objects Can Do                                                  | [Go to Topic](#14-methods-in-classes-what-objects-can-do)                                 |
| 1.5     | Constructors: Initializing Your Objects                                                  | [Go to Topic](#15-constructors-initializing-your-objects)                                 |
| 1.6     | The `self` Keyword: Referencing the Object                                               | [Go to Topic](#16-the-self-keyword-referencing-the-object)                                |
| 1.7     | Getter and Setter Methods                                                                | [Go to Topic](#17-getter-and-setter-methods)                                              |
| 1.8     | Inheritance: Extending Functionality                                                     | [Go to Topic](#18-what-is-inheritance)                                                    |
| **2**   | **Dictionaries in Python: The Ultimate Data Organizer**                                  | [Go to Section](#2-dictionaries-in-python)                                               |
| 2.1     | Introduction to Dictionaries: What Is a Dictionary?                                      | [Go to Topic](#21-what-is-a-dictionary)                                                  |
| 2.2     | Creating Dictionaries: A Step-by-Step Guide                                              | [Go to Topic](#22-creating-a-dictionary)                                                 |
| 2.3     | Accessing Dictionary Elements: The Right Way                                             | [Go to Topic](#23-accessing-and-updating-values)                                         |
| 2.4     | Mastering Nested Dictionaries: Access, Use, and Creation                                 | [Go to Topic](#24-nested-dictionaries)                                                   |
| **3**   | **Pygame Essentials for Creating a Snake Game**                                          | [Go to Section](#pygame-essentials-for-creating-a-snake-game)                            |
| **4**   | **State-Machine Introduction**                                                           | [Go to Section](#4-state-machine)                                                       |

---

## 1. Mastering Object-Oriented Programming

This handbook is designed to help programming newbies quickly understand Object-Oriented Programming (OOP) concepts
and interpret the given codebase during a hackathon. You don’t need to write OOP-based code, but you may encounter it
in the provided code.

---

### 1.1 Understanding Objects: The Building Blocks

An **object** is an instance of a **class**, which serves as a blueprint for organizing data (attributes) and behaviors
(methods). Classes define how objects are structured and what they can do.

#### Example:
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog(name="Buddy", breed="Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Buddy says Woof!
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>


---

### 1.2 Defining a Class: Your Blueprint for Objects

A **class** is a blueprint for creating objects. It defines attributes (data) and methods (behavior) that the objects created from it will have.

#### Example:
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car(make="Toyota", model="Corolla", year=2021)
print(my_car.make)  # Output: Toyota
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

### 1.3 Exploring Attributes (Fields): What Objects Hold

Attributes are variables that store data for an object. They are defined in the class and initialized through the `__init__` constructor method.

#### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person(name="Alice", age=30)
print(person.name)  # Output: Alice
print(person.age)   # Output: 30
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

### 1.4 Methods in Classes: What Objects Can Do

Methods are functions defined inside a class that operate on the object’s data or perform actions. They are essential for defining object behavior.

#### Example:
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

### 1.5 Constructors: Initializing Your Objects

A **constructor** is a special method that initializes an object’s attributes when the object is created. In Python, it is defined as `__init__`.

#### Example:
```python
class Animal:
    def __init__(self, species="Unknown", habitat="Unknown"):
        self.species = species
        self.habitat = habitat

animal = Animal(species="Tiger", habitat="Forest")
print(animal.species)  # Output: Tiger
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

### 1.6 The `self` Keyword: Referencing the Object

The `self` keyword refers to the current instance of the class. It allows methods to access attributes and other methods of the same object.

#### Example:
```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply_and_add(self, x, y, z):
        return self.add(x, y) * z

calc = Calculator()
print(calc.multiply_and_add(2, 3, 4))  # Output: 20
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

## 1.7 Getter and Setter Methods
### What Are They?

| **Method Type**     | **Description**                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------|
| **Getter Methods**   | Allow you to **get** the value of an object’s private attributes.                               |
| **Setter Methods**   | Allow you to **set** or update the value of an object’s private attributes, often with checks or rules. |

---

### Why Use Them?

| **Benefit**            | **Description**                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------|
| **Encapsulation**       | Keeps internal details private but accessible in a controlled way.                         |
| **Validation**          | Ensures valid data is set (e.g., positive numbers).                                        |
| **Read-Only Properties**| Create attributes that can’t be changed by only providing a getter.                        |
| **Easier Maintenance**  | Centralized control makes future changes easier.                                           |

---

### How to Create Them?

| **Step**               | **Description**                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------|
| **1. Create a Getter**  | Define a method to retrieve the value of a private attribute.                               |
| **2. Create a Setter**  | Define a method to update the value of a private attribute, with optional validation checks. |

### Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Private attribute
        self.age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter for age
    def get_age(self):
        return self.age

    # Setter for age
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.age = new_age
        else:
            raise ValueError("Age must be a positive integer.")

# Usage Example
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

person.set_name("Bob")
person.set_age(35)
print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 35
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---
## 1.8 What is Inheritance?

### What Is It?

[//]: # ()
[//]: # (- **Inheritance**: A child class reuses and extends the functionality of a parent class.)

[//]: # (- **Parent Class**: The original class &#40;template&#41;.)

[//]: # (- **Child Class**: The new class that inherits and customizes the parent class.)

[//]: # ()

[//]: # ()
[//]: # (1. **Reusability**: Avoid duplicate code by inheriting common functionality.)

[//]: # (2. **Extensibility**: Add or modify behavior in child classes without changing the parent.)

[//]: # (3. **Clarity**: Naturally represent hierarchies &#40;e.g., Animal → Dog&#41;.)

| Concept              | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Inheritance**       | A child class reuses and extends the functionality of a parent class.                        |
| **Parent Class**      | The original class that serves as a template for inheriting functionality.                   |
| **Child Class**       | The new class that inherits and customizes the parent class.                                 |

### Why Use It?
| Benefit              | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| **Reusability**       | Avoid duplicate code by inheriting common functionality.                                     |
| **Extensibility**     | Add or modify behavior in child classes without changing the parent class.                   |
| **Clarity**           | Naturally represent hierarchies (e.g., `Animal → Dog`).                                      |

### Example

```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Usage Example
generic_animal = Animal("Animal")
dog = Dog("Buddy")

print(generic_animal.speak())  # Output: Animal makes a sound.
print(dog.speak())             # Output: Buddy barks.
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

### Why Use `super().__init__()`?

- **Why?** To call and reuse the parent class’s constructor or methods.
- **When?** When the child class needs to initialize both parent and child attributes.

### Example

```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal initialized with name: {self.name}")

# Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
        print(f"Dog initialized with breed: {self.breed}")

# Usage Example
dog = Dog("Buddy", "Golden Retriever")
# Output:
# Animal initialized with name: Buddy
# Dog initialized with breed: Golden Retriever
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

# 2. Dictionaries in Python

## 2.1 What is a Dictionary?
A **dictionary** in Python is a collection of data stored in **key-value pairs**. Each **key** is unique and is used to
retrieve its associated **value**, which can be any type (numbers, strings, lists, even other dictionaries).
Dictionaries are created using curly braces `{}` and are useful for organizing and quickly accessing data.

<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

## 2.2 Creating a Dictionary
A dictionary is created using curly braces `{}` with **key-value pairs** separated by colons `:`.

### Example:
```python
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Paris'}
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---
## 2.3 Accessing and Updating Values

### Access Values Using Keys
You can retrieve values from a dictionary using:

| Method                | Description                                                                                  | Example               |
|-----------------------|----------------------------------------------------------------------------------------------|-----------------------|
| **Square Brackets**   | Access values using `dictionary[key]`. Raises an error if the key doesn’t exist.             | `value = my_dict["key"]` |
| **`get()` Method**    | Access values using `dictionary.get(key)`. Returns `None` if the key doesn’t exist.          | `value = my_dict.get("key")` |

### Update or Add Key-Value Pairs
Use square brackets or the `update()` method to modify or add key-value pairs.
```python
# Accessing values
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25
print(person.get("country", "Not Found"))  # Output: Not Found

# Updating values
person["city"] = "London"
person.update({"age": 26, "country": "UK"})

print(person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'London', 'country': 'UK'}
```
<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

---

## 2.4 Nested Dictionaries

A **nested dictionary** stores dictionaries as values, creating hierarchical structures for more complex data.

### Example:
```python
# Nested dictionary
person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland",
        "postal_code": "12345"
    },
    "contact": {
        "email": "alice@example.com",
        "phone": "123-456-7890"
    }
}

# Accessing nested elements
print(person["address"]["city"])  # Output: Wonderland
print(person.get("contact").get("email"))  # Output: alice@example.com

# Adding to a nested dictionary
person["address"]["country"] = "Fantasyland"
print(person["address"])
# Output: {'street': '123 Main St', 'city': 'Wonderland', 'postal_code': '12345', 'country': 'Fantasyland'}
```

## Quick Reference

[//]: # (- **Create**: Use `{key: value}`.)

[//]: # (- **Access**: Use `dictionary[key]` or `dictionary.get&#40;key&#41;`.)

[//]: # (- **Update**: Use `dictionary[key] = value` or `dictionary.update&#40;{key: value}&#41;`.)

[//]: # (- **Nested**: Access inner dictionaries with `dictionary[key][subkey]`.)

[//]: # (- **Default with `get&#40;&#41;`**: Use `dictionary.get&#40;key, default&#41;` for safe access.)

| Operation                | Description                                                                                  | Example                                      |
|--------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------|
| **Create**               | Use `{key: value}` to create a dictionary.                                                  | `person = {"name": "Alice", "age": 30}`      |
| **Access**               | Use `dictionary[key]` or `dictionary.get(key)` to access values.                            | `person["name"]` or `person.get("age")`      |
| **Update**               | Use `dictionary[key] = value` or `dictionary.update({key: value})` to update or add values. | `person["city"] = "Paris"` or `person.update({"age": 31})` |
| **Nested**               | Access inner dictionaries with `dictionary[key][subkey]`.                                   | `person["address"]["city"]`                  |
| **Default with `get()`** | Use `dictionary.get(key, default)` for safe access with a default value if the key is absent.| `person.get("country", "Not Found")`         |

<p align="right">(<a href="#table-of-contents">back to top</a>)</p>


## 3. Quick Guide to Pygame for the Snake Game

| Function/Method         | Description                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------|
| **`pygame.init()`**      | Initializes all imported Pygame modules. Sets up internal resources like graphics, audio, and input. Returns a tuple indicating the number of successfully initialized modules and failures. |
| **`pygame.display.set_mode()`** | Creates a game window with the specified dimensions `(width, height)`. Additional flags can customize the window (e.g., fullscreen). |
| **`pygame.display.set_caption()`** | Sets the title for the game window, displayed on the border and helping identify the program.                       |
| **`pygame.draw.rect()`** | Draws a rectangle on the screen. Takes parameters like surface, color, and dimensions `(x, y, width, height)`. Commonly used for game elements like the snake or fruit. |
| **`pygame.event.get()`** | Fetches all events currently in the event queue, allowing the program to respond to inputs or system signals. |
| **`pygame.KEYDOWN`**     | Event type triggered when a key is pressed down. The `key` attribute of the event object indicates which key was pressed. |
| **`pygame.QUIT`**        | Event type triggered when the window close button is clicked. Allows the program to terminate gracefully. |
| **`pygame.display.update()`** | Refreshes the entire screen to apply changes made since the last frame. Used when the screen changes and needs updating. |
| **`pygame.time.Clock()`** | Creates a Clock object to manage tasks like controlling the frame rate. Ensures consistent game speed regardless of system performance. |
| **`Clock.tick(fps)`**    | Limits the frame rate of the game to the specified `fps` (frames per second). Regulates game speed by pausing the program for short durations. |

<p align="right">(<a href="#table-of-contents">back to top</a>)</p>

## 4. State-Machine

**What is a State Machine?**
A state machine is a way to organize different parts (or "states") of your game (like menus, gameplay, pause screens)
into separate, self-contained modules. Each state knows how to handle events, update its logic, and draw itself. The
main loop runs once and delegates work to whichever state is currently active. When it’s time to move on—say, from a
menu to the actual game—the state machine "flips" to the new state. This approach keeps code clean, organized, and
easier to maintain.

**Minimal Example:**
Below is a minimal working example using Pygame. It has two states (Menu and Game) and a simple mechanism to switch
between them. Click the mouse in the Menu state to move to the Game state. Press any key in the Game state to quit.

```python
import pygame as pg
import sys

# Base state class
class State:
    def __init__(self):
        self.done = False
        self.next = None

    def startup(self):
        pass
    def cleanup(self):
        pass
    def get_event(self, event):
        pass
    def update(self, screen, dt):
        pass

# Menu state: fill screen red, click to go to Game
class Menu(State):
    def __init__(self):
        super().__init__()
        self.next = 'game'
    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, screen, dt):
        screen.fill((255,0,0))

# Game state: fill screen blue, press key to quit
class Game(State):
    def __init__(self):
        super().__init__()
        self.next = None  # no next state; key press will quit
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            self.done = True
    def update(self, screen, dt):
        screen.fill((0,0,255))

# State machine controller
class App:
    def __init__(self, states, start_state, size=(400,300), fps=60):
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]
        self.running = True

    def flip_state(self):
        self.state.cleanup()
        self.state = self.states[self.state.next]
        self.state.startup()

    def run(self):
        while self.running:
            dt = self.clock.tick(60)/1000.0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                self.state.get_event(event)
            self.state.update(self.screen, dt)
            pg.display.update()

            if self.state.done:
                if self.state.next is None:
                    self.running = False
                else:
                    self.state.done = False
                    self.flip_state()

        pg.quit()
        sys.exit()

if __name__ == '__main__':
    states = {
        'menu': Menu(),
        'game': Game()
    }
    app = App(states, 'menu')
    app.run()
```
