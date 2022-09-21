package main

// T:O(n) M:O(26)
func lengthOfLongestSubstringKDistinct(s string, k int) int {
	longest := 0

	set := map[byte]int{}
	l := 0
	for r := 0; r < len(s); r++ {
		set[s[r]] += 1

		// keeps slide window valid
		for l < r && len(set) > k {
			set[s[l]] -= 1
			if set[s[l]] == 0 {
				delete(set, s[l])
			}
			l += 1
		}

		longest = max(longest, r-l+1)
	}

	return longest
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
