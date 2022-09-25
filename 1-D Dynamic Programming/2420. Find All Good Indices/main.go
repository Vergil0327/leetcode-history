package main

// https://leetcode.com/problems/find-all-good-indices/discuss/2620565/DP-(C%2B%2BJavaPython)-%2B-Intuition
func goodIndicesDP(nums []int, k int) []int {
	n := len(nums)
	dpLeft, dpRight := make([]int, n+1), make([]int, n+1)
	for i := 0; i < len(dpLeft); i++ {
		dpLeft[i] = 1
		dpRight[i] = 1
	}

	for i := 1; i < n; i++ {
		if nums[i] <= nums[i-1] {
			dpLeft[i] = dpLeft[i-1] + 1
		}
	}

	for i := n - 2; i >= 0; i-- {
		if nums[i] <= nums[i+1] {
			dpRight[i] = dpRight[i+1] + 1
		}
	}

	res := []int{}
	for i := k; i < n-k; i++ {
		if dpLeft[i-1] >= k && dpRight[i+1] >= k {
			res = append(res, i)
		}
	}

	return res
}

// [478184,863008,716977,921182,182844,350527,541165,881224], k=1
// length of decreasing from left: [1, 1, 2, 1, 2, 1, 1, 1, 0]
// length of decreasing from right: [2 1 2 1 4 3 2 1 0]
// [2,1,1,1,3,4,1], k=2
// [878724,201541,179099,98437,35765,327555,475851,598885,849470,943442], k=4
// [440043,276285,336957], k=1
// prefix sum array + suffix sum array
// T:O(n) M:O(n)
func goodIndices(nums []int, k int) []int {
	if len(nums) < 2*k+1 {
		return nil
	}

	numGoodFromLeft := make([]int, len(nums)+1)
	validLen := 1
	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i] <= nums[i-1] {
			validLen += 1
			numGoodFromLeft[i] = validLen
		} else {
			validLen = 1
			numGoodFromLeft[i] = validLen
		}
	}

	validLen = 1
	numGoodFromRight := make([]int, len(nums)+1)
	for i := len(nums) - 1; i >= 0; i-- {
		if i+1 < len(nums) && nums[i] <= nums[i+1] {
			validLen += 1
			numGoodFromRight[i] = validLen
		} else {
			validLen = 1
			numGoodFromRight[i] = validLen
		}
	}

	res := []int{}
	for i := k; i < len(nums)-k; i++ {
		if numGoodFromLeft[i-1] >= k && numGoodFromRight[i+1] >= k {
			res = append(res, i)
		}
	}

	return res
}
