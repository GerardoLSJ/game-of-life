import numpy as np

def life(grid):
    """
    Conway's Game of Life step function
    Takes a 2D boolean array and returns the next generation
    """
    # Get dimensions
    rows, cols = grid.shape
    
    # Create padded grid to handle edges
    padded = np.pad(grid, 1, mode='constant', constant_values=False)
    
    # Count neighbors for each cell
    neighbors = np.zeros_like(grid, dtype=int)
    
    # Sum all 8 neighboring positions
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the center cell
            neighbors += padded[1+i:rows+1+i, 1+j:cols+1+j]
    
    # Apply Game of Life rules:
    # 1. Any live cell with 2 or 3 neighbors survives
    # 2. Any dead cell with exactly 3 neighbors becomes alive
    # 3. All other cells die or stay dead
    
    next_gen = (neighbors == 3) | (grid & (neighbors == 2))
    
    return next_gen

# Example usage with a glider pattern
def demo():
    # Create a 10x10 grid with a glider pattern
    grid = np.zeros((10, 10), dtype=bool)
    
    # Glider pattern
    glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    for r, c in glider:
        grid[r, c] = True
    
    print("Initial state:")
    print_grid(grid)
    
    # Run 5 generations
    for gen in range(5):
        grid = life(grid)
        print(f"\nGeneration {gen + 1}:")
        print_grid(grid)

def print_grid(grid):
    """Print grid with * for alive cells and . for dead cells"""
    for row in grid:
        print(''.join('*' if cell else '.' for cell in row))

if __name__ == "__main__":
    demo()