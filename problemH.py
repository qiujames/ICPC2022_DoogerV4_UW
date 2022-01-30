import sys

coordline = sys.stdin.readline()
x, y, i, j = coordline.split()
x = float(x)
y = float(y)
i = float(i)
j = float(j)
n_line = sys.stdin.readline().split()
n = int(n_line[0])
ans = 0
for z in range(n):
    a, b, c = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    num1 = a * x + b * y
    num2 = a * i + b * j
    if((num1-c)*(num2-c) < 0):
        ans += 1
print(ans)

