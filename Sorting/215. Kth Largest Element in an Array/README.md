[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

`Medium`

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

```
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

Constraints:

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

see here: [Heap/215. Kth Largest Element in an Array](../../Heap/215.%20Kth%20Largest%20Element%20in%20an%20Array)

<details>
<summary>solution</summary>

```go
func findKthLargest(nums []int, k int) int {
    targetIdx := len(nums) - k

    return quickselect(nums, targetIdx, 0, len(nums)-1)
}

func quickselect(nums []int, target, l, r int) int {
    pivot := nums[r]
    p:=l
    for i:=l;i<r;i++ {
        if nums[i] < pivot {
            nums[i], nums[p] = nums[p], nums[i]
            p+=1
        }
    }
    nums[p], nums[r] = nums[r], nums[p]
    
    if p < target {
        return quickselect(nums, target, p+1, r)
    } else if p > target {
        return quickselect(nums, target, l, p-1 )  
    } else {
        return nums[p]
    }
}
```
</details>