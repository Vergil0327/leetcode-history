// https://leetcode.com/problems/koko-eating-bananas/
package main

import (
	"math"
)

// Example 1:
// Input: piles = [3,6,7,11], h = 8
// Output: 4

// Example 2:
// Input: piles = [30,11,23,4,20], h = 5
// Output: 30

// Example 3:
// Input: piles = [30,11,23,4,20], h = 6
// Output: 23

// target: return minimum speed if sum <= h
// speed is minumum when sum == h
// T: O( log(max(p))*p)
func minEatingSpeed(piles []int, h int) int {
	var max int
	for _, v := range piles {
		if v > max {
			max = v
		}
	}

	bot, top := 1, max

	for bot < top {
		// mid := top - (top-bot)/2 // cause dead loop ex. [1, 2]
		mid := bot + (top-bot)/2

		count := checkOK(piles, h, mid)

		if count <= h {
			top = mid // mid 可能是答案不能排除
		} else {
			bot = mid + 1 // 因為count > h，所以mid不會是答案，得排除掉
		}
	}

	return top
}

func checkOK(piles []int, h, mid int) int {
	count := 0
	for _, v := range piles {
		count += int(math.Ceil(float64(v) / float64(mid)))
	}
	return count
}
