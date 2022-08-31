// https://leetcode.com/problems/partition-labels/
package main

import (
	"math"
)

/*
Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
*/

func partitionLabels(s string) []int {
	pos := map[rune][]int{}

	i := 0
	for i < len(s) {
		pos[rune(s[i])] = append(pos[rune(s[i])], i)
		i += 1
	}

	res := []int{}
	currStart, currEnd := -1, -1
	for _, ch := range s {
		start, end := pos[ch][0], pos[ch][len(pos[ch])-1]
		if currStart == -1 {
			currStart = start
		}
		if currEnd == -1 {
			currEnd = end
		}

		if start <= currEnd {
			currEnd = int(math.Max(float64(currEnd), float64(end)))
		} else {
			res = append(res, currEnd-currStart+1)
			currStart, currEnd = start, end
		}
	}
	res = append(res, currEnd-currStart+1)

	return res
}

// explanation: https://www.youtube.com/watch?v=B7m8UmZE-vw
// T:O(n) M:O(1) only 26 characters
func partitionLabelsNeetCode(s string) []int {
	lastIdx := map[rune]int{}
	for i, ch := range s {
		lastIdx[ch] = i
	}

	res := []int{}
	size, end := 0, 0
	for i, ch := range s {
		size += 1
		end = int(math.Max(float64(end), float64(lastIdx[ch])))

		if i == end {
			res = append(res, size)
			size = 0
		}
	}

	return res
}
