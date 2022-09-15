// https://leetcode.com/problems/sqrtx/
package main

// binary search upper bound
// T: log(x)
func mySqrt(x int) int {
	l, r := 0, x
	for l <= r {
		mid := l + (r-l)/2
		if x > mid*mid {
			l = mid + 1
		} else if x < mid*mid {
			r = mid - 1
		} else {
			return mid
		}
	}

	// l = r+1, so r is lower bound we want
	return r
}
