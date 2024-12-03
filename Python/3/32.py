import math
import re

from Python.utils.read_input import read_input

data = read_input('Input/3.txt')

# Define the regex patterns
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Find all matches in the data
mul_matches = re.finditer(mul_pattern, data)
do_matches = re.finditer(do_pattern, data)
dont_matches = re.finditer(dont_pattern, data)

# Combine all matches and sort by their position in the text
all_matches = sorted(
    list(mul_matches) + list(do_matches) + list(dont_matches),
    key=lambda m: m.start()
)

# Initialize variables
enabled = True
total_sum = 0

# Process each match
for match in all_matches:
    if match.re.pattern == do_pattern:
        enabled = True
    elif match.re.pattern == dont_pattern:
        enabled = False
    elif match.re.pattern == mul_pattern and enabled:
        total_sum += math.prod(map(int, match.groups()))

print(f"Total sum of products: {total_sum}")
