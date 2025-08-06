# Count the number of pairs of indices (i,j) such that i<j and aj−ai=j−i
# => implies aj-j = ai-i => we can group nums[i] together by this condition
 
# then, the problem reduce to how to calculate valid pairs in each group
# [1,2,3,4]: for 1, has 3 valid right counterpart. for 2, has 2 valid counterpart. ... => (3+2+1) = (1+3)*3/2
# [1,2,3]: same as above
# therefore:
#   if size > 1: valid pairs = (1+(size-1)) * (size-1) / 2
#   if size = 1: valid pairs = 0
 
from collections import defaultdict
 
t = int(input())
for tt in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    group = defaultdict(int) # {key: size}
    for i, num in enumerate(nums):
        group[num-i] += 1
 
    res = 0
    for size in group.values():
        if size > 1:
            res += (1+(size-1)) * (size-1) // 2
    print(res)