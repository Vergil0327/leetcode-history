// https://leetcode.com/problems/powx-n/

package main

import "math"

/*
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

2.00000
-2147483648

*/

// Divide & conquer
// explanation: https://www.youtube.com/watch?v=g9YQyYi4IQQ
func myPow(x float64, n int) float64 {
	var pow func(x float64, n int) float64

	pow = func(x float64, n int) float64 {
		if x == 0 {
			return 0
		}
		if x == 1 {
			return 1
		}

		if n == 0 {
			return 1
		}

		if n%2 == 0 {
			return pow(x*x, n/2)
		} else {
			return pow(x*x, n/2) * x
		}
	}

	if val := pow(x, int(math.Abs(float64(n)))); n >= 0 {
		return val
	} else {
		return 1 / val
	}
}
