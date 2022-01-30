import sys

n_line = sys.stdin.readline().split()
n = int(n_line[0])
array = [int(elem) for elem in sys.stdin.readline().strip().split()]

def index(i):
    return i % len(array)

i = 0
while (i < len(array)):
    next_index = index(i + 1)
    if (array[next_index] == array[i]):

        if (next_index > i):
            array.pop(next_index)
            array.pop(i)
        else:
            array.pop(i)
            array.pop(next_index)
        i = max(0, i - 1)
    else:
        i += 1

while (len(array) > 0 and array[0] == array[-1]):
    array.pop(-1)
    array.pop(0)

print(len(array))



