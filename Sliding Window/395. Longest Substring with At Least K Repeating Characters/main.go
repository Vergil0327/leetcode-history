// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
package main

// T:O(26*n^2)
func longestSubstringBruteForce(s string, k int) int {
	longest := 0
	for i := 0; i < len(s); i++ {
		freq := make(map[byte]int)
		for j := i; j < len(s); j++ {
			freq[s[j]] += 1
			if checkFreq(freq, k) {
				longest = max(longest, j-i+1)
			}
		}
	}

	return longest
}

// T:O(26)
func checkFreq(m map[byte]int, k int) bool {
	for _, v := range m {
		if v < k {
			return false
		}
	}
	return true
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
Intuition:

Divide and Conquer is one of the popular strategies that work in 2 phases.

Divide the problem into subproblems. (Divide Phase).
Repeatedly solve each subproblem independently and combine the result to solve the original problem. (Conquer Phase).
We could apply this strategy by recursively splitting the string into substrings and combine the result to find the longest substring that satisfies the given condition.
The longest substring for a string starting at index start and ending at index end can be given by,

		longestSustring(start, end) = max(longestSubstring(start, mid), longestSubstring(mid+1, end))

Finding the split position (mid)
The string would be split only when we find an invalid character.
An invalid character is the one with a frequency of less than k.
As we know, the invalid character cannot be part of the result, we split the string at the index where we find the invalid character, recursively check for each split, and combine the result.

Algorithm:

- Build the countMap with the frequency of each character in the string s.
- Find the position for mid index by iterating over the string. The mid index would be the first invalid character in the string.
- Split the string into 2 substrings at the mid index and recursively find the result.
- To make it more efficient, we ignore all the invalid characters after the mid index as well, thereby reducing the number of recursive calls.

```java
class Solution {
    public int longestSubstring(String s, int k) {
        return longestSubstringUtil(s, 0, s.length(), k);
    }

    int longestSubstringUtil(String s, int start, int end, int k) {
        if (end < k) return 0;
        int[] countMap = new int[26];
        // update the countMap with the count of each character
        for (int i = start; i < end; i++)
            countMap[s.charAt(i) - 'a']++;
        for (int mid = start; mid < end; mid++) {
            if (countMap[s.charAt(mid) - 'a'] >= k) continue;
            int midNext = mid + 1;
            while (midNext < end && countMap[s.charAt(midNext) - 'a'] < k) midNext++;
            return Math.max(longestSubstringUtil(s, start, mid, k),
                    longestSubstringUtil(s, midNext, end, k));
        }
        return (end - start);
    }
}
```

Time Complexity: O(N^2), where N is the length of string s.
Though the algorithm performs better in most cases, the worst case time complexity is still O(N^2)
In cases where we perform split at every index, the maximum depth of recursive call could be O(N).
For each recursive call it takes O(N) time to build the countMap resulting in O(n^2) time complexity.

Space Complexity: O(N)
This is the space used to store the recursive call stack.
The maximum depth of recursive call stack would be O(N)
*/

// https://youtu.be/_MJKUvM-4fM
func longestSubstring(s string, k int) int {
	var longestSubstringUtil func(start, end int) int
	longestSubstringUtil = func(start, end int) int {
		if end < k {
			return 0
		}

		countMap := make([]int, 26)
		// update the countMap with the count of each characters
		for i := start; i < end; i++ {
			countMap[s[i]-'a'] += 1
		}

		for mid := start; mid < end; mid++ {
			if countMap[s[mid]-'a'] >= k {
				continue
			}

			midNext := mid + 1
			// skip invalid
			for midNext < end && countMap[s[midNext]-'a'] < k {
				midNext += 1
			}

			return max(longestSubstringUtil(start, mid), longestSubstringUtil(midNext, end))
		}

		return end - start
	}

	return longestSubstringUtil(0, len(s))
}
