n = int(input())
nums = list(map(int, input().split()))
 
mn, mx = 1e10, 0
 
from collections import Counter
count = Counter()
for num in nums:
    mn = min(mn, num)
    mx = max(mx, num)
    count[num] += 1
 
from math import comb
print(mx-mn, count[mx] * count[mn] if mx != mn else comb(count[mx], 2))