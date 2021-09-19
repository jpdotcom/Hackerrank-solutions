from sys import stdin
from collections import Counter

prime = [True for _ in range(8192)]
prime[0] = False
prime[1] = False
for d in range(2, 4096):
    if prime[d]:
        k = 2*d
        while k < 8192:
            prime[k] = False
            k += d

mod = 10**9+7
def f(a):
    cnt = Counter(a)
    a = list(set(a))
    n = len(a)
    dp = [[0]*8192 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for x in range(8192): 
            dp[i][x] = dp[i-1][x] * ((cnt[a[i-1]]+2)/2) + dp[i-1][x ^ a[i-1]] * ((cnt[a[i-1]]+1)/2)
            dp[i][x] %= mod
            
    res = 0
    for x in range(8192):
        if prime[x]:
            res += dp[n][x]
            res %= mod
    return res

a=[3511]
print(f(a))