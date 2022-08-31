// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
package main

import (
	"math"
)

/*
Example 1:
Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

Example 2:
Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:
Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
*/

// T:O(n) M:O(1)
// discuss: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/discuss/1253874/C%2B%2B-Solution-sliding-window.-O(N)-Time-O(1)-Space
func minFlips(s string) int {
	n := len(s)

	flips := len(s)
	diff1 := 0 // 0101010101...
	diff2 := 0 // 1010101010...
	for i := 0; i < 2*len(s); i++ {
		var letter int
		if i < n {
			// make '1' and '0' to be integer 1 and 0.
			letter = int(s[i] - '0')
		} else {
			// make '1' and '0' to be integer 1 and 0.
			letter = int(s[i-n] - '0')
		}

		if i%2 != letter {
			diff1 += 1
		}

		if (i+1)%2 != letter {
			diff2 += 1
		}

		//the most left element is outside of sliding window, we need to subtract the ans if we did `flip` before.
		if i >= n {
			if (i-n)%2 != letter {
				diff1 -= 1
			}
			if (i+1-n)%2 != letter {
				diff2 -= 1
			}
		}
		if i >= n-1 {
			flips = int(math.Min(float64(flips), math.Min(float64(diff1), float64(diff2))))
		}
	}

	return flips
}

// explanation: https://www.youtube.com/watch?v=MOeuK6gaC2A
// T:O(2n) M:O(n)
func minFlipsBetter(s string) int {
	windowSize := len(s)
	s = s + s

	// starts with 0 & 1 separately
	targetStr1, targetStr2 := "", ""
	for i := range s {
		if i%2 == 0 {
			targetStr1 += "0"
		} else {
			targetStr1 += "1"
		}

		if i%2 == 0 {
			targetStr2 += "1"
		} else {
			targetStr2 += "0"
		}
	}

	flips := len(s)
	diff1, diff2 := 0, 0
	l := 0
	for r := 0; r < len(s); r++ {
		if s[r] != targetStr1[r] {
			diff1 += 1
		}
		if s[r] != targetStr2[r] {
			diff2 += 1
		}

		//the most left element is outside of sliding window, we need to subtract the ans if we did `flip` before.
		if r-l+1 > windowSize {
			if s[l] != targetStr1[l] {
				diff1 -= 1
			}
			if s[l] != targetStr2[l] {
				diff2 -= 1
			}
			l += 1
		}

		if r-l+1 == windowSize {
			flips = int(math.Min(float64(flips), math.Min(float64(diff1), float64(diff2))))
		}
	}

	return flips
}

// T:(n^2)
func minFlipsSlow(s string) int {
	if len(s) <= 1 {
		return 0
	}

	min := math.MaxInt

	n := len(s)
	str := s
	for n > 0 {
		count := 0
		ptr := 0
		start := str[0]
		for ptr < len(s) {
			if ptr%2 == 0 && str[ptr] != start {
				count += 1
			}
			if ptr%2 != 0 && str[ptr] == start {
				count += 1
			}
			ptr += 1
		}

		if count < min {
			min = count
		}
		str = str[1:] + string(str[0])
		n -= 1
	}

	return min
}
