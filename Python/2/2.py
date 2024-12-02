from Python.utils.read_input import read_input

data = read_input('Input/2.txt')

safe_count = 0

def is_safe_sequence(numbers):
    increasing = None
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1] 
        diff_direction = diff > 0
        if increasing is not None and not diff_direction == increasing:
            return False
        increasing = diff_direction
        change = abs(diff)
        if change < 1 or change > 3:
            return False
    return True


for line in data.strip().split('\n'):
    numbers = list(map(int, line.split()))

    ## Good to see ##
    print(numbers)
    ## Good to see ##

    if is_safe_sequence(numbers):
        ## Good to see ##
        print("Safe")
        ## Good to see ##
        safe_count += 1

print(f"Answer: {safe_count}")
