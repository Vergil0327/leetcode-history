package main

/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
*/

// T:O(n)
func getFingerPrint(str string) (output [26]int) {
	for _, ch := range str {
		output[ch-'a'] += 1
	}
	return
}

// T: O(m*n*26), M:O(n), m:len(strs), n:len(str)
func groupAnagrams(strs []string) [][]string {
	output := [][]string{}
	m := map[[26]int][]string{}
	for _, str := range strs {
		m[getFingerPrint(str)] = append(m[getFingerPrint(str)], str)
	}

	for _, anagrams := range m {
		output = append(output, anagrams)
	}

	return output
}
