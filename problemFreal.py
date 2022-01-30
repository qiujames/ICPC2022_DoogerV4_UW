import sys
import itertools

n_line = sys.stdin.readline().split()
n = int(n_line[0])
my_list = [int(elem) for elem in sys.stdin.readline().strip().split()]
list_of_lists = []
for x in range(n - 1):
    values = sys.stdin.readline().strip().split()
    list_of_lists.append([int(elem) for elem in values])

def didWin(picks, us):

    if(us > max(picks)):
        return True
    counts = {}
    for elem in picks:
        if elem not in counts:
            counts[elem] = 0
        counts[elem] += 1
    max_num = -1
    unique = False
    for elem in counts:
        if counts[elem] == 1 and elem > max_num:
            max_num = elem
            unique = True
    if unique:
        if (max_num > us):
            return False

    if (len(counts) == 1):
        return True

    for elem in counts:
        if elem == us:
            return False
    return True

total = 0
best_choice = my_list[0]
possibilities = list(itertools.product(*list_of_lists))

for my_choice in my_list:
    cur_total = 0
    for choices in possibilities:
        if didWin(choices, my_choice):
            print(my_choice, choices, "won")
            cur_total += 1
        if (cur_total > total):
            total = cur_total
            best_choice = my_choice

print(best_choice)
print(total / (5 ** (n-1)))