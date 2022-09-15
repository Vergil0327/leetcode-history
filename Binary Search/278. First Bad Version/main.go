// https://leetcode.com/problems/first-bad-version/
package main

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 */
func isBadVersion(version int) bool

func firstBadVersion(n int) int {
	l, r := 1, n

	for l < r {
		mid := l + (r-l)/2
		if !isBadVersion(mid) {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return l
}
