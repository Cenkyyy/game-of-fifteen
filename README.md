# Game of Fifteen

The Game of Fifteen is a classic sliding puzzle game where the goal is to arrange numbered tiles in a specific order by sliding them into an empty space. This repository contains a Python implementation of the game with two modes of play: using arrow keys or WASD keys.

<img src="https://github.com/user-attachments/assets/ac5c0d5b-b7d0-45b8-8964-95b98d4eb8d9" alt="Game of Fifteen board" width="300"/>

## Game Description

### Objective
Arrange the tiles on a 4x4 grid to match the winning board configuration:

|  1 |  2 |  3 |  4 |
|----|----|----|----|
|  5 |  6 |  7 |  8 |
| 9  | 10 | 11 | 12 |
| 13 | 14 | 15 | __ |

### Game Modes
1. **Play by Arrows**: Use arrow keys to move the tiles. 
   - **Arrow Up**: Move tile up
   - **Arrow Down**: Move tile down
   - **Left Arrow**: Move tile left
   - **Right Arrow**: Move tile right
   - **Left Shift**: Solve the game with AI
   - **Escape**: Exit the game

2. **Play by Keys**: Use WASD keys to move the tiles.
   - **W**: Move tile up
   - **S**: Move tile down
   - **A**: Move tile left
   - **D**: Move tile right
   - **Q**: Solve the game with AI
   - **E**: Exit the game

### Required Installations

Ensure that you have Python installed. The libraries `random`, `time`, and `copy` are built-in, but you'll need to install the **pynput** library. To install **pynput**, follow these steps:
1. Open your terminal.
2. Run: `pip install pynput`

After that, you should be ready to play.

### Possible Improvements

While I'm satisfied with this project as it was my first one, there are some potential improvements which could be made:
- Adding new game board sizes (e.g., 3x3 instead of 4x4)
- Adding an option to restart the game
- Introducing different difficulty levels

### Author

Oliver Tomáš Cenker

### Event 

This game was created during the winter semester of 2023/24 as part of my studies at Charles University, as a credit program for Programming I.

---

### For more information, check [program manual](program%20manual.md). 

---
