import pygame
import random
import sys
from const import CELL_SIZE, WHITE, BLACK, RED, BLUE, GREEN, WIDTH, HEIGHT

class Labyrinth:
    def __init__(self, R, C):
        self.rows = R
        self.cols = C
        
        # Instructor requirement: northWall and eastWall
        # We add 1 to dimensions to handle the 'phantom' bottom/left edges
        self.north_wall = [[1 for _ in range(C)] for _ in range(R + 1)]
        self.east_wall = [[1 for _ in range(C + 1)] for _ in range(R)]
        
        self.visited = [[False for _ in range(C)] for _ in range(R)]
        self.path_stack = []
        self.dead_end_markers = set()
        self.final_route = []
        
        self.entrance = (0, 0)
        self.exit = (R - 1, C - 1)