# Blic-Bloc
A remake of Blic-Bloc from The Sims 4!

This program is a fan-game of the Blic-Bloc game of the Sims 4, implemented in Python using Pygame. 
It features falling blocks, randomized tetromino shapes, and a playful interface. Whether you're looking to pass some time
or dive into some creative gameplay, this project is a great mix of coding and entertainment.

# MAIN FEATURES:
- A grid-based game where blocks (tetrominos) fall, and players can move and place them strategically.
- Randomized tetromino shapes with rotations and matching mechanics for an extra layer of challenge.
- A UI displaying the upcoming blocks for better strategic planning.
- Colorful gameplay with dynamic block handling and interaction.

# HOW IT WORKS:
1. The game starts with a 7x5 grid and a set of predefined tetromino shapes (L, Lr, T, Z, Zr, O, and I).
2. Players control a single block that spawns at the top of the grid, moving it left, right, or down.
3. When the block can no longer move down, it "locks" into the grid, and the program checks for matching patterns.
4. Matching patterns (completed tetrominos) are cleared from the grid, making space for new blocks.
5. The game ends when no more blocks can be placed at the top of the grid.

# CLASSES AND METHODS:
- **Game()**: The main class encapsulating the game's logic, UI, and mechanics.
  - `__init__()`: Sets up the game environment, initializes the grid, defines tetrominos, and manages player states.
  - `run(speed: int)`: The game's main loop, controlling frame updates, block movements, and rendering.
  - `draw_grid()`: Renders the grid and the placed blocks.
  - `draw_ui()`: Displays the upcoming tetromino blocks.
  - `move_down()`: Moves the current block down; if blocked, locks it into the grid.
  - `move_left()`, `move_right()`: Allow horizontal movement for the active block.
  - `check_tetrominos(color: int)`: Detects and processes completed tetromino shapes in the grid.
  - `match_pattern(shape, color)`: Checks for a specific tetromino pattern in the grid.
  - `rotate_shape(shape, nb: int)`: Rotates a shape 90° clockwise a specified number of times.
  - `clear_shape(shape)`: Cleans up empty rows/columns from a shape.
  - `destroy_tetromino(y, x, shape)`: Clears a detected tetromino from the grid.
  - `falling_block()`: Handles the natural falling motion of blocks in the grid.
  - `game_over()`: Ends the game when no more moves are possible.

# CONTROLS:
- LEFT Arrow: Move the block to the left.
- RIGHT Arrow: Move the block to the right.
- DOWN Arrow: Speed up the block's descent.

# ADDITIONAL DETAILS:
- Colors are randomly assigned to blocks, making the grid visually lively.
- The tetrominos' order is shuffled in each iteration for unpredictable gameplay.
- Speed can be adjusted by modifying the `speed` parameter in the `run()` method.
---
# TODO
	Score
	Animations
	Levels
	Savings

# TO RUN THE GAME:
Simply execute the script (`python script_name.py`). Pygame and Numpy must be installed in your environment. You can also use a .venv: (https://docs.python.org/3/library/venv.html)

Use the controls to guide the blocks and try to clear as many patterns as you can before the grid fills up!
SUL SUL!
"""
