package main

// https://leetcode.com/problems/minimize-maximum-of-array/discuss/2706521/JavaC%2B%2BPython-Prefix-Sum-Average-O(n)

// Intuition
// In one operation:
// decrease A[i] by 1.
// increase A[i - 1] by 1.

// We actully move the value of A[i] to A[i - 1] by 1,
// the sum won't change.

// If A[i] < A[i + 1],
// then we can repeatly do the operations,
// until A[i] >= A[i+1].
// So finally the array A will become descending order.

// Explanation
// We calculate the prefix sum arrray and their average.
// The average is the lower bound of the result,
// and it's reachable lower bound by the process in intuition,
// so this average is the result.

// https://leetcode.com/problems/minimize-maximum-of-array/discuss/2706384/Python-Elegant-and-Short-or-Commented-or-O(n)-or-Prefix-Average
// The idea is dynamic programming. Think of the numbers representing bar heights.
// The operation essentially allows us to re-allocate the height from the bar to whatever bars to its left. And the sum of bar heights will always remain unchanged.
// Then we want to find the minimum height such that we can fit every new bar under such height.
// So starting from left to right, let dp[i] represents the answer of nums[0:(i+1)], when nums[i+1] come in, we compare it to dp[i]:

// If nums[i+1] <= dp[i], we don't want to re-allocate its height, because if the left bars are all of the height dp[i], then we might risk increasing the minimum height limit.
// But if nums[i+1] > dp[i], we want to allocate the extra height to the left as evenly as possible.

func minimizeArrayValue(nums []int) int {
	minMax := 0
	sum := 0
	for i, num := range nums {
		sum += num

		// https://leetcode.com/problems/minimize-maximum-of-array/discuss/2706472/Average
		// the best we can get is math.Ceil(sum) at every calcuation
		// round up average
		// To round up two integer division a/b without using ceil(), we do (a+b-1)/b
		avg := (sum + (i + 1) - 1) / (i + 1)
		minMax = max(minMax, avg)
	}

	return minMax
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}

// https://leetcode.com/problems/minimize-maximum-of-array/discuss/2706375/Binary-Search-or-With-explanation
// https://leetcode.com/problems/minimize-maximum-of-array/discuss/2706361/C%2B%2B-or-Binary-search
// whenever Problem saying you have to minimize the maximum or maximize the minimum then 90% of the cases binary Search on answer can be applied
// Time complexity should be O(nlogm) where m = max(nums) <= 1e9
func minimizeArrayValueBinSearch(nums []int) int {
	maxVal := 0
	for _, num := range nums {
		if num > maxVal {
			maxVal = num
		}
	}

	// we want minimum possible value of maximum num in array
	// => upperbound
	l, r := 0, maxVal
	for l < r {
		mid := l + (r-l)/2
		if check(nums, mid) {
			r = mid
		} else {
			l = mid + 1
		}
	}

	return l
}

// Choose an integer i such that 1 <= i < n and nums[i] > 0.
// Decrease nums[i] by 1.
// Increase nums[i - 1] by 1.
// ex. [3,7,1,6], ans = 5

func check(nums []int, mid int) bool {
	if mid < nums[0] {
		return false
	}

	prev := nums[0]
	for i := 1; i < len(nums); i++ {
		diff := mid - prev
		prev = nums[i] - diff
		if prev > mid {
			return false
		}
	}

	return true
}
