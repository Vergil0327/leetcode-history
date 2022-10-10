[698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

`Medium`

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

```
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false
```

Constraints:

- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= 10^4
- The frequency of each element is in the range [1, 4].

<details>
<summary>Hint</summary>

We can figure out what target each subset must sum to. Then, let's recursively search, where at each call to our function, we choose which of k subsets the next value will join.
</details>



<details>
<summary>Solution</summary>

```go
func canPartitionKSubsets(nums []int, k int) bool {
    if k == 1 { return true }
    sum := 0
    max := 0
    for _, v := range nums {
        sum += v
        if v > max { max = v }
    }
    if sum % k != 0 || max > sum / k { return false }
    sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
    seen := make([]bool, len(nums))
    return dfs(nums, seen, 0, 0, k, sum / k)
}

func dfs(nums []int, seen []bool, start, sum, k, target int) bool {
    if k == 1 { return true }
    if sum == target { return dfs(nums, seen, 0, 0, k - 1, target) }
    for i := start; i < len(nums); i++ {
        if !seen[i] && sum + nums[i] <= target {
            seen[i] = true
            if dfs(nums, seen, i + 1, nums[i] + sum, k, target) { return true }
            seen[i] = false
        }
    }
    return false
}
```

```go
func canPartitionKSubsets(nums []int, k int) bool {
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }
    
    if totalSum % k != 0 {
        return false
    }
    
    sort.Ints(nums)
    subSetSum := totalSum / k
    cache := make(map[int]bool)
    mask := 0
    
    return dfs(len(nums)-1, 0, k, 0, subSetSum, mask, nums, cache)
}

func dfs(idx, groupId, k, sum, subSetSum, mask int, nums []int, cache map[int]bool) bool {
    // If we find k-1, then even kth will be subSetSum
    if groupId == k-1 {
        return true
    }
    
    if sum == subSetSum  {
        return dfs(len(nums)-1, groupId+1, k, 0, subSetSum, mask, nums, cache)
    }
    
    if sum > subSetSum {
        return false
    }
    
    // This is primarly used to return false
    if value, ok := cache[mask]; ok {
        return value
    }
    
    for i := idx; i >= 0; i-- {
        if mask & (1 << i) == 0 {
            mask = mask | (1 << i)
            if dfs(i-1, groupId, k, sum+nums[i], subSetSum, mask, nums, cache) {
                return true
            }
            mask = mask ^ (1 << i)
        }
    }
    
    cache[mask] = false
    return false
}
```
</details>