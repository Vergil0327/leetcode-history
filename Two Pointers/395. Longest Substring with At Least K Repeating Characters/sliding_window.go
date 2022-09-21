package main

// Intuition:
// 	There is another intuitive method to solve the problem by using the Sliding Window Approach.
// 	The sliding window slides over the string s and validates each character.
// 	Based on certain conditions, the sliding window either expands or shrinks.
// 	A substring is valid if each character has at least k frequency.
// 	The main idea is to find all the valid substrings with a different number of unique characters and track the maximum length.
// Algorithm:
// 	1. Find the number of unique characters in the string s and store the count in variable maxUnique. For s = aabcbacad, the unique characters are a,b,c,d and maxUnique = 4.
// 	2. Iterate over the string s with the value of currUnique ranging from 1 to maxUnique. In each iteration, currUnique is the maximum number of unique characters that must be present in the sliding window.
// 	3. The sliding window starts at index windowStart and ends at index windowEnd and slides over string s until windowEnd reaches the end of string s. At any given point, we shrink or expand the window to ensure that the number of unique characters is not greater than currUnique.
// 	4. If the number of unique character in the sliding window is less than or equal to currUnique, expand the window from the right by adding a character to the end of the window given by windowEnd
// 	5. Otherwise, shrink the window from the left by removing a character from the start of the window given by windowStart.
// 	6. Keep track of the number of unique characters in the current sliding window having at least k frequency given by countAtLeastK. Update the result if all the characters in the window have at least k frequency.

// https://www.youtube.com/watch?v=_MJKUvM-4fM&ab_channel=HuifengGuan
// use two-pointers sliding window that constraints with m different characters at most
// repeat m from 1 to 26. 26 lowercase English character at most
// T:O(26n)
// M:O(26)
func longestSubstringSlidingWindow(s string, k int) int {
	longest := 0
	for m := 1; m < 26; m++ {
		longest = max(longest, slidingWindow(s, m, k))
	}

	return longest
}

// T:O(maxUnique * n)
// M:O(26)
func longestSubstringSlidingWindowOptimized(s string, k int) int {
	ch := map[byte]bool{}
	for i := range s {
		ch[s[i]] = true
	}
	maxUniq := len(ch)

	longest := 0
	for m := 1; m <= maxUniq; m++ {
		longest = max(longest, slidingWindow(s, m, k))
	}

	return longest
}

func slidingWindow(s string, m, k int) int {
	longest := 0
	count := 0 // count of valid character(freq >= k)
	freq := map[byte]int{}

	l := 0
	for r := 0; r < len(s); r++ {
		freq[s[r]] += 1
		if freq[s[r]] == k {
			count += 1
		}

		if len(freq) == m && count == m {
			longest = max(longest, r-l+1)
		}

		// frequently add/delete hashmap is inefficient, maybe we can use count array instead and extra variable to keep tracks of m corresponding to count array
		for l < r && len(freq) > m {
			freq[s[l]] -= 1
			if freq[s[l]] == k-1 {
				count -= 1
			}
			if freq[s[l]] == 0 {
				delete(freq, s[l])
			}
			l += 1
		}
	}

	return longest
}
