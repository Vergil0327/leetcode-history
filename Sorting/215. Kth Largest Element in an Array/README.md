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