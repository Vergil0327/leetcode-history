# 目標是找出符合小於等於k的n的最大因數
# 1. 如果k >= n, 那麼最大因數就是n自身
# 2. 再來就是找出所有因數, 然後排序. 透過二分找出第一個小於等於k的因數即為答案


import math
import bisect

t = int(input())
        
for _ in range(t):
    n, k = list(map(int, input().split()))
    if k >= n:
        print(1)
        continue

    factors = []
    for i in range(1, math.isqrt(n)+1):
        if n%i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
    factors = list(sorted(factors))

    idx = bisect.bisect_right(factors, k)-1
    print(n // factors[idx])