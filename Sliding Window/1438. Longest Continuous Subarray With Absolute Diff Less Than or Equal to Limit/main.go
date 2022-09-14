// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/
package main

/*
[1,5,6,7,8,10,6,5,6], limit: 4
l    r      min						max max-min
0    0		  [1]  					[1]
0    1		  [1,5]					[5] 5-1 <= limit
1    2		  [1,5,6]				[6] 6-1 > limit ==> pop l from deque & l+=1
1    3		  [5,6,7] 			[7] 7-5 <= limit
1    4			[5,6,7,8] 		[8] 8-5 <= limit
2    5			[6,7,8,10] 		[10] 10-5 > limit ==> pop l from deque & l+=1
2    6			[6,6]					[10,6] 10-6 <= limit
6    7			[5]						[6,5] 10-5 > limit ==> pop l & l+=1 until valid
expected: 5
*/

// https://www.youtube.com/watch?v=p8-f0_CwWLk
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)
// T:O(n) M:O(n)
func longestSubarray(nums []int, limit int) int {
	dequeMax := []int{}
	dequeMin := []int{}
	maxLen := 0
	l := 0
	for r, num := range nums {
		for len(dequeMax) > 0 && nums[dequeMax[len(dequeMax)-1]] < num {
			dequeMax = dequeMax[:len(dequeMax)-1]
		}
		for len(dequeMin) > 0 && nums[dequeMin[len(dequeMin)-1]] > num {
			dequeMin = dequeMin[:len(dequeMin)-1]
		}

		dequeMax = append(dequeMax, r)
		dequeMin = append(dequeMin, r)

		for nums[dequeMax[0]]-nums[dequeMin[0]] > limit {
			if dequeMax[0] == l {
				dequeMax = dequeMax[1:]
			}
			if dequeMin[0] == l {
				dequeMin = dequeMin[1:]
			}
			l += 1
		}
		maxLen = Max(maxLen, r-l+1)
	}

	return maxLen
}

func Max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
