// https://leetcode.com/problems/permutation-in-string/
package main

import "fmt"

// Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
// In other words, return true if one of s1's permutations is the substring of s2.
//
// Example 1:
// Input: s1 = "ab", s2 = "eidbaooo"
// Output: true
// Explanation: s2 contains one permutation of s1 ("ba").
//
// Example 2:
// Input: s1 = "ab", s2 = "eidboaoo"
// Output: false

// Maps are printed in key-sorted order to ease testing,
// so we can compare by fmt.Sprint
func checkMapEquality(m1, m2 map[byte]int) bool {
	return fmt.Sprint(m1) == fmt.Sprint(m2)
}

// T:O(mn), m:len(s1), n:len(s2)
func checkInclusion(s1 string, s2 string) bool {
	mContainS1 := map[byte]int{}
	for i := range s1 {
		mContainS1[s1[i]] += 1
	}

	l := 0
	for l < len(s2)-len(s1)+1 {
		if _, ok := mContainS1[s2[l]]; !ok {
			l += 1
			continue
		}

		mContainS2 := map[byte]int{}
		r := l + len(s1) - 1
		for i := l; i <= r; i++ {
			mContainS2[s2[i]] += 1
		}
		if checkMapEquality(mContainS1, mContainS2) {
			return true
		}

		l += 1
	}
	return false
}
