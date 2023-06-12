# Intuition

permutiotion: ex. [a,b,c]
a b c
a c b
b a c
b c a
c a b
c b a
=> choose any subset of nums for our request.

since constraints are large:
- 0 <= nums[i] <= 10^5
- 1 <= n <= 10^5 
- 1 <= requests.length <= 10^5

first? I'm thinking how to maximum our total sum?

use diff array to mark our wanted interval
=> [1,1,-1,0,-1]
=> [1,2,1,1,0]
=> value of diff[i] means how many count for nums[i] contribute to sum.
    => think diff[i] is contribution
=> use maxHeap to greedily put max nums[i] in these position from larger count to lower (another maxHeap)

```py
numContribution = [-contrib for contrib in diff if contrib > 0]
heapq.heapify(numContribution)

maxNumHeap = [-num for num in nums]
heapq.heapify(maxNumHeap)

mod = 10**9+7
res = 0
while numContribution:
    cnt = -heapq.heappop(numContribution)
    currMaxNum = -heapq.heappop(maxNumHeap)
    res = (res + cnt * currMaxNum) % mod
return res
```

time: O(nlogn)

# Optimization

actually, we don't need max heap.
we can just sort the `diff` array and nums

```py
nums.sort(reverse=True)
diff.sort(reverse=True)

res = 0
mod = 10**9+7
for num, cnt in zip(nums, diff):
    res = (res + num * cnt) % mod
return res
```