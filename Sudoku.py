def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_safe(grid, row, col, num):
    # Check if 'num' is not in the current row
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    # Check if 'num' is not in the current column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    # Find an empty location
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # No empty location means the puzzle is solved

    row, col = empty_location

    # Consider digits 1 to 9
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Reset if the assumption was wrong

    return False

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

# Example Sudoku puzzle (0 means empty cell)
example_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(example_grid):
    print("Sudoku grid solved successfully!")
    print_grid(example_grid)
else:
    print("No solution exists.")
