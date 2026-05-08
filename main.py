import pygame
from maze import Labyrinth
from const import ROWS, COLS, FPS, WIDTH, HEIGHT

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Eating Mouse: Maze Generator")
    
    clock = pygame.time.Clock()
    
    # Initialize using the Labyrinth class structure
    labyrinth = Labyrinth(ROWS, COLS)
    
    # Draw initial grid before starting
    labyrinth.refresh_view(screen)