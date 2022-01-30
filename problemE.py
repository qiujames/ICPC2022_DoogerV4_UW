import sys

n, x, y = sys.stdin.readline().split()
n = int(n)
x = int(x)
y = int(y)
array = [int(elem) for elem in sys.stdin.readline().strip().split()]

total = 0
result = []
for i in range(y + 1, n + 1):
    # print(array[i - 1], "result", i - 1)
    if (total <= 0):
        result.append("+")
        total += array[i - 1]
    else:
        result.append("-")
        total -= array[i - 1]


total = array[y - 1]
reversed_rest = []
i = y
while (i >= 1):
    # print(array[i - 1], "result", i - 1)
    if (total <= 0):
        reversed_rest.append("+")
        total += array[i - 1]
    else:
        reversed_rest.append("-")
        total -= array[i - 1]
    i -= 1
reversed_rest.reverse()

reversed_rest.extend(result)
print(" ".join(reversed_rest))

# total_1 = 0
# total_2 = 0
# total_3 = 0
# for count, elem in enumerate(reversed_rest, 1):
#     print(count)
#     if (elem == "+"):
#         total_1 += array[count - 1]
#         if (count > x):
#             total_2 += array[count - 1]
#         if (count > y):
#             total_3 += array[count - 1]
#     else:
#         total_1 -= array[count - 1]
#         if (count > x):
#             total_2 -= array[count - 1]
#         if (count > y):
#             total_3 -= array[count - 1]
#
#     if (abs(total_1) >= 180 or abs(total_2) >= 180 or abs(total-3) >= 180):
#         print(result)
#         print(reversed_rest)
#         print(count)
#         raise Exception("Ripp")
