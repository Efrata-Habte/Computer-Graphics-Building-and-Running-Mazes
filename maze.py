import pygame
import random
import sys
from const import CELL_SIZE, WHITE, BLACK, RED, BLUE, GREEN, WIDTH, HEIGHT

class Labyrinth:
    def __init__(self, R, C):
        self.rows = R
        self.cols = C
        
        # add 1 to dimensions to handle the 'phantom' bottom/left edges
        self.north_wall = [[1 for _ in range(C)] for _ in range(R + 1)]
        self.east_wall = [[1 for _ in range(C + 1)] for _ in range(R)]
        
        self.visited = [[False for _ in range(C)] for _ in range(R)]
        self.path_stack = []
        self.dead_end_markers = set()
        self.final_route = []
        
        self.entrance = (0, 0)
        self.exit = (R - 1, C - 1)

        def refresh_view(self, screen, current=None):
            screen.fill(BLACK)
            
            # Draw dead ends found during solving
            for r, c in self.dead_end_markers:
                pygame.draw.rect(screen, BLUE, (c*CELL_SIZE+4, r*CELL_SIZE+4, CELL_SIZE-8, CELL_SIZE-8))
            
            # Draw the current path stack
            for r, c in self.final_route:
                pygame.draw.rect(screen, GREEN, (c*CELL_SIZE+6, r*CELL_SIZE+6, CELL_SIZE-12, CELL_SIZE-12))

            # Render walls
            for r in range(self.rows):
                for c in range(self.cols):
                    x, y = c * CELL_SIZE, r * CELL_SIZE
                    # North wall of current cell
                    if self.north_wall[r][c]:
                        pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 2)
                    # East wall of current cell
                    if self.east_wall[r][c+1]:
                        pygame.draw.line(screen, WHITE, (x+CELL_SIZE, y), (x+CELL_SIZE, y+CELL_SIZE), 2)
            
            # Draw Phantom Left Edge (east_wall index 0)
            for r in range(self.rows):
                if self.east_wall[r][0]:
                    pygame.draw.line(screen, WHITE, (0, r*CELL_SIZE), (0, (r+1)*CELL_SIZE), 2)
                    
            # Draw Phantom Bottom Edge (north_wall index 0)
            for c in range(self.cols):
                if self.north_wall[0][c]:
                    pygame.draw.line(screen, WHITE, (c*CELL_SIZE, HEIGHT), ((c+1)*CELL_SIZE, HEIGHT), 2)

            if current:
                pygame.draw.circle(screen, RED, (current[1]*CELL_SIZE + CELL_SIZE//2, current[0]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)
            
            pygame.display.flip()