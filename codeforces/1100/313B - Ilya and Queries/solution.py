s = input()
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]
 
 
nums = [int(s[i] == s[i+1]) for i in range(len(s)-1)]
 
from itertools import accumulate
presum = list(accumulate(nums, initial=0))
 
for l, r in queries:
    print(presum[r-1] - presum[l-1])