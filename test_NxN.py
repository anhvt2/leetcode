import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def find_largest_square(grid):
    """
    Finds the largest N x N square consisting of 1s within a binary grid.
    
    Args:
        grid (np.ndarray): 2D numpy array of 0s and 1s representing the binary grid.
    
    Returns:
        max_size (int): Side length N of the largest square.
        top_left (tuple): Coordinates (row, col) of the top-left corner of that square.
    """

    # Dimensions of the grid
    rows, cols = grid.shape
    
    # Dynamic programming (DP) table to store largest square size ending at (i, j)
    dp = np.zeros((rows, cols), dtype=int)
    
    # Track maximum square size and its bottom-right corner location
    max_size = 0
    max_i = 0
    max_j = 0

    # Loop through every cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:  # Only consider cells with value 1
                if i == 0 or j == 0:
                    # First row or first column → max square ending here is just 1x1
                    dp[i, j] = 1
                else:
                    # Transition relation:
                    # The size of the largest square ending at (i, j) depends on its
                    # top, left, and top-left neighbors in the DP table
                    dp[i, j] = min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]) + 1

                # Update max if we found a bigger square
                if dp[i, j] > max_size:
                    max_size = dp[i, j]
                    max_i, max_j = i, j  # store bottom-right corner of largest square

    # Compute top-left corner of the largest square
    top_left = (max_i - max_size + 1, max_j - max_size + 1)
    
    return max_size, top_left


# Generate a 512x512 random blob using random circles
np.random.seed(42)
size = 512
blob = np.zeros((size, size), dtype=int)
num_circles = 10
for _ in range(num_circles):
    # Random center and radius
    cy, cx = np.random.randint(0, size, 2)
    r = np.random.randint(30, 100)
    y, x = np.ogrid[:size, :size]
    mask = (y - cy)**2 + (x - cx)**2 <= r**2
    blob[mask] = 1

# Find largest square
square_size, (r0, c0) = find_largest_square(blob)

# Plot the blob and overlay the largest square
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(blob, cmap='gray', origin='lower')
if square_size > 0:
    rect = Rectangle((c0 - 0.5, r0 - 0.5), square_size, square_size,
                     fill=False, linewidth=2, edgecolor='red')
    ax.add_patch(rect)

ax.set_title(f"512×512 Random Blob\nLargest Square: Size = {square_size} at (row={r0}, col={c0})")
ax.set_xlabel("Column")
ax.set_ylabel("Row")
plt.tight_layout()
plt.show()
