(n, d) = map(int, input().split())
mod = 10 ** 9 + 7

if n == 0:
    print(1)
elif d == 0:
    print(0)
elif n < d:
    print(int(2 ** n % mod))
else:
    dp = [0] * (d + 1)
    dp[0] = 1
    for i in range(n):
        next_dp = [0] * (d + 1)
        next_dp[1] = int((dp[0] * 2) % mod)
        next_dp[d-1] = int((next_dp[d-1] + dp[d]) % mod)
        for j in range(1, d):
            next_dp[j-1] = int((next_dp[j-1] + dp[j]) % mod)
            next_dp[j+1] = int((next_dp[j + 1] + dp[j]) % mod)
        dp = next_dp

    print(int(sum(dp) % mod))


