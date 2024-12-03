import math
import re

from Python.utils.read_input import read_input

data = read_input('Input/3.txt')

# Define the regex pattern
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches in the data
matches = re.findall(pattern, data)

# Iterate over the matches, multiply the numbers, and sum them up
answer = sum([math.prod(map(int, match)) for match in matches])

## Good to see ##
# ANSI escape code for green text
GREEN = '\033[92m'
RESET = '\033[0m'

# Highlight matches in green
highlighted_data = re.sub(pattern, lambda m: f"{GREEN}{m.group(0)}{RESET}", data)
## Good to see ##

print(f"Total sum of products: {answer}")

## Good to see ##
print("Highlighted text:")
print(highlighted_data)
## Good to see ##
