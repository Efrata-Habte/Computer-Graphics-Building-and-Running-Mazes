import pygame
from maze import Labyrinth
from const import ROWS, COLS, FPS, WIDTH, HEIGHT


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
    print("Starting generation...")
    maze.generate_labyrinth(screen)

    # This adds random gaps to create cycles (1 in 20 chance)
    print("Injecting cycles to break the shoulder-to-the-wall rule...")
    maze.create_cycles(probability=20)

    pygame.time.delay(1000)

    # Maze Solving
    print("Starting solver...")
    maze.solve_labyrinth(screen)

    # Final State Loop
    print("Maze completed.")

    while True:
        maze.check_events()
        maze.refresh_view(screen)
        clock.tick(FPS)


if __name__ == "__main__":
    main()
