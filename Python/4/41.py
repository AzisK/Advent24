from Python.utils.read_input import read_input

data = read_input('Input/4.txt')
grid = [list(line) for line in data.strip().split('\n')]

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Search horizontally and horizontally reversed
    for r in range(rows):
        for c in range(cols - word_len + 1):
            if ''.join(grid[r][c:c+word_len]) == word:
                count += 1
            if ''.join(grid[r][c:c+word_len][::-1]) == word:
                count += 1

    # Search vertically and vertically reversed
    for c in range(cols):
        for r in range(rows - word_len + 1):
            if ''.join(grid[r+i][c] for i in range(word_len)) == word:
                count += 1
            if ''.join(grid[r+i][c] for i in range(word_len))[::-1] == word:
                count += 1

    # Search diagonally (top-left to bottom-right) and its reverse
    for r in range(rows - word_len + 1):
        for c in range(cols - word_len + 1):
            if ''.join(grid[r+i][c+i] for i in range(word_len)) == word:
                count += 1
            if ''.join(grid[r+i][c+i] for i in range(word_len))[::-1] == word:
                count += 1

    # Search diagonally (top-right to bottom-left) and its reverse
    for r in range(rows - word_len + 1):
        for c in range(word_len - 1, cols):
            if ''.join(grid[r+i][c-i] for i in range(word_len)) == word:
                count += 1
            if ''.join(grid[r+i][c-i] for i in range(word_len))[::-1] == word:
                count += 1

    return count

word = "XMAS"
count = search_word(grid, word)
print(f"Answer: {count}")
