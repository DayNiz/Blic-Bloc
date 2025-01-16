# Blic-Bloc
A remake of Blic-Bloc from The Sims 4!

This program is a fan-game of the Blic-Bloc game of the Sims 4, implemented in Python using Pygame. 

# MAIN FEATURES:
- Choose you speed in the menu. They are separated in 3 categories, Easy, Hard, and Impossible.
- A grid-based game where blocks fall, and players place them strategically.
- Assemble the block to create tetrominos.
- The two next block color are shown for better strategic planning.

# HOW IT WORKS:
1. The game starts with a 7x5 grid and a set of predefined tetromino shapes (L, Lr, T, Z, Zr, O, and I).
2. Players control a single block that spawns at the top center of the grid, moving it left, right, or down.
3. When the block can no longer move down, it "locks" into the grid, and the program checks for matching patterns.
4. Completed tetrominos are cleared from the grid, making space for new blocks, leading to cascade of tetrominos and falling blocks.
   (There may be some bugs here, the algo is not quite perfect...)
6. The game ends when no more blocks can be placed at the top of the grid.

# CONTROLS:
- LEFT Arrow: Move the block to the left.
- RIGHT Arrow: Move the block to the right.
- DOWN Arrow: Speed up the block's descent.

# TO-DO / Roadmap:
- Saving score on exit.
- Animations when block are destroyed.
- Change the Game-Over Screen to the Sims one.
---

# TO RUN THE GAME:
Simply execute the script (`python script_name.py`). Pygame, Pygame-menu and Numpy must be installed in your environment.

Use the controls to guide the blocks and try to clear as many patterns as you can before the grid fills up!
SUL SUL!
