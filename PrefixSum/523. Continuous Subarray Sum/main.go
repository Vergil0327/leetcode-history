package main

// Neetcode explanation: https://youtu.be/OKcrLfR-8mE
// why store remainder ?
// because if we got duplicate remainder, it means we increment our sum by multiple of k
// 5%6= 5 -> 5+6%6 = 5
// T:O(n)
func checkSubarraySum(nums []int, k int) bool {
	sum := 0

	// edge case: [0, ...], size of [0] is 1, so we can't return true although 0 is always a multiple of k
	// [0,0] -> true for any k
	remainderIdx := map[int]int{0: -1} // { [remainder]: index }

	for i, num := range nums {
		sum += num
		remainder := sum % k

		if j, ok := remainderIdx[remainder]; !ok {
			remainderIdx[remainder] = i
		} else if i-j > 1 { // size of array should be 2 at least
			return true
		}
	}

	return false
}

// Brute Force, O(n^2)
func checkSubarraySumTLE(nums []int, k int) bool {
	prefixSum := make([]int, len(nums)+1)
	for i, num := range nums {
		prefixSum[i+1] = prefixSum[i] + num
	}

	for l := 0; l < len(prefixSum)-2; l++ {
		for r := l + 2; r < len(prefixSum); r++ {
			if check(prefixSum[r]-prefixSum[l], k) {
				return true
			}
		}
	}

	return false
}

func check(sum int, k int) bool {
	return sum%k == 0
}
