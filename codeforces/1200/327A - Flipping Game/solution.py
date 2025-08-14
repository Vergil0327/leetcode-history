from itertools import accumulate

n = int(input())
nums = list(map(int, input().split()))

presum = list(accumulate(nums, initial=0))

res = 0 # must flip exactly once. minimum value can't be sum(nums). ex. nums = [1] => answer=0
for i in range(n):
    for j in range(i, n):
        # flips nums[i:j+1]
        flips = (j+1-i) - (presum[j+1]-presum[i])
        res = max(res, presum[i] + flips + presum[n]-presum[j+1]) # left + flips + right
print(res)

