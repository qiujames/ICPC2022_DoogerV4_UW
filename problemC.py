import sys
from itertools import combinations

def get_all_substrings_2(string):
    length = len(string) + 1
    return [string[x:y] for x, y in combinations(range(length), r=2)]

n_line = sys.stdin.readline().split()
n = int(n_line[0])
song = ""
for n in range(n):
    song += sys.stdin.readline();

substrings = get_all_substrings_2(song)
occurences = {}
for substring in substrings:
    occurences[substring] = occurences.get(substring, 0) + 1

choruses = {k:v for (k,v) in occurences.items() if v >= 3}
print(max(choruses.keys(), key=len))