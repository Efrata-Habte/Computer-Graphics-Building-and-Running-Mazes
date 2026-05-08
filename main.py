import pygame
from maze import Labyrinth

ROWS = 25
COLS = 25
CELL_SIZE = 30
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 60


def main():
    # Initialize the Pygame engine
    pygame.init()

    # Setup the display surface and window title
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Project: The Eating Mouse & Backtracking Solver")

    # Clock to control frame rate for the final display
    clock = pygame.time.Clock()

    # Initialize our Labyrinth object with specified dimensions
    maze = Labyrinth(ROWS, COLS)

    # Maze Generation
    # This shows the "mouse" eating through walls dynamically
    print("Starting generation...")
    maze.generate_labyrinth(screen)

    # Add Addendum Features
    # This adds random gaps to create cycles (1 in 20 chance)
    print("Injecting cycles to break the shoulder-to-the-wall rule...")
    maze.create_cycles(probability=20)

    # Brief pause so the viewer can see the completed maze before solving
    pygame.time.delay(1000)

    # Maze Solving
    # This shows the red dot moving and yellow dots marking dead ends
    print("Starting solver...")
    maze.solve_labyrinth(screen)

    # Final State Loop
    # Keep the window open so the user can see the final path
    print("Maze completed.")
    while True:
        maze.check_events()

        maze.refresh_view(screen)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
