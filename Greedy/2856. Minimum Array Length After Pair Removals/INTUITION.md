# Intuition

see this: nums = [1,1,2,2,3,3]

the answer is:
```
3 & 2 -> remain: [1,1,2,3]
1 & 2 -> remain: [1,3]
1 & 3 -> remain: []
```

greedily choose first two largest occurence nums[i] and pair them.
the remains should be our answer

the reason why I did this is we want pairs as many as possible, and duplicates can't pair.
therefore, always choose two distinct nums[i] from largest occurence to lowest to avoid duplicates remaining

since duplicates can't make pair, therefore, we want duplicates as less as possible.
=> always choose duplicates to make pairs


# Complexity

- time:
$$O(nlogn)$$
- space
$$O(n)$$

# Code
```
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        
        pq = []
        
        for num, cnt in count.items():
            heapq.heappush(pq, -cnt)

        while len(pq)>1:
            cnt1 = -heapq.heappop(pq)
            cnt2 = -heapq.heappop(pq)
            cnt1 -= 1
            cnt2 -= 1
            if cnt1 > 0:
                heapq.heappush(pq, -cnt1)
            if cnt2 > 0:
                heapq.heappush(pq, -cnt2)

        return -sum(pq)
```