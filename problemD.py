import sys

n_line = sys.stdin.readline().split()
n = int(n_line[0])
array = [int(elem) for elem in sys.stdin.readline().strip().split()]

def index(i):
    return i % len(array)

i = 0
while (i < len(array)):
    while (i < len(array) and array[index(i - 1)] == array[i]):
        if (index(i - 1) > i):
            array.pop(index(i - 1))
            array.pop(i)
        else:
            array.pop(i)
            array.pop(index(i - 1))

    if (i < len(array) and array[i] == array[index(i + 1)]):
        if (index(i + 1) > i):
            array.pop(index(i + 1))
            array.pop(i)
        else:
            array.pop(i)
            array.pop(index(i + 1))
    else:
        i += 1

while (len(array) > 0 and array[0] == array[-1]):
    array.pop(-1)
    array.pop(0)

print(array)



