import pygame
import random
import sys

CELL_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (35, 35, 35)
RED = (255, 0, 0)
BLUE = (50, 100, 255)
GREEN = (0, 255, 0)
ROWS = 25
COLS = 25
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 60

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


    def generate_labyrinth(self, screen):
        # Starting mouse position
        start_node = (random.randint(0, self.rows-1), random.randint(0, self.cols-1))
        self.visited[start_node[0]][start_node[1]] = True
        stack = [start_node]

        while stack:
            self.check_events()
            curr_r, curr_c = stack[-1]
            
            # Find neighbors with all 4 walls intact (unvisited)
            neighbors = []
            directions = [(-1, 0, 'N'), (1, 0, 'S'), (0, -1, 'W'), (0, 1, 'E')]
            for dr, dc, label in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and not self.visited[nr][nc]:
                    neighbors.append((nr, nc, label))

            if neighbors:
                nr, nc, direction = random.choice(neighbors)
                # "Eat" the wall
                if direction == 'N': self.north_wall[curr_r][curr_c] = 0
                elif direction == 'S': self.north_wall[nr][nc] = 0
                elif direction == 'E': self.east_wall[curr_r][curr_c+1] = 0
                elif direction == 'W': self.east_wall[curr_r][curr_c] = 0
                
                self.visited[nr][nc] = True
                stack.append((nr, nc))
            else:
                stack.pop()
            
            self.refresh_view(screen, current=(curr_r, curr_c))
            pygame.time.delay(20)

    
    def solve_labyrinth(self, screen):
        solve_stack = [self.entrance]
        solved_visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        solved_visited[self.entrance[0]][self.entrance[1]] = True

        while solve_stack:
            self.check_events()
            curr = solve_stack[-1]
            self.final_route = list(solve_stack)
            self.refresh_view(screen, current=curr)
            pygame.time.delay(40)

            if curr == self.exit: return True

            r, c = curr
            accessible = []
            # Check if walls are missing (0 means wall is eaten/gone)
            if r > 0 and not self.north_wall[r][c]: accessible.append((r-1, c))
            if r < self.rows-1 and not self.north_wall[r+1][c]: accessible.append((r+1, c))
            if c > 0 and not self.east_wall[r][c]: accessible.append((r, c-1))
            if c < self.cols-1 and not self.east_wall[r][c+1]: accessible.append((r, c+1))

            random.shuffle(accessible)
            moved = False
            for nr, nc in accessible:
                if not solved_visited[nr][nc]:
                    solved_visited[nr][nc] = True
                    solve_stack.append((nr, nc))
                    moved = True
                    break
            
            if not moved:
                self.dead_end_markers.add(solve_stack.pop())
        return False
    

    def create_cycles(self, probability=20):
        # 1 in 20 chance to eat an extra wall
        for r in range(1, self.rows):
            for c in range(1, self.cols):
                if random.randint(1, probability) == 1:
                    if random.choice([True, False]):
                        self.north_wall[r][c] = 0
                    else:
                        self.east_wall[r][c] = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()