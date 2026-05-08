# Maze Generator and Solver

A Python-based maze generation and solving visualization using Pygame. This project demonstrates computer graphics concepts by creating mazes using a randomized depth-first search algorithm and solving them with a backtracking algorithm.

## Features

- **Real-time Maze Generation**: Watch as the maze is carved out using a randomized depth-first search algorithm
- **Interactive Solving**: See the solver navigate through the maze using backtracking
- **Visual Feedback**: Different colors represent different elements:
  - **White lines**: Maze walls
  - **Red circle**: Current position during generation/solving
  - **Yellow squares**: Dead ends discovered during solving
  - **Green squares**: Final solution path
- **Cycle Injection**: Random wall removals to create multiple solution paths
- **Smooth Animations**: Configurable animation speeds for generation and solving

## Requirements

- Python 3.6+
- Pygame library

## Installation

1. Ensure you have Python 3.6 or higher installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```

## How to Run

1. Navigate to the project directory
2. Run the main script:
   ```bash
   python main.py
   ```

## What You'll See

The program will display a window showing:

1. **Maze Generation Phase**: A red circle moves through the grid, "eating" walls to create passages
2. **Cycle Injection**: Brief pause while additional openings are added to prevent dead-end traps
3. **Maze Solving Phase**: The red circle navigates from start to finish, marking dead ends in yellow
4. **Final Result**: The complete maze with the solution path shown in green

## Controls

- **Close Window**: Click the X button in the window title bar to exit

## Technical Details

- **Maze Size**: 20x20 grid (configurable via ROWS and COLS constants)
- **Cell Size**: 30 pixels per cell
- **Generation Algorithm**: Randomized Depth-First Search
- **Solving Algorithm**: Backtracking with cycle detection
- **Frame Rate**: 60 FPS

## Project Structure

```
├── main.py          # Main entry point and game loop
├── maze.py          # Maze class with generation and solving logic
└── README.md        # This file
```

## Algorithm Overview

### Maze Generation

Uses a randomized depth-first search to create a perfect maze (no loops, fully connected). The algorithm:

1. Starts at a random cell
2. Explores neighboring cells randomly
3. Removes walls between visited cells
4. Backtracks when no unvisited neighbors remain

### Maze Solving

Implements a backtracking solver that:

1. Starts at the entrance (top-left)
2. Explores paths systematically
3. Marks dead ends when backtracking
4. Continues until reaching the exit (bottom-right)

### Cycle Injection

Adds random wall removals (1 in 20 chance) to create alternative paths, making the maze more interesting and preventing the "wall follower" paradox.

## Customization

You can modify the constants in `main.py` and `maze.py`:

- `ROWS`, `COLS`: Maze dimensions
- `CELL_SIZE`: Visual cell size
- Animation delays in `generate_labyrinth()` and `solve_labyrinth()` methods
- Color values for different visual elements

## License

This project is open source and available under the MIT License.
