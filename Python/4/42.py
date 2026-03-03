from Python.utils.read_input import read_input

data = read_input('Input/4.txt')
grid = [list(line) for line in data.strip().split('\n')]

def search_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Define the possible "MAS" sequences
    mas_sequences = ["MAS", "SAM"]

    # Search for the "X-MAS" pattern
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if ''.join([grid[r-1][c-1], grid[r][c], grid[r+1][c+1]]) in mas_sequences and \
                ''.join([grid[r-1][c+1], grid[r][c], grid[r+1][c-1]]) in mas_sequences:
                count += 1

    return count

count = search_x_mas(grid)
print(f"Answer: {count}")
