from itertools import accumulate
from bisect import bisect_left
 
n = int(input())
piles = list(map(int, input().split()))
 
presum = list(accumulate(piles))
 
m = int(input())
queries = list(map(int, input().split()))
for i in range(m):
    print(bisect_left(presum, queries[i]) + 1) # to 1-indexed


"""
Intuition

juicy worm的label是累計的,
可利用prefix sum + binary search找出每個queries[i] (juicy worm)落在哪個piles[j]裡
"""