# Intuition

come up with this dp definition fn intuitively:
`dp[i][num]: the number of distinct idea arrays of length `i` ended with `num``

and it's easily to come up with state transfer fn:

```py
for num in range(1, maxValue+1):
    dp[num] = 1

for i in range(2, n+1):
    for v in range(1, maxValue+1):
        for num in range(1, v+1):
            if v%num == 0:
                dp[i][v] += dp[i-1][num]
                dp[i][v] %= mod
return sum(dp[n])% mod
```

but this will TLE. even two loops O(n^2) cause TLE.

we need an efficient way to find divisible num -> prime factors
```
ideal = [X X X Max]

if Max=30:

30 = 2*3*5
   => [1,1,1,2*3*5*previous] = [1,1,1,30]
   => [1,1,2,3*5*previous] = [1,1,2,30]
   => [1,1,3,2*5*previous] = [1,1,3,30]
   => [1,1,5,2*3*previous] = [1,1,5,30]
   => [1,2,3*previous,5*previous] = [1,2,6,30]
   => put prime factors (2, 3, 5) into n positions

what if we have more than 1 for each prime factor?

what if n = 2 and Max = 4 = 2*2 ?

[2] [2] = [2,2]
[2] [2] = [2,2]
[2,2] [] = [4,4]
[] [2,2] = [1,4]

we got duplicate ideal subarray for first 2 results
```

thus, what we really want is to find **dp[n][k]: how many distinct plans to place k same factors in n places, (allowing multiple factors in the same place)** for each value

`dp[i][j] = sum(dp[i-1][j-t] for t = 0, 1, 2, 3, ..., j)` where `t` is the number of same factors in `i` position

```
for i in range(1, n+1):
    for j in range(k+1):
        for t in rnage(j+1):
            dp[i][j] += dp[i-1][j-t]

time = O(N*K*K) = (10^4 * 14 * 14)
maxValue <= 10^4
the smallest prime factor is 2 -> 2^13 < 10^4 < 2^14 -> K=14 at most
```

then we iterate num from 1 to maxValue.
find each num's prime and the number of prime `count`
each prime contributes `dp[n][count]` ways

```py
res = 0
for v in range(1, maxValue+1):
    ways = 1
    
    num = v
    for p in primes:
        count = 0
        while num > 1 and num%p == 0:
            num //= p
            count += 1
        
        ways = ways * dp[n][count] % mod
    res = (res + ways) % mod
```