"""
排序後用binary search去猜測`x`, 然後去檢查所有`<= x`的元素是不是剛好k個
"""

[n, k] = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()

import bisect

l, r = -1, 10**9

flag = 1
while l <= r:
    mid = l + (r-l)//2
    x = bisect.bisect_right(nums, mid)
    if x == k:
        print(mid)
        flag = 0
        break
    elif x > k:
        r = mid-1
    else:
        l = mid+1
if flag:
    print(-1)