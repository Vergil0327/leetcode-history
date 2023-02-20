# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
find first `>=` position. it's either insert position we want or target itself

# Complexity
- Time complexity:
$$O(log(n))$$

- Space complexity:
$$O(1)$$

# Code

```go
func searchInsert(nums []int, target int) int {
    l, r := 0, len(nums)
    for l < r {
        mid := l + (r-l)/2
        if nums[mid] < target {
            l = mid + 1
        } else {
            r = mid
        }
    }

    return l
}
```


```py
# equals bisect.bisect_left in python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        return l
```