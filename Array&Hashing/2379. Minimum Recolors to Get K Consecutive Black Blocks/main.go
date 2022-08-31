// https://leetcode.com/contest/biweekly-contest-85/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
package main

import "math"

/*
6157. Time Needed to Rearrange a Binary String

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
*/

func minimumRecolors(blocks string, k int) int {
	res := math.MaxInt
	l := 0
	for l < len(blocks)-k+1 {
		tmp := 0
		r := l
		for r < len(blocks) && r-l+1 <= k {
			if blocks[r] == 'W' {
				tmp += 1
			}
			r += 1
		}
		res = int(math.Min(float64(res), float64(tmp)))

		l += 1
	}

	return res
}

func minimumRecolorsBetter(blocks string, k int) int {
	res := math.MaxInt

	for i := 0; i < len(blocks); i++ {
		cnt := 0
		for j := i; j < i+k; j++ {
			if blocks[j] == 'W' {
				cnt += 1
			}
		}
		res = int(math.Min(float64(res), float64(cnt)))
	}

	return res
}
