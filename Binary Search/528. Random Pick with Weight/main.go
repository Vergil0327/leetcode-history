// https://leetcode.com/problems/random-pick-with-weight/
package main

import (
	"math/rand"
)

// https://leetcode.com/problems/random-pick-with-weight/discuss/154044/Java-accumulated-freq-sum-and-binary-search
type Solution struct {
	searchSpace []int
}

func Constructor(w []int) Solution {
	prefixSum := make([]int, len(w)+1)
	for i := 0; i < len(w); i++ {
		prefixSum[i+1] = prefixSum[i] + w[i]
	}
	prefixSum = prefixSum[1:]

	return Solution{
		searchSpace: prefixSum,
	}
}

// find upperbound
// [3,14,1,7]=>[3,17,18,25]
// 1-3 -> return 0
// 4-17 -> return 1
// 18 -> return 2
// 19-25 -> return 3
func (this *Solution) PickIndex() int {
	l, r := 0, len(this.searchSpace)-1

	/*
		Example:
		Let's assume the same weights are: [2, 7, 3, 3]
		The prefix sum becomes: [2, 9, 12, 15]
		The maximum in this range is 15.
		Note: The binary search algorithm here finds the upper bound index. For random numbers [10, 11, 12], we would want index 2.

		Random.nextInt(15)
		This generates random numbers in the range (0, 14).
		So for random numbers in range [0, 2], index 0 will be picked.
		For random numbers in range [3, 9] index 1 will be picked.
		And for random numbers in range [13, 14] index 3 will be picked.
		Conclusion: This yields incorrect probability distribution for Index 0 and 3, because we want index 0 to be picked 2 times and not 3 times because of range [0, 2]. Similarly, we want index 3 to be picked 3 times instead of 2 times because of range [13, 14].

		Random.nextInt(15 + 1)
		This generates random numbers in the range (0, 14).
		So for random numbers in range [0, 2], index 0 will be picked.
		And for random numbers in range [13, 15] index 3 will be picked.
		Conclusion: This corrects the probability distribution for index 3, but distribution for index 0 i still incorrect

		Random.nextInt(15) + 1
		This generates random numbers in the range (1, 15).
		So for random numbers in range [1, 2], index 0 will be picked.
		And for random numbers in range [13, 15] index 3 will be picked.
		Conclusion: This corrects the probability distribution for index 3 as well as index 0, and hence the correct solution.
	*/
	idx := int(rand.Int31n(int32(this.searchSpace[len(this.searchSpace)-1]))) + 1 // [1,this.searchSpace[len(this.searchSpace)-1]]

	for l < r {
		mid := l + (r-l)/2
		if idx > this.searchSpace[mid] {
			l = mid + 1
		} else if idx < this.searchSpace[mid] {
			r = mid
		} else {
			return mid
		}
	}

	return l
}

/**
* Your Solution object will be instantiated and called as such:
* obj := Constructor(w);
* param_1 := obj.PickIndex();
 */
