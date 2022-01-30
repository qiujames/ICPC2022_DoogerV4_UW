import sys

n_line = sys.stdin.readline().split()
n = int(n_line[0])
array = [int(elem) for elem in sys.stdin.readline().strip().split()]

i = 0
ans = []
for elem in array:
    if len(ans) == 0:
        ans.append(elem)
    else:
        if (ans[-1] == elem):
            ans.pop()
        else:
            ans.append(elem)

j = 0
k = len(ans) - 1
while (j < k and ans[j] == ans[k]):
    j += 1
    k -= 1

print(k - j + 1)



