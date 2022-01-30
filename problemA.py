import sys

n_line = sys.stdin.readline().split()
n = int(n_line[0])

# Compute dictionary
# number to list of sorted values
mod_to_numbers = {}
numbers_to_mod = {}

for i in range(n):
    mod_result = ((i % n) ** 3) % n
    numbers_to_mod[i] = mod_result
    if mod_result not in mod_to_numbers:
        mod_to_numbers[mod_result] = []
    mod_to_numbers[mod_result].append(i)

result = []

for i in range(n):
    for j in range(i + 1, n):
        current_mod_total = (numbers_to_mod[i] + numbers_to_mod[j]) % n
        mod_goal = (n - current_mod_total) % n
        if mod_goal in mod_to_numbers:
            for elem in mod_to_numbers[mod_goal]:
                if elem > j:
                    result.append((i, j, elem))

print(len(result))
for elem in result:
    print(elem[0], elem[1], elem[2])



