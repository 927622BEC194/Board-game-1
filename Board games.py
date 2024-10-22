from collections import deque

# Function to rotate a vector by 90 degrees clockwise
def rotate_clockwise(x, y):
    return y, -x

# Function to rotate a vector by 90 degrees counterclockwise
def rotate_counterclockwise(x, y):
    return -y, x

# Function to rotate a vector by 180 degrees
def rotate_180(x, y):
    return -x, -y

def is_valid(nx, ny, M, N, grid):
    return 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0

def bfs(grid, M, N, start, end, move_rule):
    sx, sy = start
    ex, ey = end
    move_x, move_y = move_rule
    
    # Direction vectors: forward, right (90 clockwise), left (90 anticlockwise), backward (180 degrees)
    directions = [
        (move_x, move_y),                        # Forward
        rotate_clockwise(move_x, move_y),        # Right
        rotate_counterclockwise(move_x, move_y), # Left
        rotate_180(move_x, move_y)               # Backward
    ]
    
    # BFS setup
    queue = deque([(sx, sy, 0)])  # (x, y, steps)
    visited = set([(sx, sy)])
    
    while queue:
        x, y, steps = queue.popleft()
        
        # If we reached the destination
        if (x, y) == (ex, ey):
            return steps
        
        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny, M, N, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    # If no path is found
    return -1

# Input parsing
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
source = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))
move_rule = tuple(map(int, input().split()))

# Output the result of the BFS
print(bfs(grid, M, N, source, destination, move_rule))
