import sys
import math

n_line = sys.stdin.readline().split()
n = int(n_line[0])
types = {}
for x in range(n):
    type, num = sys.stdin.readline().split()
    types[type] = (types.get(type, 0)) + int(num);
sum = 0
for pizza in types.keys():
    sum += math.ceil(types.get(pizza)/8)
print(sum)

