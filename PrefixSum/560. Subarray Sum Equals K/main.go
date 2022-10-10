package main

func subarraySum(nums []int, k int) int {
	count := 0

	sumCount := map[int]int{}
	prefixSum := make([]int, len(nums)+1)
	for i, num := range nums {
		prefixSum[i+1] = prefixSum[i] + num
		sumCount[prefixSum[i+1]] += 1

		sum := prefixSum[i+1]
		// if itself is k
		if sum == k {
			count += 1
		}

		// if sum-k exist in previous subarray
		// ex. [1,-1,0], 0
		if cnt, ok := sumCount[sum-k]; ok {
			if sum-k == sum {
				count += cnt - 1 // exclude itself if k == 0
			} else {
				count += cnt
			}
		}
	}

	return count
}
