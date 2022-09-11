// https://leetcode.com/problems/optimal-partition-of-string/

package main

// we can be greedy, just search the duplicate position and reset hashmap at each extension
// we can see from below that left pointer doesn't effect the partition count
// https://leetcode.com/problems/optimal-partition-of-string/discuss/2560408/C%2B%2B-oror-JAVA-oror-Easy-solution-Explained-oror-Beginner-Friendly-oror-Best-Method
// T:O(n)
func partitionStringGreedy(s string) int {
	ans := 1
	m := map[byte]bool{}

	for i := 0; i < len(s); i++ {
		// insert Till we find duplicate element.
		if _, ok := m[s[i]]; !ok {
			m[s[i]] = true

			// if we found duplicate char then increment count and clear set and start with new set.
		} else {
			ans += 1
			m = make(map[byte]bool)
			m[s[i]] = true
		}
	}

	return ans
}

// From left to right, extend every substring in the partition as much as possible.
// T:O(n)
func partitionString(s string) int {
	m := map[byte]int{}
	count := 0
	l := 0
	for r := 0; r < len(s); r++ {
		if r == len(s)-1 {
			// if duplicate
			if _, ok := m[s[r]]; ok {
				count += 2

				// add last partition
			} else {
				count += 1
			}
			break
		}

		if _, ok := m[s[r]]; ok {
			count += 1
			for l <= r {
				delete(m, s[l])
				l += 1
			}
			l = r
		}
		m[s[r]] = r
	}

	return count
}
