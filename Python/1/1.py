from Python.utils.read_input import read_input


def process_input(file_path):
    data = read_input(file_path)
    left = []
    right = []
    
    for line in data.strip().split('\n'):
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    
    left.sort()
    right.sort()
    
    return left, right

left, right = process_input('Input/1.txt')

## Good to see ##
print("Left\tRight\tDifference")
for l, r in zip(left, right):
    print(f"{l}\t{r}\t{abs(r - l)}")
## Good to see ##

answer = sum([abs(r - l) for l, r in zip(left, right)])

print(f"Answer: {answer}")


